from __future__ import annotations
import re
from dataclasses import dataclass

GARBAGE_PATTERNS = [
    re.compile(r"important\s+notice", re.IGNORECASE),
    re.compile(r"is being deprecated", re.IGNORECASE),
    re.compile(r"\bdeprecated\b.*\bapi\b", re.IGNORECASE),
    re.compile(r"please (use|switch|migrate)", re.IGNORECASE),
    re.compile(r"rate[- ]?limit(ed)?", re.IGNORECASE),
    re.compile(r"api key (is )?(required|missing|invalid)", re.IGNORECASE),
    re.compile(r"unauthor[iz]ed", re.IGNORECASE),
    re.compile(r"cloudflare", re.IGNORECASE),
    re.compile(r"<html", re.IGNORECASE),
    re.compile(r"403 forbidden", re.IGNORECASE),
]


@dataclass
class ValidationOutcome:
    valid: bool
    note: str


def validate_text_ping_response(text: str, expected_token: str) -> ValidationOutcome:
    if not text or not text.strip():
        return ValidationOutcome(False, "empty body")

    stripped = text.strip()
    if len(stripped) < 2:
        return ValidationOutcome(False, "response too short")

    for pat in GARBAGE_PATTERNS:
        if pat.search(stripped):
            return ValidationOutcome(False, f"garbage pattern matched: {pat.pattern!r}")

    if expected_token.lower() in stripped.lower():
        return ValidationOutcome(True, f"contains expected token '{expected_token}'")
        
    return ValidationOutcome(
        False,
        f"expected '{expected_token}', got: {stripped[:80]!r}",
    )


def validate_text_loose(text: str) -> ValidationOutcome:
    if not text or not text.strip():
        return ValidationOutcome(False, "empty body")

    stripped = text.strip()
    if len(stripped) < 10:
        return ValidationOutcome(False, "response too short")

    for pat in GARBAGE_PATTERNS:
        if pat.search(stripped):
            return ValidationOutcome(False, f"garbage pattern matched: {pat.pattern!r}")

    return ValidationOutcome(True, "non-empty loose validation pass")


def validate_binary_media(data: bytes, min_size: int = 256) -> ValidationOutcome:
    if not data:
        return ValidationOutcome(False, "empty binary")
    if len(data) < min_size:
        return ValidationOutcome(False, f"too small: {len(data)}b")
        
    sigs = {
        b"\xff\xd8\xff": "jpeg",
        b"\x89PNG": "png",
        b"GIF8": "gif",
        b"RIFF": "wav/webp",
        b"ID3": "mp3",
        b"OggS": "ogg",
    }
    head = data[:8]
    for sig, name in sigs.items():
        if head.startswith(sig):
            return ValidationOutcome(True, f"signature: {name}")
            
    if len(data) >= 8 and data[4:8] == b"ftyp":
        return ValidationOutcome(True, "signature: mp4")
        
    return ValidationOutcome(True, "binary payload validation pass with unknown signature")