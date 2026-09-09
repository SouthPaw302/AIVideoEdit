#!/usr/bin/env python3
"""Bridge browser projects into isolated canonical AIVideoEdit production repos.

Each workstation project gets its own local checkout and `song/<slug>` branch.
The compatibility scaffold only creates the minimum INITIALIZED project files;
the current-main production guard remains the authority for validity and all
later stage advancement.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import server as base
from core_adapter import CORE


def _run(cmd: list[str], cwd: Path, timeout: int = 300) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout, check=False)


def _engine_root(project_id: str) -> Path:
    return base.PROJECT_ROOT / project_id / "engine"


def _song_slug(project_id: str) -> str:
    return base.slugify(project_id)


def _branch(project_id: str) -> str:
    return f"song/{_song_slug(project_id)}"


def _canonical_project_dir(engine: Path, project_id: str) -> Path:
    return engine / "projects" / _song_slug(project_id)


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _scaffold(project_id: str, name: str, engine: Path) -> Path:
    project_dir = _canonical_project_dir(engine, project_id)
    project_dir.mkdir(parents=True, exist_ok=True)
    branch = _branch(project_id)
    contract = CORE.production_contract()
    denied = contract.get("default_denied_sources", [])

    text_files = {
        "PROJECT.md": f"# {name}\n\nAIVideoEdit production workspace.\n",
        "STATUS.md": "# Status\n\nStage: INITIALIZED\n",
        "HANDOFF.md": "# Handoff\n\nProduction initialized; no creative direction is implied by this scaffold.\n",
        "SCRIPT.md": "# Script\n\nNot locked.\n",
        "VISUAL_DNA.md": "# Visual DNA\n\nNot established.\n",
        "SHOT_LIST.md": "# Shot List\n\nNot established.\n",
        "RENDER_HISTORY.md": "# Render History\n\nNo accepted renders.\n",
        "QC.md": "# QC\n\nNo final QC has been performed.\n",
    }
    for filename, content in text_files.items():
        (project_dir / filename).write_text(content, encoding="utf-8")

    _write_json(project_dir / "PROJECT_STATE.json", {
        "schema": "aivideoedit.project-state.v1",
        "branch": branch,
        "stage": "INITIALIZED",
        "source_ingest_complete": False,
        "reference_analysis_complete": False,
        "music_analysis_complete": False,
        "lyrics_status_resolved": False,
        "genre_authority_resolved": False,
        "visual_approach_established": False,
        "storyboard_locked": False,
        "script_locked": False,
        "shot_packages_built": False,
        "shot_proofs_accepted": False,
        "fx_lock_verified": False,
        "assembly_complete": False,
        "final_qc_passed": False,
        "archive_complete": False,
    })
    _write_json(project_dir / "SOURCE_AUTHORITY.json", {
        "schema": "aivideoedit.source-authority.v1",
        "allow": {key: False for key in denied},
        "explicit_user_authorizations": [],
    })
    _write_json(project_dir / "REFERENCE_MANIFEST.json", {"videos": [], "images": []})
    _write_json(project_dir / "MEDIA_PLAN.json", {"selected_capabilities": [], "user_approach_established": False})
    _write_json(project_dir / "ASSET_MANIFEST.json", {"assets": []})
    _write_json(project_dir / "MUSIC_ANALYSIS.json", {})
    _write_json(project_dir / "SCRIPT.json", {"entries": []})
    return project_dir


def initialize(project_id: str) -> dict:
    project = base.find_project(project_id)
    if not project:
        raise ValueError("project not found")
    if not CORE.status().get("bootstrapped"):
        raise RuntimeError("canonical core is not loaded")

    engine = _engine_root(project_id)
    if engine.exists():
        return status(project_id)
    engine.parent.mkdir(parents=True, exist_ok=True)

    proc = _run(["git", "clone", "--no-hardlinks", str(CORE.core_repo), str(engine)], CORE.core_repo)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout or "local core clone failed")[-1200:])

    branch = _branch(project_id)
    checkout = _run(["git", "checkout", "-b", branch, "main"], engine, timeout=60)
    if checkout.returncode != 0:
        checkout = _run(["git", "checkout", "-b", branch, "origin/main"], engine, timeout=60)
    if checkout.returncode != 0:
        shutil.rmtree(engine, ignore_errors=True)
        raise RuntimeError((checkout.stderr or checkout.stdout or "song branch creation failed")[-1200:])

    project_dir = _scaffold(project_id, project.get("name") or project_id, engine)
    _run(["git", "config", "user.name", "AIVideoEdit Workstation"], engine, timeout=20)
    _run(["git", "config", "user.email", "workstation@aivideoedit.local"], engine, timeout=20)
    _run(["git", "add", f"projects/{project_dir.name}"], engine, timeout=30)
    commit = _run(["git", "commit", "-m", "Initialize AIVideoEdit production workspace"], engine, timeout=60)
    if commit.returncode != 0:
        raise RuntimeError((commit.stderr or commit.stdout or "initial project commit failed")[-1200:])

    boot = _run([
        sys.executable, str(engine / "bootstrap.py"), "boot",
        "--repo-root", str(engine),
        "--branch", branch,
        "--project-dir", f"projects/{project_dir.name}",
    ], engine, timeout=300)
    if boot.returncode != 0:
        return {
            "ok": False,
            "initialized": True,
            "guard_pass": False,
            "branch": branch,
            "engine_root": str(engine),
            "project_dir": str(project_dir),
            "stdout": (boot.stdout or "")[-4000:],
            "stderr": (boot.stderr or "")[-4000:],
        }
    return status(project_id)


def status(project_id: str) -> dict:
    project = base.find_project(project_id)
    if not project:
        raise ValueError("project not found")
    engine = _engine_root(project_id)
    project_dir = _canonical_project_dir(engine, project_id)
    session_path = engine / ".aivideoedit" / "session.json"
    state_path = project_dir / "PROJECT_STATE.json"
    session = {}
    state = {}
    try:
        session = json.loads(session_path.read_text(encoding="utf-8"))
    except Exception:
        pass
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception:
        pass
    return {
        "ok": True,
        "initialized": engine.is_dir() and project_dir.is_dir(),
        "guard_pass": session.get("guard_result") == "PASS" and session.get("branch") == _branch(project_id),
        "branch": _branch(project_id),
        "stage": state.get("stage"),
        "engine_root": str(engine) if engine.is_dir() else None,
        "project_dir": str(project_dir) if project_dir.is_dir() else None,
        "main_commit": session.get("os_main_commit"),
        "session_id": session.get("session_id"),
    }


def run_guard(project_id: str) -> dict:
    current = status(project_id)
    if not current.get("initialized"):
        raise RuntimeError("production workspace is not initialized")
    engine = Path(current["engine_root"])
    session = engine / ".aivideoedit" / "session.json"
    try:
        rec = json.loads(session.read_text(encoding="utf-8"))
    except Exception:
        raise RuntimeError("production bootstrap session is missing")
    os_root = Path(rec.get("os_root") or "")
    guard = os_root / "general/reusable/tools/production_guard.py"
    if not guard.is_file():
        raise RuntimeError("bootstrapped production guard is missing")
    env = dict(os.environ)
    env["AIVIDEOEDIT_REPO_ROOT"] = str(engine)
    env["AIVIDEOEDIT_OS_ROOT"] = str(os_root)
    env["AIVIDEOEDIT_PROJECT_DIR"] = f"projects/{_song_slug(project_id)}"
    proc = subprocess.run(
        [sys.executable, str(guard), "--branch", _branch(project_id)],
        cwd=str(engine), env=env, capture_output=True, text=True, timeout=120, check=False,
    )
    latest = status(project_id)
    latest.update({
        "ok": proc.returncode == 0,
        "guard_pass": proc.returncode == 0,
        "stdout": (proc.stdout or "")[-4000:],
        "stderr": (proc.stderr or "")[-4000:],
    })
    return latest
