from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.skipif(shutil.which("git") is None, reason="git required for offline bootstrap fixture")
def test_offline_boot_capsule_fixture(tmp_path: Path):
    source_repo = Path(__file__).resolve().parents[2]
    fixture = tmp_path / "fixture"
    (fixture / "general/reusable/tools").mkdir(parents=True)
    (fixture / "general/reusable").mkdir(parents=True, exist_ok=True)
    (fixture / "runtime_v2/boot").mkdir(parents=True)

    for rel in (
        "bootstrap.py",
        "runtime_v2/__init__.py",
        "runtime_v2/boot/capsule.py",
        "runtime_v2/models/__init__.py",
        "runtime_v2/models/registry.py",
        "runtime_v2/models/registry.json",
    ):
        src = source_repo / rel
        dst = fixture / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())

    (fixture / "README.md").write_text("fixture\n", encoding="utf-8")
    manifest = {
        "schema": "fixture",
        "files": [
            {"path": "PRIME_DIRECTIVE.md"},
            {"path": "general/reusable/PRODUCTION_CONTRACT.json"}
        ]
    }
    (fixture / "PRIME_DIRECTIVE.md").write_text("fixture directive\n", encoding="utf-8")
    (fixture / "general/reusable/AIVIDEOEDIT_OS_MANIFEST.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    (fixture / "general/reusable/PRODUCTION_CONTRACT.json").write_text(
        json.dumps({"states": ["INITIALIZED"]}), encoding="utf-8"
    )
    for name in ("production_guard.py", "recut_guard.py", "workflow_guard.py"):
        (fixture / "general/reusable/tools" / name).write_text(
            "raise SystemExit(0)\n", encoding="utf-8"
        )

    subprocess.run(["git", "init"], cwd=fixture, check=True, stdout=subprocess.PIPE)
    subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=fixture, check=True)
    subprocess.run(["git", "config", "user.name", "Fixture"], cwd=fixture, check=True)
    subprocess.run(["git", "add", "."], cwd=fixture, check=True)
    subprocess.run(["git", "commit", "-m", "fixture"], cwd=fixture, check=True, stdout=subprocess.PIPE)
    subprocess.run(["git", "branch", "-M", "MainV2"], cwd=fixture, check=True)

    p = subprocess.run(
        [
            sys.executable,
            str(source_repo / "bootstrap.py"),
            "boot",
            "--repo-root",
            str(fixture),
            "--branch",
            "MainV2",
            "--authority-ref",
            "MainV2",
            "--offline",
        ],
        cwd=source_repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    assert p.returncode == 0, p.stderr + "\n" + p.stdout
    assert "AIVideoEdit OS BOOTSTRAP: PASS" in p.stdout
    capsule = json.loads((fixture / ".aivideoedit/boot_capsule.json").read_text(encoding="utf-8"))
    attestation = json.loads((fixture / ".aivideoedit/session_attestation.json").read_text(encoding="utf-8"))
    assert capsule["authority"]["ref"] == "MainV2"
    assert capsule["active"]["branch"] == "MainV2"
    assert capsule["active"]["next_contract_stage"] == "INITIALIZED"
    assert attestation["session_id"] == capsule["session_id"]
    model = capsule["models"]["music_and_beat_analysis"]
    assert model["available"] is True
    assert model["resolved"] == "music.beat.micro-dsp.v1"
