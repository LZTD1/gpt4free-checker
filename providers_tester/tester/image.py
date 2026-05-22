from __future__ import annotations
import time
from .base import BaseTester
from ..models import TestResult, Capability, Status
from ..config import CONFIG

class ImageTester(BaseTester):
    async def test(self, provider: str, model: str) -> TestResult:
        async def _run():
            t0 = time.monotonic()
            
            data = await self.client.images.generate(
                model=model,
                provider=provider,
                prompt=CONFIG.image_prompt
            )
            
            dt = time.monotonic() - t0
            url = None
            
            if hasattr(data, "data") and data.data:
                url = data.data[0].url
            elif isinstance(data, dict) and "data" in data and data["data"]:
                url = data["data"][0].get("url") or data["data"][0].get("b64_json")
            elif isinstance(data, str):
                url = data
                
            if not url:
                return TestResult(provider, model, Capability.IMAGE, Status.EMPTY, dt, error="No image url/payload returned")
                
            preview = url[:100] if not url.startswith("data:") else "Base64 payload"
            return TestResult(
                provider=provider,
                model=model,
                capability=Capability.IMAGE,
                status=Status.OK,
                response_time=dt,
                response_preview=preview,
                validation_note="Valid image generation output"
            )
            
        return await self.run_with_retry(provider, model, Capability.IMAGE, _run)