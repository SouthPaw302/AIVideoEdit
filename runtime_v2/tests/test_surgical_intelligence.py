from __future__ import annotations

import json
import math
import wave
from array import array
from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from runtime_v2.boot.capsule import (
    build_capsule,
    sign_capsule,
    verify_capsule,
)
from runtime_v2.gatekeeper import evaluate_action
from runtime_v2.harness.adapter import specialist_request
from runtime_v2.intelligence_api import router
from runtime_v2.jev.decision import decide
from runtime_v2.models.music_beat import analyze_music
from runtime_v2.models.registry import ModelRegistry
from runtime_v2.regression.runner import compare_golden


def _write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data),
        encoding="utf-8",
    )


def _fixture_repo(tmp_path: Path):
    repo = tmp_path / "repo"
    os_root = repo / ".aivideoedit" / "os"
    project = repo / "projects" / "fixture"
    for p in [
        os_root / "general/reusable/tools",
        os_root / "general/reusable/fx_v2",
        project,
    ]:
        p.mkdir(parents=True, exist_ok=True)

    _write_json(
        os_root / "general/reusable/PRODUCTION_CONTRACT.json",
        {"states": ["INITIALIZED", "SOURCE_INGESTED"]},
    )
    _write_json(
        project / "PROJECT_STATE.json",
        {"stage": "INITIALIZED"},
    )
    _write_json(
        project / "OPERATING_ORDER.json",
        {
            "exact_next_action": "ingest source audio",
            "direction_authority": "music_led",
            "production_mode": "hybrid",
            "canon_lock": {
                "locked": True,
                "items": ["hero-a"],
            },
            "refinement_scope": {
                "active": True,
                "allowed_changes": ["audio_sync"],
                "forbidden_changes": ["hero_identity"],
                "restart_authorized": False,
            },
            "recut_scope": {"active": False},
        },
    )
    _write_json(
        project / "REFERENCE_MANIFEST.json",
        {"videos": [], "images": []},
    )
    _write_json(
        project / "ASSET_MANIFEST.json",
        {"assets": []},
    )

    for rel in [
        "general/reusable/tools/production_guard.py",
        "general/reusable/tools/recut_guard.py",
        "general/reusable/tools/workflow_guard.py",
        "general/reusable/tools/branch_policy.py",
        "general/reusable/STANDARD_WORKFLOW_REGISTRY.json",
        "general/reusable/CANONICAL_EFFECT_REGISTRY.json",
        "general/reusable/fx_v2/registry.json",
        "general/reusable/fx_v2/recipes.json",
    ]:
        p = os_root / rel
        p.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
        p.write_text(
            "{}",
            encoding="utf-8",
        )
    return repo, os_root, project


def _click_wav(
    path: Path,
    bpm: float = 120.0,
    seconds: float = 6.0,
    rate: int = 16000,
):
    total = int(seconds * rate)
    data = array("h", [0]) * total
    period = int(rate * 60.0 / bpm)
    for start in range(
        0,
        total,
        period,
    ):
        for i in range(
            start,
            min(
                total,
                start + int(0.025 * rate),
            ),
        ):
            t = (i - start) / rate
            data[i] = int(
                22000
                * math.sin(
                    2 * math.pi * 1000 * t
                )
                * (1 - t / 0.025)
            )
    with wave.open(
        str(path),
        "wb",
    ) as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(data.tobytes())


