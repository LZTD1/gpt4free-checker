from __future__ import annotations
from dataclasses import dataclass, field
import os
from typing import Optional, List

@dataclass(frozen=True)
class Config:
    base_url: str = "http://127.0.0.1:8081"
    api_key: str = "test-key"
    port: int = 8081

    request_timeout: int = 25
    server_startup_timeout: int = 60
    server_poll_interval: float = 1.0

    max_concurrent: int = 8
    inter_batch_pause: float = 0.5
    retries_count: int = 1

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