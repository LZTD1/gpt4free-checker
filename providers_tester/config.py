from __future__ import annotations
from dataclasses import dataclass, field
import os
from typing import Optional, List

@dataclass(frozen=True)
class Config:
    base_url: str = "http://127.0.0.1:8081"
    api_key: str = "test-key"
    port: int = 8081

    # Таймаут увеличен до 45с — бесплатные провайдеры часто медленные
    request_timeout: int = 45
    server_startup_timeout: int = 60
    server_poll_interval: float = 1.0

    # Число ОДНОВРЕМЕННЫХ ПРОВАЙДЕРОВ (не запросов).
    # Внутри каждого провайдера модели идут строго по очереди → нет pile-up на один хост.
    max_concurrent: int = 10
    # Базовая пауза между моделями одного провайдера — главный anti-429 механизм.
    # Реальная пауза = inter_model_pause + random(0, inter_model_pause_jitter)
    inter_model_pause: float = 1.5
    inter_model_pause_jitter: float = 1.0
    # Оставлен для совместимости, больше не используется в основном цикле
    inter_batch_pause: float = 0.0
    retries_count: int = 2

    reports_dir: str = "reports"
    previous_summary_path: Optional[str] = None

    ping_prompt: str = "Reply with exactly one word and nothing else: PONG"
    ping_expected_token: str = "PONG"
    image_prompt: str = "a single red apple on a white background, minimalist"
    audio_prompt: str = "Hello, this is a short test."
    video_prompt: str = "a cat walking on grass"

    is_ci: bool = os.getenv("GITHUB_ACTIONS") == "true"

    filter_providers: List[str] = field(default_factory=list)
    filter_capabilities: List[str] = field(default_factory=list)
    include_auth: bool = False

CONFIG = Config()