def test_surgical_stack(
    tmp_path: Path,
    monkeypatch,
):
    repo, os_root, project = _fixture_repo(
        tmp_path
    )
    capsule = build_capsule(
        repo=repo,
        os_root=os_root,
        branch="song/fixture",
        project=project,
        authority_ref="MainV2",
        authority_commit="abc",
        session_id="s1",
    )
    att = sign_capsule(
        capsule,
        key="k",
    )
    assert verify_capsule(
        capsule,
        att,
        key="k",
    )[0]

    tampered = json.loads(
        json.dumps(capsule)
    )
    tampered["active"]["stage"] = (
        "SOURCE_INGESTED"
    )
    assert not verify_capsule(
        tampered,
        att,
        key="k",
    )[0]

    session = repo / ".aivideoedit"
    _write_json(
        session / "boot_capsule.json",
        capsule,
    )
    _write_json(
        session / "session_attestation.json",
        sign_capsule(capsule),
    )

    assert evaluate_action(
        repo=repo,
        action="sync",
        mutation=True,
        requested_changes=["audio_sync"],
        expected_stage="INITIALIZED",
        current_branch="song/fixture",
    ).decision == "PASS"

    assert evaluate_action(
        repo=repo,
        action="replace",
        mutation=True,
        protected_canon_replacement=True,
        current_branch="song/fixture",
    ).decision == "DENY"

    assert evaluate_action(
        repo=repo,
        action="sync",
        mutation=True,
        requested_changes=["hero_identity"],
        current_branch="song/fixture",
    ).decision == "DENY"

    assert evaluate_action(
        repo=repo,
        action="sync",
        mutation=True,
        current_branch="wrong",
    ).decision == "DENY"

    monkeypatch.delenv(
        "AIVIDEOEDIT_BEAT_ONNX_MODEL",
        raising=False,
    )
    registry = ModelRegistry.load_default()
    resolution = registry.resolve(
        "music.beat.onnx.v1"
    )
    assert resolution.used_fallback is True

    with pytest.raises(KeyError):
        registry.resolve(
            "unknown.model"
        )

    wav = tmp_path / "click.wav"
    _click_wav(wav)
    evidence = analyze_music(wav)
    assert evidence["engine"] == (
        "deterministic_dsp"
    )
    assert 112 <= evidence["bpm"] <= 128

    bounded = {
        "gate": "PASS",
        "checks": {"qc": True},
        "next_action_permitted": True,
    }
    assert decide(bounded) == decide(bounded)
    assert decide(bounded)["decision"] == (
        "CONTINUE"
    )
    assert decide(
        {"gate": "DENY"}
    )["decision"] == "FAIL"
    assert decide(
        {
            "gate": "PASS",
            "ambiguous": True,
        }
    )["decision"] == "ESCALATE"

    result = specialist_request(
        task="visual-qc",
        context={"frame": "fixture.png"},
        provider=lambda envelope: {
            "seen_task": envelope["task"]
        },
    )
    assert result["status"] == "PASS"
    assert result["request"]["authority"] == (
        "advisory_only"
    )

    assert compare_golden(
        {"decision": "PASS"},
        {"decision": "PASS"},
    )["pass"] is True


def test_intelligence_http_surface(
    tmp_path: Path,
    monkeypatch,
):
    repo, os_root, project = _fixture_repo(
        tmp_path
    )
    capsule = build_capsule(
        repo=repo,
        os_root=os_root,
        branch="song/fixture",
        project=project,
        authority_ref="MainV2",
        authority_commit="abc",
        session_id="s1",
    )
    _write_json(
        repo / ".aivideoedit/boot_capsule.json",
        capsule,
    )
    _write_json(
        repo
        / ".aivideoedit/session_attestation.json",
        sign_capsule(capsule),
    )
    monkeypatch.setenv(
        "AIVIDEOEDIT_REPO_ROOT",
        str(repo),
    )
    monkeypatch.delenv(
        "AIVIDEOEDIT_BEAT_ONNX_MODEL",
        raising=False,
    )

    wav = repo / "fixture.wav"
    _click_wav(wav)

    app = FastAPI()
    app.include_router(router)
    client = TestClient(app)

    assert client.get(
        "/intelligence/status"
    ).status_code == 200

    assert client.get(
        "/intelligence/models/resolve/music_and_beat_analysis"
    ).json()["available"] is True

    assert client.post(
        "/intelligence/gate",
        json={
            "action": "inspect",
            "mutation": False,
        },
    ).json()["decision"] == "PASS"

    assert client.post(
        "/intelligence/jev",
        json={
            "evidence": {
                "gate": "PASS",
                "checks": {"x": True},
            }
        },
    ).json()["decision"] == "PASS"

    assert client.post(
        "/intelligence/music/analyze",
        json={"path": "fixture.wav"},
    ).json()["bpm"] is not None

    assert client.post(
        "/intelligence/music/analyze",
        json={"path": "../escape.wav"},
    ).status_code in {400, 404}

    assert client.post(
        "/intelligence/harness/request",
        json={
            "task": "qc",
            "context": {},
        },
    ).json()["status"] == "ESCALATE"
