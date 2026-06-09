from __future__ import annotations
import asyncio
import logging
import random
from typing import Callable, Optional
from g4f.client import AsyncClient

from .text import TextTester
from .image import ImageTester
from .audio import AudioTester
from .video import VideoTester
from ..models import ProviderReport, TestResult, Capability
from ..config import CONFIG

log = logging.getLogger(__name__)


class Tester:
    def __init__(self, client: AsyncClient, max_concurrent: int):
        self.client = client
        # Семафор ограничивает число ОДНОВРЕМЕННЫХ ПРОВАЙДЕРОВ (разные хосты)
        # Внутри каждого провайдера модели идут строго по очереди → нет pile-up на один хост
        self.provider_sem = asyncio.Semaphore(max_concurrent)

        # Тестеры без семафора — сериализация теперь на уровне провайдера
        self.text_tester  = TextTester(client)
        self.image_tester = ImageTester(client)
        self.audio_tester = AudioTester(client)
        self.video_tester = VideoTester(client)

    def _get_runner(self, cap: Capability) -> Optional[Callable]:
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
        """
        Захватываем один слот семафора на весь провайдер.
        Внутри — модели тестируются строго последовательно с паузой между ними.
        Это исключает одновременные запросы в один хост → резко снижает 429.
        """
        async with self.provider_sem:
            for meta in report.models_meta:
                model_id = meta.get("id")
                if not model_id:
                    continue

                caps = meta.get("capabilities", [])
                for cap_val in caps:
                    cap = Capability(cap_val)
                    runner = self._get_runner(cap)
                    if not runner:
                        continue

                    try:
                        res = await runner(report.name, model_id)
                        report.results.append(res)
                        if progress_cb:
                            progress_cb(res)
                    except Exception:
                        log.debug(
                            "Unhandled exception in runner for %s / %s (%s)",
                            report.name, model_id, cap_val, exc_info=True
                        )

                    # Пауза между моделями одного провайдера — ключевой anti-429 механизм.
                    # Джиттер десинхронизирует параллельные провайдеры → нет "волн" запросов.
                    jitter = random.uniform(0.0, CONFIG.inter_model_pause_jitter)
                    await asyncio.sleep(CONFIG.inter_model_pause + jitter)
