from __future__ import annotations
import json
from pathlib import Path

class BadgeReporter:
    def __init__(self, reports_dir: Path):
        self.reports_dir = reports_dir

    def write(self, summary: dict) -> None:
        working_text = summary.get("by_capability", {}).get("text", 0)
        working_image = summary.get("by_capability", {}).get("image", 0)

        badge_data = {
            "schemaVersion": 1,
            "label": "models online",
            "message": f"text: {working_text} | image: {working_image}",
            "color": "green" if (working_text + working_image) > 0 else "red"
        }
        
        (self.reports_dir / "badge.json").write_text(
            json.dumps(badge_data, indent=2, ensure_ascii=False), encoding="utf-8"
        )