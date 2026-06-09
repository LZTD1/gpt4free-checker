from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional, List

class Capability(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"


class Status(str, Enum):
    OK = "ok"
    INVALID_CONTENT = "invalid"
    HTTP_ERROR = "http_error"
    API_ERROR = "api_error"
    RATE_LIMITED = "rate_limited"
    TIMEOUT = "timeout"
    EMPTY = "empty"
    EXCEPTION = "exception"
    SKIPPED = "skipped"


@dataclass
class TestResult:
    provider: str
    model: str
    capability: Capability
    status: Status
    response_time: float
    response_preview: Optional[str] = None
    error: Optional[str] = None
    validation_note: Optional[str] = None

    @property
    def working(self) -> bool:
        return self.status == Status.OK

    def to_dict(self) -> dict:
        d = asdict(self)
        d["capability"] = self.capability.value
        d["status"] = self.status.value
        d["working"] = self.working
        return d


@dataclass
class ProviderReport:
    name: str
    url: Optional[str] = None
    label: Optional[str] = None
    model_count: int = 0
    results: List[TestResult] = field(default_factory=list)
    fetch_error: Optional[str] = None
    models_meta: List[dict] = field(default_factory=list)

    @property
    def working_results(self) -> List[TestResult]:
        return [r for r in self.results if r.working]

    @property
    def working(self) -> bool:
        return len(self.working_results) > 0

    @property
    def avg_response_time(self) -> float:
        ok = self.working_results
        return sum(r.response_time for r in ok) / len(ok) if ok else 0.0