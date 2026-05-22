from __future__ import annotations
import asyncio
from typing import List, Coroutine, Any
from g4f.client import AsyncClient

from .text import TextTester
from .image import ImageTester
from .audio import AudioTester
from .video import VideoTester
from ..models import ProviderReport, TestResult, Capability

class Tester:
    def __init__(self, client: AsyncClient, max_concurrent: int):
        self.client = client
        self.sem = asyncio.Semaphore(max_concurrent)
        
        self.text_tester = TextTester(client, self.sem)
        self.image_tester = ImageTester(client, self.sem)
        self.audio_tester = AudioTester(client, self.sem)
        self.video_tester = VideoTester(client, self.sem)

    def _get_runner(self, cap: Capability):
        if cap == Capability.TEXT:
            return self.text_tester.test
        if cap == Capability.IMAGE:
            return self.image_tester.test
        if cap == Capability.AUDIO:
            return self.audio_tester.test
        if cap == Capability.VIDEO:
            return self.video_tester.test
        return None

    async def test_provider(self, report: ProviderReport, progress_cb=None) -> None:
        tasks: List[Coroutine[Any, Any, TestResult]] = []
        
        for meta in report.models_meta:
            model_id = meta.get("id")
            if not model_id:
                continue
                
            caps = meta.get("capabilities", [])
            for cap_val in caps:
                cap = Capability(cap_val)
                runner = self._get_runner(cap)
                if runner:
                    tasks.append(runner(report.name, model_id))
                    
        for coro in asyncio.as_completed(tasks):
            try:
                res = await coro
                report.results.append(res)
                if progress_cb:
                    progress_cb(res)
            except Exception:
                pass