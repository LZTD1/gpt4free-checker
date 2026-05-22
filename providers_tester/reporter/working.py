from __future__ import annotations
import json
from pathlib import Path
from ..models import ProviderReport

class WorkingReporter:
    def __init__(self, reports_dir: Path):
        self.reports_dir = reports_dir

    def write(self, reports: list[ProviderReport]) -> None:
        rows: list[str] = []
        working_list = []
        by_cap: dict[str, list[dict]] = {"text": [], "image": [], "audio": [], "video": []}

        for r in reports:
            for res in r.working_results:
                rows.append(
                    f"{res.provider}|{res.model}|{res.capability.value}|{res.response_time:.3f}"
                )
                
                entry = {
                    "provider": res.provider,
                    "model": res.model,
                    "capability": res.capability.value,
                    "response_time": round(res.response_time, 3)
                }
                working_list.append(entry)
                
                if res.capability.value in by_cap:
                    by_cap[res.capability.value].append(entry)

        rows.sort()
        (self.reports_dir / "working.txt").write_text(
            "\n".join(rows) + ("\n" if rows else ""), encoding="utf-8"
        )
        
        (self.reports_dir / "working.json").write_text(
            json.dumps(working_list, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        
        (self.reports_dir / "working_by_capability.json").write_text(
            json.dumps(by_cap, indent=2, ensure_ascii=False), encoding="utf-8"
        )