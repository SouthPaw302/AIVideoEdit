#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
GUARD = HERE / "workflow_guard.py"
REGISTRY = ROOT / "general/reusable/STANDARD_WORKFLOW_REGISTRY.json"


def load_guard():
    spec = importlib.util.spec_from_file_location("aivideoedit_workflow_guard_test", GUARD)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {GUARD}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_optional_runtime_cannot_become_workflow_authority():
    mod = load_guard()
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert mod.validate_optional_runtime_boundary(registry) == []

    poisoned = json.loads(json.dumps(registry))
    poisoned["workflows"][0]["implementation"]["backend_options"].append("render_runtime")
    errors = mod.validate_optional_runtime_boundary(poisoned)
    assert errors
    assert "forbidden in STANDARD_WORKFLOW_REGISTRY" in errors[0]


def test_existing_aivideoedit_defaults_remain_mandatory():
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    default_ids = {
        wf["id"]
        for wf in registry.get("workflows", [])
        if isinstance(wf, dict) and wf.get("select_if", {}).get("default") is True
    }
    required = {"WF-PROJECT-STATE", "WF-RENDER-DELIVERY", "WF-MACHINE-QC", "WF-CACHE-INVALIDATION"}
    assert required.issubset(default_ids)


if __name__ == "__main__":
    test_optional_runtime_cannot_become_workflow_authority()
    test_existing_aivideoedit_defaults_remain_mandatory()
    print("workflow authority regression: PASS")
