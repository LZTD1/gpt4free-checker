from __future__ import annotations
import json
from pathlib import Path

class DiffReporter:
    def __init__(self, reports_dir: Path):
        self.reports_dir = reports_dir

    def write(self, current_summary_data: dict, previous_summary_path: str | None) -> None:
        prev_data = None
        if previous_summary_path:
            p_path = Path(previous_summary_path)
            if p_path.exists():
                try:
                    prev_data = json.loads(p_path.read_text(encoding="utf-8"))
                except Exception:
                    pass

        lines = [
            "# Daily Change Report (Diff)",
            "",
        ]

        if not prev_data:
            lines.append("_No historical execution summary found to perform analysis comparison._")
            (self.reports_dir / "changes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
            return

        prev_map = {}
        for prov_item in prev_data.get("providers", []):
            prov_name = prov_item.get("name")
            for res_item in prov_item.get("results", []):
                key = (prov_name, res_item.get("model"), res_item.get("capability"))
                prev_map[key] = res_item.get("working", False)

        curr_map = {}
        for prov_item in current_summary_data.get("providers", []):
            prov_name = prov_item.get("name")
            for res_item in prov_item.get("results", []):
                key = (prov_name, res_item.get("model"), res_item.get("capability"))
                curr_map[key] = res_item.get("working", False)

        newly_working = []
        newly_broken = []

        all_keys = set(prev_map.keys()) | set(curr_map.keys())
        for key in sorted(all_keys):
            prov, model, cap = key
            prev_status = prev_map.get(key)
            curr_status = curr_map.get(key)

            if prev_status is False and curr_status is True:
                newly_working.append(f"- **{prov}** / `{model}` ({cap})")
            elif prev_status is True and curr_status is False:
                newly_broken.append(f"- **{prov}** / `{model}` ({cap})")

        lines.append("## Newly Working ✅")
        if newly_working:
            lines.extend(newly_working)
        else:
            lines.append("_No newly working capabilities since last run._")

        lines.append("")
        lines.append("## Newly Broken ❌")
        if newly_broken:
            lines.extend(newly_broken)
        else:
            lines.append("_No working models broke since last run._")

        (self.reports_dir / "changes.md").write_text("\n".join(lines) + "\n", encoding="utf-8")