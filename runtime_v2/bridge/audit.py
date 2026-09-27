"""Append-only JSONL audit records for bridge requests."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import datetime, timezone
import json
import logging
from pathlib import Path


LOGGER = logging.getLogger("runtime_v2.bridge.audit")


@dataclass(frozen=True)
class AuditRecord:
    timestamp: str
    request_id: str
    method: str
    path: str
    status_code: int
    duration_ms: float


def build_record(
    *,
    request_id: str,
    method: str,
    path: str,
    status_code: int,
    duration_ms: float,
) -> AuditRecord:
    return AuditRecord(
        timestamp=datetime.now(timezone.utc).isoformat(),
        request_id=request_id,
        method=method,
        path=path,
        status_code=status_code,
        duration_ms=round(duration_ms, 3),
    )


def write_record(record: AuditRecord, path: str | None) -> None:
    payload = json.dumps(asdict(record), separators=(",", ":"), sort_keys=True)
    LOGGER.info(payload)

    if not path:
        return

    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("a", encoding="utf-8") as handle:
        handle.write(payload + "\n")
