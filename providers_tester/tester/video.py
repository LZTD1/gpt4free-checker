from __future__ import annotations
import time
from .base import BaseTester
from ..models import TestResult, Capability, Status
from ..config import CONFIG

class VideoTester(BaseTester):
    async def test(self, provider: str, model: str) -> TestResult:
        async def _run():
            t0 = time.monotonic()
            
            response = self.client.chat.completions.create(
                model=model,
                provider=provider,
                messages=[{"role": "user", "content": CONFIG.video_prompt}],
                stream=True
            )
            
            found_url = None
            async for chunk in response:
                if hasattr(chunk, "choices") and chunk.choices:
                    choice = chunk.choices[0]
                    delta = getattr(choice, "delta", None)
                    message = getattr(choice, "message", None) or delta
                    if message:
                        video = getattr(message, "video", None)
                        if isinstance(video, dict) and video.get("url"):
                            found_url = video["url"]
                            break
                        elif isinstance(video, str):
                            found_url = video
                            break
                elif isinstance(chunk, dict):
                    choices = chunk.get("choices")
                    if choices and len(choices) > 0 and choices[0] is not None:
                        delta = choices[0].get("delta", {})
                        message = choices[0].get("message") or delta
                        video = message.get("video")
                        if isinstance(video, dict) and video.get("url"):
                            found_url = video["url"]
                            break
                        elif isinstance(video, str):
                            found_url = video
                            break
            
            dt = time.monotonic() - t0
            if not found_url:
                return TestResult(provider, model, Capability.VIDEO, Status.EMPTY, dt, error="No video URL extracted")
                
            return TestResult(
                provider=provider,
                model=model,
                capability=Capability.VIDEO,
                status=Status.OK,
                response_time=dt,
                response_preview=found_url[:100],
                validation_note="Video payload returned"
            )
            
        return await self.run_with_retry(provider, model, Capability.VIDEO, _run)