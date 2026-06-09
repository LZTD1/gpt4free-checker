from __future__ import annotations
import asyncio
import logging
import shutil
import sys
import time
from pathlib import Path
import warnings

warnings.filterwarnings("ignore", category=ResourceWarning)
try:
    import colorama
    colorama.init()
except ImportError:
    pass

from g4f.client import AsyncClient

from .config import CONFIG
from .cli import parse_args
from .discovery import Discovery
from .models import Status
from .reporter import Reporter
from .tester import Tester

log = logging.getLogger("provider_tester")


class ColoredFormatter(logging.Formatter):
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GRAY = "\033[90m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    LEVEL_COLORS = {
        logging.DEBUG: GRAY,
        logging.INFO: WHITE,
        logging.WARNING: YELLOW,
        logging.ERROR: RED,
        logging.CRITICAL: RED + BOLD,
    }

    def format(self, record: logging.LogRecord) -> str:
        asctime = self.formatTime(record, "%H:%M:%S")
        level_color = self.LEVEL_COLORS.get(record.levelno, self.RESET)
        level_name = f"{level_color}{record.levelname:<7}{self.RESET}"
        logger_name = f"{self.CYAN}{record.name}{self.RESET}"
        message = record.getMessage()

        if "OK" in message or "✅" in message:
            message = f"{self.GREEN}{message}{self.RESET}"
        elif "❌" in message:
            message = f"{self.RED}{message}{self.RESET}"
        elif "skipping" in message or "skipped" in message:
            message = f"{self.GRAY}{message}{self.RESET}"
        elif record.levelno == logging.WARNING:
            message = f"{self.YELLOW}{message}{self.RESET}"
        elif record.levelno >= logging.ERROR:
            message = f"{self.RED}{message}{self.RESET}"

        formatted = f"{self.GRAY}{asctime}{self.RESET} [{level_name}] {logger_name}: {message}"

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
            if record.exc_text:
                formatted += f"\n{self.RED}{record.exc_text}{self.RESET}"
        if record.stack_info:
            formatted += f"\n{self.formatStack(record.stack_info)}"

        return formatted


def _setup_logging() -> None:
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(ColoredFormatter())

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers = [handler]

    for noisy in (
        "urllib3", "asyncio", "aiohttp", "requests", "g4f",
        "uvicorn", "fastapi", "starlette", "h11", "httpcore"
    ):
        l = logging.getLogger(noisy)
        l.setLevel(logging.WARNING)
        l.propagate = False


async def _run(active_config) -> int:
    log.info("Initializing g4f async client...")
    client = AsyncClient()
    tester = Tester(client, max_concurrent=active_config.max_concurrent)

    log.info("Discovering metadata matching active providers...")
    reports = Discovery.get_providers()
    total_models = sum(r.model_count for r in reports)
    log.info(
        "Discovered %d provider configs, %d models matching filters",
        len(reports), total_models,
    )
    log.info(
        "Strategy: %d providers in parallel, models sequential inside each (pause=%.1fs)",
        active_config.max_concurrent, active_config.inter_model_pause,
    )

    progress = {"done": 0, "ok": 0, "rate_limited": 0}

    def on_result(res):
        progress["done"] += 1
        if res.status.value == "rate_limited":
            progress["rate_limited"] += 1
        if res.status == Status.OK:
            progress["ok"] += 1
            log.info(
                "✅ [%d/%d OK] '%s' -> '%s' (%s) %.2fs",
                progress["ok"], progress["done"],
                res.provider, res.model, res.capability.value, res.response_time,
            )
        else:
            err_msg = res.error or "unknown error"
            log.info(
                "❌ [%d/%d OK] '%s' -> '%s' (%s) %s — %s (%.2fs)",
                progress["ok"], progress["done"],
                res.provider, res.model, res.capability.value,
                res.status.value, err_msg, res.response_time,
            )

    log.info("Starting parallel execution (providers=%d concurrently)...", active_config.max_concurrent)
    t0 = time.monotonic()

    # Все провайдеры запускаются одновременно — семафор внутри Tester
    # ограничивает фактический параллелизм до max_concurrent
    async def run_one(i: int, report) -> None:
        if report.model_count == 0:
            log.info(
                "[%d/%d] Provider '%s' — no models matching filters, skipping",
                i, len(reports), report.name,
            )
            return
        log.info(
            "[%d/%d] Queued provider '%s' (%d models)...",
            i, len(reports), report.name, report.model_count,
        )
        try:
            await tester.test_provider(report, progress_cb=on_result)
        except Exception as exc:
            log.exception(
                "Structural failure during testing of provider %s: %s",
                report.name, exc,
            )
            report.fetch_error = f"{type(exc).__name__}: {exc}"

    await asyncio.gather(*(run_one(i, r) for i, r in enumerate(reports, 1)))

    elapsed = time.monotonic() - t0
    log.info("Execution finished in %.1fs", elapsed)
    if progress["rate_limited"]:
        log.info("Rate-limited responses: %d (%.1f%%)", progress["rate_limited"],
                 100 * progress["rate_limited"] / max(progress["done"], 1))

    target_reports_dir = Path(active_config.reports_dir)
    temp_reports_dir = target_reports_dir.parent / f"{target_reports_dir.name}.tmp"

    if temp_reports_dir.exists():
        shutil.rmtree(temp_reports_dir)
    temp_reports_dir.mkdir(parents=True, exist_ok=True)

    log.info("Writing reports to temporary dir: %s/", temp_reports_dir)
    reporter = Reporter(str(temp_reports_dir))
    summary = reporter.write_all(reports, previous_summary_path=active_config.previous_summary_path)

    try:
        if target_reports_dir.exists():
            shutil.rmtree(target_reports_dir)
        temp_reports_dir.rename(target_reports_dir)
        log.info("Reports swapped to: %s/", target_reports_dir)
    except Exception as e:
        log.error("Failed atomic replacement of reports directory: %s", e)
        return 1

    log.info("==== SUMMARY ====")
    log.info("Providers working: %d/%d", summary["providers_working"], summary["providers_total"])
    log.info(
        "Success rate: %d/%d (%.2f%%)",
        summary["tests_ok"], summary["tests_total"], summary["success_rate_pct"],
    )
    log.info("By status: %s", summary["by_status"])
    return 0


def main() -> int:
    _setup_logging()

    try:
        active_config = parse_args()
    except Exception as e:
        log.error("Failed parsing configuration arguments: %s", e)
        return 1

    try:
        return asyncio.run(_run(active_config))
    except KeyboardInterrupt:
        log.warning("Execution interrupted by user")
        return 130
    except Exception:
        log.exception("Fatal runner crash")
        return 1


if __name__ == "__main__":
    sys.exit(main())