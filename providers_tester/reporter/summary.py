from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter
from ..models import ProviderReport

class SummaryReporter:
    def __init__(self, reports_dir: Path):
        self.reports_dir = reports_dir

    def build_summary(self, reports: list[ProviderReport]) -> dict:
        all_results = [res for r in reports for res in r.results]
        ok = [res for res in all_results if res.working]

        by_cap = Counter(res.capability.value for res in ok)
        by_status = Counter(res.status.value for res in all_results)
        working_providers = [r.name for r in reports if r.working]

        total_models = sum(r.model_count for r in reports)
        
        return {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "providers_total": len(reports),
            "providers_working": len(working_providers),
            "models_total": total_models,
            "tests_total": len(all_results),
            "tests_ok": len(ok),
            "success_rate_pct": round(100 * len(ok) / len(all_results), 2) if all_results else 0.0,
            "avg_response_time": round(sum(r.response_time for r in ok) / len(ok), 3) if ok else 0.0,
            "by_capability": dict(by_cap),
            "by_status": dict(by_status),
            "working_providers": sorted(working_providers),
        }

    def write(self, summary: dict, reports: list[ProviderReport]) -> None:
        payload = {
            "summary": summary,
            "providers": [
                {
                    "name": r.name,
                    "url": r.url,
                    "label": r.label,
                    "model_count": r.model_count,
                    "working": r.working,
                    "avg_response_time": round(r.avg_response_time, 3),
                    "fetch_error": r.fetch_error,
                    "results": [res.to_dict() for res in r.results],
                }
                for r in reports
            ],
        }
        (self.reports_dir / "summary.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )

        lines = [
            "# g4f providers — daily test report",
            "",
            f"_Generated: `{summary['generated_at']}`_",
            "",
            "## Overview",
            "",
            f"- **Providers:** {summary['providers_working']} / {summary['providers_total']} working",
            f"- **Models discovered:** {summary['models_total']}",
            f"- **Tests run:** {summary['tests_total']}",
            f"- **Successful:** {summary['tests_ok']} ({summary['success_rate_pct']}%)",
            f"- **Avg response time (OK):** {summary['avg_response_time']}s",
            "",
            "## Results by capability",
            "",
            "| Capability | Working |",
            "| --- | ---: |",
        ]
        for cap in ("text", "image", "audio", "video"):
            lines.append(f"| {cap} | {summary['by_capability'].get(cap, 0)} |")

        lines += [
            "",
            "## Results by status",
            "",
            "| Status | Count |",
            "| --- | ---: |",
        ]
        for status, count in sorted(summary["by_status"].items(), key=lambda x: -x[1]):
            lines.append(f"| `{status}` | {count} |")

        lines += [
            "",
            "## Providers",
            "",
            "| Provider | Models | OK | Fail | Avg time | Capabilities | Status |",
            "| --- | ---: | ---: | ---: | ---: | --- | :---: |",
        ]
        
        def safe_name(name: str) -> str:
            cleaned = "".join(c if c.isalnum() or c in "-_." else "_" for c in name)
            if cleaned.upper() in ("CON", "PRN", "AUX", "NUL", "COM1", "LPT1"):
                cleaned = f"_{cleaned}"
            return cleaned

        for r in sorted(reports, key=lambda x: (not x.working, x.name.lower())):
            ok_res = r.working_results
            fail_res = [res for res in r.results if not res.working]
            caps = sorted({res.capability.value for res in ok_res})
            badge = "✅" if r.working else "❌"
            caps_str = ", ".join(caps) if caps else "—"
            avg = f"{r.avg_response_time:.2f}s" if ok_res else "—"
            link = f"[ {r.name} ](providers/{safe_name(r.name)}.md)"
            lines.append(
                f"| {link} | {r.model_count} | {len(ok_res)} | {len(fail_res)} | "
                f"{avg} | {caps_str} | {badge} |"
            )

        (self.reports_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")