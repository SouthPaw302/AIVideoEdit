#!/usr/bin/env python3
"""Agent-harness read model for AIVideoEdit Studio.

This module deliberately adds only read-oriented orchestration helpers.
Production mutations continue to flow through the existing provider-neutral
Tool API and its canonical AIVideoEdit guards.
"""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import server as base
import production_project
from core_adapter import CORE

SCHEMAS = [
    {
        "name": "harness.status",
        "description": "Show whether the optional agent-harness bridge is available without changing production state.",
        "input_schema": {"type": "object", "properties": {}},
    },
    {
        "name": "harness.context",
        "description": "Return a compact authoritative project/branch/stage/director snapshot for an agent before it acts.",
        "input_schema": {
            "type": "object",
            "required": ["project_id"],
            "properties": {"project_id": {"type": "string"}},
        },
    },
]


def schemas():
    return SCHEMAS


def _read_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def status() -> dict:
    dsh = shutil.which("dsh")
    npx = shutil.which("npx")
    return {
        "schema": "aivideoedit.harness-status.v1",
        "ok": True,
        "bridge": "mcp-stdio",
        "bridge_ready": True,
        "deepseek_harness_detected": bool(dsh or npx),
        "launcher": dsh or npx,
        "canonical_core": CORE.status(),
        "policy": {
            "production_authority": "canonical-aivideoedit-core",
            "main_mutation": False,
            "guard_bypass": False,
            "project_context_required": True,
        },
    }


def context(project_id: str) -> dict:
    pid = str(project_id or "").strip()
    project = base.find_project(pid)
    if not project:
        raise ValueError("project not found")

    production = production_project.status(pid)
    project_dir_text = production.get("project_dir") or ""
    project_dir = Path(project_dir_text) if project_dir_text else None
    order = _read_json(project_dir / "OPERATING_ORDER.json", {}) if project_dir and project_dir.is_dir() else {}
    state = _read_json(project_dir / "PROJECT_STATE.json", {}) if project_dir and project_dir.is_dir() else {}

    with base.LOCK:
        assets = [
            {
                "id": a.get("id"),
                "filename": a.get("filename"),
                "status": a.get("status"),
                "sha256": a.get("sha256"),
                "qc": (a.get("qc") or {}).get("status"),
                "origin": a.get("origin"),
            }
            for a in base.STATE["assets"]
            if a.get("project") == pid
        ]
        active_jobs = [
            {
                "id": j.get("id"),
                "type": j.get("type"),
                "status": j.get("status"),
                "progress": j.get("progress"),
                "result": j.get("result"),
            }
            for j in base.STATE["jobs"]
            if j.get("project") == pid and j.get("status") in {"queued", "running"}
        ]

    return {
        "schema": "aivideoedit.harness-context.v1",
        "project": {
            "id": project.get("id"),
            "name": project.get("name"),
        },
        "production": {
            "initialized": bool(production.get("initialized")),
            "branch": production.get("branch"),
            "stage": production.get("stage"),
            "next_stage": production.get("next_stage"),
            "guard_pass": bool(production.get("guard_pass")),
            "main_commit": (production.get("core") or {}).get("main_commit") or CORE.status().get("main_commit"),
        },
        "director": {
            "director_brain_version": state.get("director_brain_version"),
            "mission": order.get("mission"),
            "direction_authority": order.get("direction_authority"),
            "production_mode": order.get("production_mode"),
            "current_user_direction": order.get("current_user_direction"),
            "exact_next_action": order.get("exact_next_action"),
            "canon_lock": order.get("canon_lock"),
            "accepted_baseline": order.get("accepted_baseline"),
            "accepted_source_library": order.get("accepted_source_library"),
            "refinement_scope": order.get("refinement_scope"),
            "recut_scope": order.get("recut_scope"),
        },
        "assets": {
            "count": len(assets),
            "ready": sum(1 for a in assets if a.get("status") == "ready"),
            "items": assets,
        },
        "active_jobs": active_jobs,
        "agent_rules": [
            "Treat the current project branch and current explicit user instruction as project authority.",
            "Run through existing AIVideoEdit tools; do not bypass canonical production guards.",
            "Do not mutate main from the harness experiment.",
            "Refresh harness.context after a stage-changing operation before choosing the next action.",
        ],
    }


def call(name: str, args: dict | None = None):
    args = args or {}
    if name == "harness.status":
        return status()
    if name == "harness.context":
        return context(str(args.get("project_id") or ""))
    raise ValueError(f"unknown harness tool: {name}")
