from __future__ import annotations
import time
import os
import tempfile
import asyncio
from pathlib import Path
from .base import BaseTester
from ..models import TestResult, Capability, Status
from ..config import CONFIG
from ..validators import validate_binary_media

class AudioTester(BaseTester):
    async def test(self, provider: str, model: str) -> TestResult:
        async def _run():
            t0 = time.monotonic()
            
            response = await self.client.chat.completions.create(
                model=model,
                provider=provider,
                messages=[{"role": "user", "content": CONFIG.audio_prompt}],
                audio={"voice": "alloy", "format": "mp3"}
            )
            
            dt = time.monotonic() - t0
            data = b""
            
            if hasattr(response, "choices") and response.choices:
                message = response.choices[0].message
                if hasattr(message, "save"):
                    with tempfile.TemporaryDirectory() as tmpdir:
                        filepath = os.path.join(tmpdir, "audio.mp3")
                        if asyncio.iscoroutinefunction(message.save):
                            await message.save(filepath)
                        else:
                            message.save(filepath)
                        if os.path.exists(filepath):
                            data = Path(filepath).read_bytes()
                elif hasattr(message, "content") and isinstance(message.content, bytes):
                    data = message.content
                    
            if not data:
                return TestResult(provider, model, Capability.AUDIO, Status.EMPTY, dt, error="No audio payload detected")
                
            v = validate_binary_media(data, min_size=512)
            return TestResult(
                provider=provider,
                model=model,
                capability=Capability.AUDIO,
                status=Status.OK if v.valid else Status.INVALID_CONTENT,
                response_time=dt,
                response_preview=f"Binary stream: {len(data)} bytes",
                validation_note=v.note,
                error=None if v.valid else v.note
            )
            
        return await self.run_with_retry(provider, model, Capability.AUDIO, _run)