from __future__ import annotations
import asyncio
import logging
import time
from typing import Callable, Any, Coroutine
from g4f.client import AsyncClient
from ..models import TestResult, Capability, Status
from ..config import CONFIG

log = logging.getLogger(__name__)

def classify_exception(exc: Exception) -> Status:
    err_str = f"{type(exc).__name__}: {str(exc)}".lower()
    if any(w in err_str for w in ("timeout", "timed out", "asyncio.exceptions.timeout_error")):
        return Status.TIMEOUT
    if any(w in err_str for w in ("429", "rate limit", "too many requests")):
        return Status.API_ERROR
    if any(w in err_str for w in ("auth", "api key", "unauthorized", "login", "forbidden")):
        return Status.API_ERROR
    if any(w in err_str for w in ("not found", "404", "model_not_found")):
        return Status.HTTP_ERROR
    return Status.EXCEPTION



def extract_retry_after(exc: Exception) -> float | None:
    headers = None
    if hasattr(exc, "headers") and exc.headers:
        headers = exc.headers
    elif hasattr(exc, "response") and hasattr(exc.response, "headers") and exc.response.headers:
        headers = exc.response.headers

    if headers:
        retry_after = headers.get("Retry-After") or headers.get("retry-after")
        if retry_after:
            try:
                return float(retry_after)
            except ValueError:
                pass 

    err_str = str(exc)

    hms_match = re.search(r"try again in (\d+):(\d+):(\d+)", err_str, re.IGNORECASE)
    if hms_match:
        h, m, s = map(int, hms_match.groups())
        return float(h * 3600 + m * 60 + s)

    sec_match = re.search(r"try again in (\d+)\s*(s|sec|second)", err_str, re.IGNORECASE)
    if sec_match:
        return float(sec_match.group(1))

    min_match = re.search(r"try again in (\d+)\s*(m|min|minute)", err_str, re.IGNORECASE)
    if min_match:
        return float(min_match.group(1)) * 60.0

    return None


class BaseTester:
    def __init__(self, client: AsyncClient, sem: asyncio.Semaphore):
        self.client = client
        self.sem = sem

    async def run_with_retry(
        self,
        provider: str,
        model: str,
        cap: Capability,
        test_coro_fn: Callable[[], Coroutine[Any, Any, TestResult]]
    ) -> TestResult:
        retries = CONFIG.retries_count if CONFIG.retries_count >= 0 else 0
        last_result = None
        
        for attempt in range(retries + 1):
            t0 = time.monotonic()
            try:
                async with self.sem:
                    result = await asyncio.wait_for(
                        test_coro_fn(),
                        timeout=float(CONFIG.request_timeout)
                    )
                    if result.working:
                        return result
                    last_result = result
            except asyncio.TimeoutError:
                dt = time.monotonic() - t0
                last_result = TestResult(
                    provider=provider,
                    model=model,
                    capability=cap,
                    status=Status.TIMEOUT,
                    response_time=dt,
                    error="Timeout limit exceeded"
                )
            except Exception as e:
                dt = time.monotonic() - t0
                status = classify_exception(e)
                last_result = TestResult(
                    provider=provider,
                    model=model,
                    capability=cap,
                    status=status,
                    response_time=dt,
                    error=f"{type(e).__name__}: {str(e)[:180]}"
                )
                
            if attempt < retries:
                wait_time = 0.5 * (attempt + 1)  
                
                if last_result.status == Status.API_ERROR:
                    extracted_wait = extract_retry_after(e)
                    if extracted_wait is not None:
                        if extracted_wait > 45.0:
                            log.warning(
                                "Skipping retries for %s -> %s (requested wait of %.1fs exceeds maximum of 45s)",
                                provider, model, extracted_wait
                            )
                            break
                        wait_time = extracted_wait + 1
                        log.info(
                            "Rate limit hit on %s. Smart backing off for %.1fs as requested...",
                            provider, wait_time
                        )

                await asyncio.sleep(wait_time)
                
        return last_result or TestResult(
            provider=provider,
            model=model,
            capability=cap,
            status=Status.EXCEPTION,
            response_time=0.0,
            error="Failed with unknown error"
        )