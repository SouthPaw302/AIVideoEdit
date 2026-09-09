#!/usr/bin/env python3
"""Adapter between the workstation stack and the canonical AIVideoEdit OS.

The adapter never copies production authority into the prototype. It asks the
repository bootstrap to materialize the exact current `main` OS under
`.aivideoedit/os/`, then reads contracts/capabilities/effects from that
attested snapshot.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
SESSION_ROOT = REPO_ROOT / ".aivideoedit"
OS_ROOT = SESSION_ROOT / "os"
SESSION_FILE = SESSION_ROOT / "session.json"
BOOTSTRAP = REPO_ROOT / "bootstrap.py"
CONTRACT = Path("general/reusable/PRODUCTION_CONTRACT.json")
CAPABILITY_MATRIX = Path("general/reusable/MEDIA_CAPABILITY_MATRIX.json")
FX_REGISTRY = Path("general/reusable/fx_v2/registry.json")


def _read_json(path: Path, default: Any) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _git_branch() -> str:
    explicit = os.environ.get("AIVIDEOEDIT_BRANCH")
    if explicit:
        return explicit
    try:
        proc = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "branch", "--show-current"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if proc.returncode == 0 and proc.stdout.strip():
            return proc.stdout.strip()
    except Exception:
        pass
    return "prototype/backend-gui"


class CoreAdapter:
    def __init__(self) -> None:
        self.repo_root = REPO_ROOT
        self.os_root = OS_ROOT
        self.session_file = SESSION_FILE

    def bootstrap(self, offline: bool = False) -> dict:
        if not BOOTSTRAP.is_file():
            return {"ok": False, "error": "bootstrap.py not found", "repo_root": str(REPO_ROOT)}
        cmd = [
            sys.executable,
            str(BOOTSTRAP),
            "boot",
            "--repo-root",
            str(REPO_ROOT),
            "--branch",
            _git_branch(),
        ]
        if offline:
            cmd.append("--offline")
        proc = subprocess.run(
            cmd,
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        result = {
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout": (proc.stdout or "")[-4000:],
            "stderr": (proc.stderr or "")[-4000:],
        }
        result.update(self.status())
        return result

    def status(self) -> dict:
        session = _read_json(self.session_file, {})
        contract = _read_json(self.os_root / CONTRACT, {}) if self.os_root.is_dir() else {}
        matrix = _read_json(self.os_root / CAPABILITY_MATRIX, {}) if self.os_root.is_dir() else {}
        fx = _read_json(self.os_root / FX_REGISTRY, {}) if self.os_root.is_dir() else {}
        capabilities = self._records(matrix, ("capabilities", "media_capabilities", "items"))
        effects = self._records(fx, ("effects", "fx", "registry", "items"))
        bootstrapped = bool(session) and self.os_root.is_dir()
        return {
            "ok": True,
            "bootstrapped": bootstrapped,
            "repo_root": str(self.repo_root),
            "branch": _git_branch(),
            "os_root": str(self.os_root) if bootstrapped else None,
            "main_commit": session.get("os_main_commit"),
            "session_id": session.get("session_id"),
            "guard_result": session.get("guard_result"),
            "contract_schema": contract.get("schema"),
            "production_states": contract.get("states", []),
            "capability_count": len(capabilities),
            "fx_count": len(effects),
        }

    @staticmethod
    def _records(payload: Any, keys: tuple[str, ...]) -> list:
        if isinstance(payload, list):
            return payload
        if isinstance(payload, dict):
            for key in keys:
                value = payload.get(key)
                if isinstance(value, list):
                    return value
                if isinstance(value, dict):
                    return [dict({"id": k}, **(v if isinstance(v, dict) else {"value": v})) for k, v in value.items()]
            # Some registries are keyed directly by capability/effect id.
            if payload and all(isinstance(k, str) for k in payload):
                records = []
                for key, value in payload.items():
                    if isinstance(value, dict):
                        records.append(dict({"id": key}, **value))
                if records:
                    return records
        return []

    def production_contract(self) -> dict:
        return _read_json(self.os_root / CONTRACT, {})

    def capabilities(self) -> list:
        payload = _read_json(self.os_root / CAPABILITY_MATRIX, {})
        return self._records(payload, ("capabilities", "media_capabilities", "items"))

    def effects(self) -> list:
        payload = _read_json(self.os_root / FX_REGISTRY, {})
        return self._records(payload, ("effects", "fx", "registry", "items"))


CORE = CoreAdapter()
