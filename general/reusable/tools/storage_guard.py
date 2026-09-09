#!/usr/bin/env python3
from pathlib import Path
import sys

BLOCKED = ("actions/upload-artifact", "actions/cache")
violations = []
for p in Path('.github/workflows').glob('*.y*ml'):
    text = p.read_text(encoding='utf-8')
    for token in BLOCKED:
        if token in text:
            violations.append(f"{p}: forbidden Actions storage directive: {token}")

if violations:
    print("\n".join(violations), file=sys.stderr)
    raise SystemExit(1)
print("PASS: workflows use zero GitHub Actions artifact/cache storage")
