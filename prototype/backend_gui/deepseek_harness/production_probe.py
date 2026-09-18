#!/usr/bin/env python3
"""Run one isolated AIVideoEdit production-direction probe through the existing Tool API.

This is a prototype/deepseek-harness test helper. It does not mutate repository main
and does not bypass canonical production guards.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parent
STACK = BACKEND / "stack.py"


def _json_request(url: str, payload: dict | None = None):
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"} if data else {})
    with urllib.request.urlopen(req, timeout=600) as response:
        return json.loads(response.read().decode("utf-8"))


def _tool(name: str, arguments: dict | None = None):
    result = _json_request(
        "http://127.0.0.1:8080/api/tools/call",
        {"name": name, "arguments": arguments or {}},
    )
    if not result.get("ok", False):
        raise RuntimeError(f"{name} failed: {result}")
    return result["result"]


def _upload(project_id: str, source: Path, content_type: str):
    query = urllib.parse.urlencode({"project": project_id, "filename": source.name})
    data = source.read_bytes()
    req = urllib.request.Request(
        f"http://127.0.0.1:8080/api/assets?{query}",
        data=data,
        headers={"Content-Type": content_type, "Content-Length": str(len(data))},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=600) as response:
        return json.loads(response.read().decode("utf-8"))


def _wait_until(predicate, timeout: int, interval: float = 1.0):
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        last = predicate()
        if last:
            return last
        time.sleep(interval)
    raise TimeoutError(f"condition timed out; last={last!r}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio", required=True)
    ap.add_argument("--video", required=True)
    ap.add_argument("--evidence-dir", required=True)
    args = ap.parse_args()

    audio = Path(args.audio).resolve()
    video = Path(args.video).resolve()
    evidence = Path(args.evidence_dir).resolve()
    evidence.mkdir(parents=True, exist_ok=True)

    runtime = Path(os.environ.get("AIVE_RUNTIME") or (evidence / "runtime")).resolve()
    env = dict(os.environ)
    env.update({"AIVE_HOST": "127.0.0.1", "AIVE_PORT": "8080", "AIVE_RUNTIME": str(runtime)})

    stack_log = (evidence / "aive-stack.log").open("w", encoding="utf-8")
    proc = subprocess.Popen([sys.executable, str(STACK)], cwd=str(BACKEND), env=env, stdout=stack_log, stderr=subprocess.STDOUT)
    try:
        _wait_until(lambda: _json_request("http://127.0.0.1:8080/api/system") if _ping() else None, 60)

        core = _json_request("http://127.0.0.1:8080/api/core/bootstrap", {"offline": False})
        (evidence / "core-bootstrap.json").write_text(json.dumps(core, indent=2, sort_keys=True), encoding="utf-8")
        if not (
            core.get("bootstrapped")
            and core.get("host_branch") == "prototype/deepseek-harness"
            and core.get("core_branch") == "main"
            and core.get("guard_result") == "PASS"
        ):
            raise RuntimeError(f"canonical bootstrap failed isolation/guard checks: {core}")

        project = _tool("project.create", {"name": "Midnight Tribal Pulse DeepSeek Harness Test"})["project"]
        pid = project["id"]
        if pid != "midnight-tribal-pulse-deepseek-harness-test":
            raise RuntimeError(f"unexpected project id: {pid}")

        uploads = [
            _upload(pid, audio, "audio/mpeg"),
            _upload(pid, video, "video/mp4"),
        ]
        (evidence / "uploads.json").write_text(json.dumps(uploads, indent=2), encoding="utf-8")

        def assets_ready():
            status = _tool("project.status", {"project_id": pid})
            return status if status.get("ready_assets", 0) >= 2 else None
        _wait_until(assets_ready, 180)

        _tool("project.prepare", {"project_id": pid})
        def qc_ready():
            status = _tool("project.status", {"project_id": pid})
            if status.get("active_jobs") == 0 and status.get("qc_fail") == 0 and status.get("qc_pass", 0) >= 2:
                return status
            return None
        qc = _wait_until(qc_ready, 300)
        (evidence / "project-qc.json").write_text(json.dumps(qc, indent=2, sort_keys=True), encoding="utf-8")

        snapshots = []
        init = _tool("production.initialize", {"project_id": pid})
        snapshots.append({"label": "initialized", "production": init, "context": _tool("harness.context", {"project_id": pid})})

        _tool("production.sync_assets", {"project_id": pid})
        snapshots.append({"label": "before-source-ingested", "context": _tool("harness.context", {"project_id": pid})})
        _tool("production.advance", {"project_id": pid, "target_stage": "SOURCE_INGESTED"})
        snapshots.append({"label": "source-ingested", "context": _tool("harness.context", {"project_id": pid})})

        # No lyric text was supplied for this run; treat the track as instrumental for directing purposes.
        _tool(
            "production.set_music_context",
            {
                "project_id": pid,
                "lyrics_status": "absent",
                "genre": "psychedelic tribal electronic / tribal house",
                "directing_use": "music structure, energy, rhythm and transitions drive pacing; supplied visual reference governs picture language",
            },
        )
        _tool("production.analyze", {"project_id": pid})
        _wait_until(lambda: _tool("project.status", {"project_id": pid}) if _tool("project.status", {"project_id": pid}).get("active_jobs") == 0 else None, 420)

        snapshots.append({"label": "before-references-analyzed", "context": _tool("harness.context", {"project_id": pid})})
        _tool("production.advance", {"project_id": pid, "target_stage": "REFERENCES_ANALYZED"})
        snapshots.append({"label": "references-analyzed", "context": _tool("harness.context", {"project_id": pid})})

        _tool(
            "approach.set_capabilities",
            {
                "project_id": pid,
                "capabilities": [
                    "source_video",
                    "extracted_frames",
                    "generated_stills",
                    "generated_support_imagery",
                    "living_painting",
                    "living_still_fx",
                    "layered_composite",
                    "depth_25d",
                    "atmospheric_plate",
                    "reactive_plate",
                    "loop_media",
                    "transition_media",
                    "conventional_video",
                    "analysis_qc_media",
                ],
                "approach_summary": (
                    "Reference-led hybrid production. Preserve the supplied nocturnal desert-oracle picture language: "
                    "ornate organic figure, sacred circular geometry, cactus/rock foreground, lunar/cosmic sky, warm gold and earth "
                    "against deep indigo. Extend it with source-derived and newly generated coherent stills, living-scene internal "
                    "motion, restrained 2.5D depth, atmospheric particles, and measured music-reactive illumination. Camera movement "
                    "remains secondary; section changes may use deliberate cinematic transitions without breaking the visual world."
                ),
            },
        )
        _tool(
            "operating.configure_v2",
            {
                "project_id": pid,
                "direction_authority": "reference_led",
                "production_mode": "hybrid",
                "mission": (
                    "Expand the supplied desert-cosmos living scene into one coherent nocturnal ritual world across the entire track, "
                    "with visual intensity rising and releasing with the music."
                ),
                "current_user_direction": (
                    "Use only this run supplied song and reference media as creative authority; do not import imagery, characters, "
                    "storyboards or assumptions from previous productions."
                ),
                "exact_next_action": (
                    "Lock the supplied reference as picture-language baseline, then author a full-song storyboard mapped to analyzed musical sections."
                ),
            },
        )
        media = _tool("media.list", {"project_id": pid})["assets"]
        baseline = next(x for x in media if x.get("filename") == video.name)
        _tool(
            "operating.lock_canon",
            {
                "project_id": pid,
                "picture_language": (
                    "Psychedelic nocturnal desert oracle: intricate organic and sacred-geometry illustration, cactus and rock terrain, "
                    "celestial moon and star field, warm amber-gold bioluminescence against indigo-violet night, contemplative mystical "
                    "scale, stable composition with living internal motion."
                ),
                "items": [
                    "Preserve warm gold/earth versus deep indigo-violet palette.",
                    "Preserve sacred circular halo geometry and luminous orb motifs without cloning one static composition.",
                    "Desert botanical and rocky foreground remains tactile and richly detailed.",
                    "Motion is primarily internal: glow, particles, celestial drift, botanical breathing, ornament micro-motion and parallax; avoid aggressive camera drift.",
                    "Visual evolution follows musical energy while retaining one coherent world.",
                    "Do not introduce unrelated characters, urban imagery, photoreal live-action aesthetics or previous-project canon.",
                ],
                "baseline_asset_id": baseline["id"],
                "acceptance_statement": (
                    "The supplied mescalito_living_scene.mp4 is the current-run visual reference and accepted baseline for picture language and motion behavior."
                ),
            },
        )

        snapshots.append({"label": "before-approach-established", "context": _tool("harness.context", {"project_id": pid})})
        _tool("production.advance", {"project_id": pid, "target_stage": "APPROACH_ESTABLISHED"})
        snapshots.append({"label": "approach-established", "context": _tool("harness.context", {"project_id": pid})})
        (evidence / "harness-context-transitions.json").write_text(json.dumps(snapshots, indent=2, sort_keys=True), encoding="utf-8")

        status = _tool("production.status", {"project_id": pid})
        project_dir = Path(status["project_dir"])
        for name in ["PROJECT_STATE.json", "REFERENCE_MANIFEST.json", "MUSIC_ANALYSIS.json", "MEDIA_PLAN.json", "OPERATING_ORDER.json"]:
            shutil.copy2(project_dir / name, evidence / name)
        analysis_dir = runtime / "projects" / pid / "analysis"
        if analysis_dir.is_dir():
            shutil.copytree(analysis_dir, evidence / "analysis", dirs_exist_ok=True)

        (evidence / "final-status.json").write_text(
            json.dumps(
                {
                    "production": status,
                    "harness": _tool("harness.context", {"project_id": pid}),
                    "approach": _tool("approach.status", {"project_id": pid}),
                    "operating": _tool("operating.status", {"project_id": pid}),
                },
                indent=2,
                sort_keys=True,
            ),
            encoding="utf-8",
        )
        return 0
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
        stack_log.close()


def _ping() -> bool:
    try:
        with urllib.request.urlopen("http://127.0.0.1:8080/api/system", timeout=2):
            return True
    except Exception:
        return False


if __name__ == "__main__":
    raise SystemExit(main())
