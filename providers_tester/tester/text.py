from __future__ import annotations
import time
from .base import BaseTester
from ..models import TestResult, Capability, Status
from ..config import CONFIG
from ..validators import validate_text_ping_response

class TextTester(BaseTester):
    async def test(self, provider: str, model: str) -> TestResult:
        async def _run():
            t0 = time.monotonic()
            parts: list[str] = []
            
            response = self.client.chat.completions.create(
                model=model,
                provider=provider,
                messages=[{"role": "user", "content": CONFIG.ping_prompt}],
                stream=True
            )
            
            async for chunk in response:
                if hasattr(chunk, "choices") and chunk.choices:
                    delta = getattr(chunk.choices[0], "delta", None)
                    if delta:
                        content = getattr(delta, "content", None)
                        if content:
                            parts.append(content)
                elif isinstance(chunk, str):
                    parts.append(chunk)
                elif isinstance(chunk, dict):
                    choices = chunk.get("choices")
                    if choices and len(choices) > 0 and choices[0] is not None:
                        delta = choices[0].get("delta", {})
                        content = delta.get("content")
                        if content:
                            parts.append(content)
            
            dt = time.monotonic() - t0
            text = "".join(parts).strip()
            
            if not text:
                return TestResult(provider, model, Capability.TEXT, Status.EMPTY, dt, error="Empty response")
                
            v = validate_text_ping_response(text, CONFIG.ping_expected_token)
            return TestResult(
                provider=provider,
                model=model,
                capability=Capability.TEXT,
                status=Status.OK if v.valid else Status.INVALID_CONTENT,
                response_time=dt,
                response_preview=text[:120],
                validation_note=v.note,
                error=None if v.valid else v.note
            )
            
        return await self.run_with_retry(provider, model, Capability.TEXT, _run)