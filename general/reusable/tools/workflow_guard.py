#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path

from branch_policy import resolve_production_project

SCRIPT_ROOT = Path(__file__).resolve().parents[3]
if os.environ.get("AIVIDEOEDIT_REPO_ROOT"):
    ROOT = Path(os.environ["AIVIDEOEDIT_REPO_ROOT"]).resolve()
elif SCRIPT_ROOT.name == "os" and SCRIPT_ROOT.parent.name == ".aivideoedit":
    ROOT = SCRIPT_ROOT.parent.parent.resolve()
else:
    ROOT = SCRIPT_ROOT.resolve()

if os.environ.get("AIVIDEOEDIT_OS_ROOT"):
    OS_ROOT = Path(os.environ["AIVIDEOEDIT_OS_ROOT"]).resolve()
elif SCRIPT_ROOT.name == "os" and SCRIPT_ROOT.parent.name == ".aivideoedit":
    OS_ROOT = SCRIPT_ROOT.resolve()
else:
    OS_ROOT = ROOT

REGISTRY = OS_ROOT / "general/reusable/STANDARD_WORKFLOW_REGISTRY.json"
RESOLVER = OS_ROOT / "general/reusable/tools/workflow_resolver.py"
MEDIA = OS_ROOT / "general/reusable/MEDIA_CAPABILITY_MATRIX.json"


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("aivideoedit_workflow_resolver_guard", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(branch: str):
    errors = []
    if not REGISTRY.is_file():
        return [f"missing standard workflow registry: {REGISTRY}"]
    if not RESOLVER.is_file():
        return [f"missing standard workflow resolver: {RESOLVER}"]
    mod = load_module(RESOLVER)
    registry = load_json(REGISTRY)
    media = load_json(MEDIA) if MEDIA.is_file() else None
    errors.extend(mod.validate_registry(registry, media))
    errors.extend(mod.regression_scenarios(registry))
    if errors or branch == "main":
        return errors

    project, branch_error = resolve_production_project(ROOT, branch)
    if branch_error:
        return [branch_error]
    if project is None:
        return [f"production project could not be resolved for {branch}"]
    try:
        resolved = mod.resolve_project(project, registry)
    except Exception as exc:
        return [f"standard workflow selection failed: {exc}"]
    selected = resolved.get("selected_workflows", [])
    mandatory = {"WF-PROJECT-STATE", "WF-RENDER-DELIVERY", "WF-MACHINE-QC", "WF-CACHE-INVALIDATION"}
    missing = mandatory - set(selected)
    if missing:
        errors.append("standard workflow selection missing mandatory defaults: " + ", ".join(sorted(missing)))
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--branch", default=os.environ.get("GITHUB_REF_NAME") or os.environ.get("AIVIDEOEDIT_BRANCH") or "")
    args = ap.parse_args()
    if not args.branch:
        print("AIVideoEdit standard workflow contract: FAIL\n- branch required")
        return 2
    errors = validate(args.branch)
    if errors:
        print("AIVideoEdit standard workflow contract: FAIL")
        for e in errors:
            print("- " + e)
        return 2
    print("AIVideoEdit standard workflow contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
