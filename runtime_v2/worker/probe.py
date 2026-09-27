"""Harmless built-in diagnostic executed by the allowlisted worker."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import platform
import sys


def main() -> int:
    payload = {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": sys.platform,
        "workspace": Path.cwd().name,
    }
    raw = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    Path("probe.json").write_text(raw, encoding="utf-8")
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    print(json.dumps({"status": "ok", "artifact": "probe.json", "sha256": digest}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
