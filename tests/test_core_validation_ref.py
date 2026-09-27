from __future__ import annotations

import importlib.util
from pathlib import Path


def load_core_adapter():
    path=Path("prototype/backend_gui/core_adapter.py")
    spec=importlib.util.spec_from_file_location("core_adapter_validation_test",path)
    mod=importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


def test_core_ref_defaults_to_main(monkeypatch):
    monkeypatch.delenv("AIVE_CORE_REF",raising=False)
    mod=load_core_adapter()
    assert mod._core_ref()=="main"


def test_core_ref_can_be_overridden_for_validation(monkeypatch):
    monkeypatch.setenv("AIVE_CORE_REF","MainV2-clean")
    mod=load_core_adapter()
    assert mod._core_ref()=="MainV2-clean"
