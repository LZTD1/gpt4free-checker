from __future__ import annotations
from pathlib import Path
from ..models import ProviderReport

class PerProviderReporter:
    def __init__(self, providers_dir: Path):
        self.providers_dir = providers_dir

    def write(self, report: ProviderReport) -> None:
        def safe_name(name: str) -> str:
            cleaned = "".join(c if c.isalnum() or c in "-_." else "_" for c in name)
            if cleaned.upper() in ("CON", "PRN", "AUX", "NUL", "COM1", "LPT1"):
                cleaned = f"_{cleaned}"
            return cleaned

        path = self.providers_dir / f"{safe_name(report.name)}.md"
        ok = report.working_results

        by_model: dict[str, list] = {}
        for res in report.results:
            by_model.setdefault(res.model, []).append(res)

        lines = [
            f"# {report.name}",
            "",
            f"- **Label:** {report.label or '—'}",
            f"- **URL:** {report.url or '—'}",
            f"- **Models:** {report.model_count}",
            f"- **Working tests:** {len(ok)} / {len(report.results)}",
            f"- **Avg response time:** " + (f"{report.avg_response_time:.2f}s" if ok else "—"),
            "",
        ]

        if report.fetch_error:
            lines += [f"> ⚠️ Fetch error: `{report.fetch_error}`", ""]

        lines += [
            "## Per-model results",
            "",
            "| Model | Capability | Status | Time | Notes |",
            "| --- | --- | :---: | ---: | --- |",
        ]
        sorted_models = sorted(
            by_model.items(),
            key=lambda kv: (not any(r.working for r in kv[1]), kv[0].lower()),
        )
        for model, results in sorted_models:
            for res in sorted(results, key=lambda r: r.capability.value):
                badge = "✅" if res.working else "❌"
                note = res.validation_note or res.error or ""
                note = note.replace("|", "\\|")[:160]
                lines.append(
                    f"| `{model}` | {res.capability.value} | {badge} `{res.status.value}` "
                    f"| {res.response_time:.2f}s | {note} |"
                )

        if ok:
            lines += [
                "",
                "## Sample successful responses",
                "",
            ]
            for res in ok[:10]:
                if not res.response_preview:
                    continue
                lines += [
                    f"### `{res.model}` — {res.capability.value}",
                    "",
                    "```",
                    res.response_preview,
                    "```",
                    "",
                ]

        path.write_text("\n".join(lines) + "\n", encoding="utf-8")