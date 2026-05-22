from __future__ import annotations
import json
from pathlib import Path
from .summary import SummaryReporter
from .working import WorkingReporter
from .per_provider import PerProviderReporter
from .diff import DiffReporter
from .badge import BadgeReporter
from ..models import ProviderReport

class Reporter:
    def __init__(self, root: str):
        self.root = Path(root)
        self.providers_dir = self.root / "providers"

    def write_all(self, reports: list[ProviderReport], previous_summary_path: str | None = None) -> dict:
        self.root.mkdir(parents=True, exist_ok=True)
        self.providers_dir.mkdir(parents=True, exist_ok=True)

        summary_rep = SummaryReporter(self.root)
        summary = summary_rep.build_summary(reports)

        summary_rep.write(summary, reports)
        WorkingReporter(self.root).write(reports)

        prov_rep = PerProviderReporter(self.providers_dir)
        for r in reports:
            prov_rep.write(r)

        BadgeReporter(self.root).write(summary)

        curr_summary_file = self.root / "summary.json"
        if curr_summary_file.exists():
            try:
                curr_data = json.loads(curr_summary_file.read_text(encoding="utf-8"))
                DiffReporter(self.root).write(curr_data, previous_summary_path)
            except Exception:
                pass

        return summary