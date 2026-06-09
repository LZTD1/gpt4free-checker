from __future__ import annotations
import argparse
import os
from .config import CONFIG, Config

def parse_args() -> Config:
    parser = argparse.ArgumentParser(
        description="gpt4free test runner engine for validating active providers"
    )

    parser.add_argument(
        "--concurrency",
        type=int,
        default=int(os.getenv("TEST_CONCURRENCY", CONFIG.max_concurrent)),
        help="Max simultaneous providers tested in parallel"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=int(os.getenv("TEST_TIMEOUT", CONFIG.request_timeout)),
        help="Timeout limit for each individual request execution"
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=int(os.getenv("TEST_RETRIES", CONFIG.retries_count)),
        help="Retries on standard connection or rate errors"
    )
    parser.add_argument(
        "--inter-model-pause",
        type=float,
        default=float(os.getenv("TEST_INTER_MODEL_PAUSE", CONFIG.inter_model_pause)),
        help="Base pause (seconds) between sequential model tests within one provider (anti-429)"
    )
    parser.add_argument(
        "--inter-model-pause-jitter",
        type=float,
        default=float(os.getenv("TEST_INTER_MODEL_PAUSE_JITTER", CONFIG.inter_model_pause_jitter)),
        help="Max random extra seconds added on top of --inter-model-pause to desync parallel providers"
    )
    parser.add_argument(
        "--capabilities",
        type=str,
        help="Comma-separated capabilities filter (text, image, audio, video)"
    )
    parser.add_argument(
        "--providers",
        type=str,
        help="Comma-separated list of providers names to limit runs"
    )
    parser.add_argument(
        "--include-auth",
        action="store_true",
        default=os.getenv("TEST_INCLUDE_AUTH", "false").lower() == "true",
        help="Incorporate auth-requiring providers into execution suite"
    )
    parser.add_argument(
        "--reports-dir",
        type=str,
        default=os.getenv("TEST_REPORTS_DIR", CONFIG.reports_dir),
        help="Target folder destination for files output"
    )
    parser.add_argument(
        "--prev-summary",
        type=str,
        default=os.getenv("TEST_PREV_SUMMARY", ""),
        help="Absolute path to previous run summary.json for diffing engine calculations"
    )

    args = parser.parse_args()

    caps = []
    if args.capabilities:
        caps = [c.strip().lower() for c in args.capabilities.split(",") if c.strip()]

    provs = []
    if args.providers:
        provs = [p.strip() for p in args.providers.split(",") if p.strip()]

    return Config(
        max_concurrent=args.concurrency,
        request_timeout=args.timeout,
        retries_count=args.retries,
        inter_model_pause=args.inter_model_pause,
        inter_model_pause_jitter=args.inter_model_pause_jitter,
        filter_capabilities=caps,
        filter_providers=provs,
        include_auth=args.include_auth,
        reports_dir=args.reports_dir,
        previous_summary_path=args.prev_summary if args.prev_summary else None
    )