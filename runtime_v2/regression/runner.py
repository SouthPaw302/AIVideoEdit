from __future__ import annotations

import hashlib
import json
from typing import Any


def stable_json_sha256(value: dict[str, Any]) -> str:
    raw = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def compare_golden(
    actual: dict[str, Any],
    expected: dict[str, Any],
    *,
    ignored_keys: set[str] | None = None,
) -> dict[str, Any]:
    ignored = ignored_keys or set()
    a = {k: v for k, v in actual.items() if k not in ignored}
    e = {k: v for k, v in expected.items() if k not in ignored}
    return {
        "pass": a == e,
        "actual_sha256": stable_json_sha256(a),
        "expected_sha256": stable_json_sha256(e),
    }
