from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, ConfigDict, Field

from runtime_v2.gatekeeper import evaluate_action
from runtime_v2.harness.adapter import (
    specialist_request,
    status as harness_status,
)
from runtime_v2.jev.decision import decide as jev_decide
from runtime_v2.models.music_beat import analyze_music
from runtime_v2.models.registry import ModelRegistry

router = APIRouter(
    prefix="/intelligence",
    tags=["intelligence"],
)


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class GateRequest(StrictModel):
    action: str = Field(min_length=1, max_length=128)
    mutation: bool = False
    requested_changes: list[str] = Field(
        default_factory=list,
        max_length=64,
    )
    expected_stage: str | None = None
    target_branch: str | None = None
    protected_canon_replacement: bool = False


class JevRequest(StrictModel):
    evidence: dict[str, Any]


class MusicRequest(StrictModel):
    path: str = Field(min_length=1)


class SpecialistRequest(StrictModel):
    task: str = Field(min_length=1, max_length=256)
    context: dict[str, Any] = Field(default_factory=dict)


def _repo_root() -> Path:
    root = Path(
        os.environ.get("AIVIDEOEDIT_REPO_ROOT") or Path.cwd()
    ).expanduser().resolve()
    if not root.is_dir():
        raise HTTPException(
            status_code=503,
            detail="AIVIDEOEDIT_REPO_ROOT is not a directory",
        )
    return root


def _safe_repo_path(value: str) -> Path:
    repo = _repo_root()
    p = Path(value)
    resolved = p.resolve() if p.is_absolute() else (repo / p).resolve()
    if resolved != repo and repo not in resolved.parents:
        raise HTTPException(
            status_code=400,
            detail="path escapes repository root",
        )
    if not resolved.is_file():
        raise HTTPException(
            status_code=404,
            detail="file not found",
        )
    return resolved


@router.get("/status")
def intelligence_status():
    repo = _repo_root()
    registry = ModelRegistry.load_default()
    try:
        music = registry.resolve_capability(
            "music_and_beat_analysis"
        )
        music_status = {
            "resolved": music.resolved,
            "available": music.available,
            "used_fallback": music.used_fallback,
            "reason": music.reason,
        }
    except Exception as exc:
        music_status = {
            "available": False,
            "error": str(exc),
        }

    enabled = os.environ.get(
        "AIVIDEOEDIT_HARNESS_ENABLED",
        "0",
    ).lower() in {"1", "true", "yes", "on"}

    return {
        "schema": "aivideoedit.intelligence-status.v1",
        "boot_capsule": (
            repo / ".aivideoedit" / "boot_capsule.json"
        ).is_file(),
        "session_attestation": (
            repo / ".aivideoedit" / "session_attestation.json"
        ).is_file(),
        "music_analysis": music_status,
        "harness": harness_status(enabled).as_dict(),
    }


@router.post("/gate")
def gate(request: GateRequest):
    return evaluate_action(
        repo=_repo_root(),
        action=request.action,
        mutation=request.mutation,
        requested_changes=request.requested_changes,
        expected_stage=request.expected_stage,
        target_branch=request.target_branch,
        protected_canon_replacement=(
            request.protected_canon_replacement
        ),
    ).as_dict()


@router.get("/models")
def models():
    registry = ModelRegistry.load_default()
    return {
        "schema": registry.data.get("schema"),
        "models": list(registry.models.values()),
    }


@router.get("/models/resolve/{capability}")
def resolve_model(capability: str):
    try:
        r = ModelRegistry.load_default().resolve_capability(
            capability
        )
    except KeyError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc
    return {
        "requested": r.requested,
        "resolved": r.resolved,
        "available": r.available,
        "used_fallback": r.used_fallback,
        "reason": r.reason,
        "authority": r.record.get("authority"),
    }


@router.post("/music/analyze")
def music_analyze(request: MusicRequest):
    try:
        return analyze_music(
            _safe_repo_path(request.path)
        )
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc


@router.post("/jev")
def jev(request: JevRequest):
    return jev_decide(request.evidence)


@router.get("/harness")
def harness():
    enabled = os.environ.get(
        "AIVIDEOEDIT_HARNESS_ENABLED",
        "0",
    ).lower() in {"1", "true", "yes", "on"}
    return harness_status(enabled).as_dict()


@router.post("/harness/request")
def harness_request(request: SpecialistRequest):
    return specialist_request(
        task=request.task,
        context=request.context,
        provider=None,
    )
