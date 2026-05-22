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
                await asyncio.sleep(0.5 * (attempt + 1))
                
        return last_result or TestResult(
            provider=provider,
            model=model,
            capability=cap,
            status=Status.EXCEPTION,
            response_time=0.0,
            error="Failed with unknown error"
        )