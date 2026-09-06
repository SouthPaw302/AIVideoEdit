#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import cv2
import numpy as np

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# V7 is a targeted human-review correction pass over the already-gated V6
# production renderer. It still rebuilds from the canonical stills + WAV via V4;
# it never uses V6 movie frames as production input.
import render_canon_motion_v6 as v6
from general.reusable.fx_v2.runtime import FXRuntime

v4 = v6.v4
_V6_CAMERA = v6.patched_camera_frame
_V6_RENDER = v6.patched_render_scene_frame
_V6_FINALIZE = v6.finalize_v6
_CANON_LIGHT_HANDOFF = FXRuntime.light_peak_handoff

for _name in ("underground_reflection_life", "forge_reframe"):
    if _name not in v6.DIRECTED_METRICS:
        v6.DIRECTED_METRICS[_name] = {"frames": 0, "samples": 0, "delta_sum": 0.0, "delta_max": 0.0}

_LAST_RENDER_IDX: int | None = None
_TRANSITION_PAIR = (None, None)


def underground_reflection_life(frame: np.ndarray, gi: int, start: int, end: int,
                                e: float, onset: float) -> np.ndarray:
    """Keep Shot 09 camera locked while making water/ash/ember visibly alive.

    Identity-bearing heroine and reflected face are protected. Motion is concentrated
    in dark water texture, sparse falling ash and the single narrative ember/ripple.
    This is a project-directed transform, not a new FX2 registry claim.
    """
    h, w = frame.shape[:2]
    yy, xx = v6._grid(frame.shape)
    t = gi / v4.FPS
    q = float(np.clip((gi-start) / max(1, end-start-1), 0.0, 1.0))

    amp = 12.0 + 8.0*e
    dx = amp*(0.72*np.sin(yy/10.0 + t*2.0) + 0.28*np.sin(xx/48.0 - t*1.10))
    dy = amp*(0.13*np.sin(xx/29.0 + t*1.30))
    warped = cv2.remap(frame, xx+dx.astype(np.float32), yy+dy.astype(np.float32),
                       cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT_101)

    water = np.clip((yy/h - 0.52)/0.15, 0.0, 1.0)
    hero = v6._ellipse(frame.shape, (0.25, 0.47), (0.23, 0.47), blur=28)
    reflection = v6._ellipse(frame.shape, (0.53, 0.77), (0.19, 0.20), blur=28)
    ember_holdout = v6._ellipse(frame.shape, (0.47, 0.78), (0.15, 0.12), blur=24)
    protect = np.clip(0.98*hero + 0.94*reflection + 0.95*ember_holdout, 0.0, 1.0)
    mask = cv2.GaussianBlur(np.clip(water*(1.0-protect), 0.0, 1.0), (0,0), 5) * 0.82
    out = v6._blend(frame, warped, mask)

    # Sparse falling ash: physical chamber atmosphere, never a generic particle storm.
    overlay = out.copy()
    rng = np.random.default_rng(909)
    pts = rng.random((70, 5), dtype=np.float32)
    for x0, y0, sp, ph, sz in pts:
        x = (x0*w + 18.0*math.sin(t*(0.25+0.35*sp) + ph*math.tau)) % w
        y = (y0*h + t*(7.0+15.0*sp)) % (h+30) - 15
        xi, yi = int(x), int(y)
        if 0 <= xi < w and 0 <= yi < h:
            r = 1 if sz < 0.90 else 2
            c = int(95 + 90*sz)
            cv2.circle(overlay, (xi, yi), r, (c, c, min(255, c+5)), -1, cv2.LINE_AA)
    out = cv2.addWeighted(out, 0.94, overlay, 0.06, 0)

    # The single ember becomes the moving narrative object and seeds water ripples.
    ox = 0.47 + 0.014*math.sin(t*0.52)
    oy = 0.78 + 0.004*math.sin(t*0.83 + 1.0)
    cx, cy = int(w*ox), int(h*oy)
    ripple = out.copy()
    for k in range(3):
        phase = (t*25.0 + k*58.0) % 174.0
        rx = int(14 + phase*0.70)
        ry = max(2, int(rx*0.15))
        fade = max(0.0, 1.0-phase/174.0)
        col = (int(25+18*fade), int(80+45*fade), int(150+70*fade))
        cv2.ellipse(ripple, (cx,cy), (rx,ry), 0, 0, 360, col, 1, cv2.LINE_AA)
    out = cv2.addWeighted(out, 0.86, ripple, 0.14, 0)

    # Dawn enters first through the reflection, while its facial geometry stays fixed.
    reflection_light = v6._ellipse(frame.shape, (0.53,0.77), (0.18,0.19), blur=25)
    glow = v6._ellipse(frame.shape, (ox,oy), (0.04,0.03), blur=13)
    f = out.astype(np.float32)
    f += reflection_light[...,None] * np.array([10,40,95], np.float32) * ((q**1.3)*(0.18+0.07*e))
    f += glow[...,None] * np.array([18,70,155], np.float32) * (0.50+0.20*math.sin(t*2.0)+0.15*onset)
    out = np.clip(f, 0, 255).astype(np.uint8)
    cv2.circle(out, (cx,cy), 1, (45,150,245), -1, cv2.LINE_AA)
    return out


def v7_camera_frame(base, global_i, scene_idx, cuts, energy):
    frame, k, q = _V6_CAMERA(base, global_i, scene_idx, cuts, energy)
    if scene_idx == 9:  # Shot 10: break the source circle by progressively cropping into the heroine.
        before = frame.copy()
        scene_q = float(np.clip((global_i-cuts[0]) / max(1, cuts[-1]-cuts[0]-1), 0.0, 1.0))
        z = 1.22 + 0.14*scene_q
        M = cv2.getRotationMatrix2D((v4.INTERNAL_W*0.43, v4.INTERNAL_H*0.32), 0, z)
        frame = cv2.warpAffine(frame, M, (v4.INTERNAL_W, v4.INTERNAL_H), flags=cv2.INTER_CUBIC,
                               borderMode=cv2.BORDER_REFLECT_101)
        v6._record("forge_reframe", before, frame, global_i)
    return frame, k, q


def v7_render_scene_frame(base, idx, gi, scene_start, scene_end, cuts, features, runtime, lp, depth, metrics):
    global _LAST_RENDER_IDX, _TRANSITION_PAIR
    frame = _V6_RENDER(base, idx, gi, scene_start, scene_end, cuts, features, runtime, lp, depth, metrics)

    previous = _LAST_RENDER_IDX
    _LAST_RENDER_IDX = idx
    if previous is not None:
        _TRANSITION_PAIR = (previous, idx)

    if idx == 8:  # Shot 09 locked camera, internal water/reflection life only.
        before = frame.copy()
        e = float(features["rms"][gi]); onset = float(features["onset"][gi])
        frame = underground_reflection_life(frame, gi, scene_start, scene_end, e, onset)
        v6._record("underground_reflection_life", before, frame, gi)
    return frame


def identity_safe_light_handoff(self, a, b, p, origin=(.78,.17), strength=.42):
    """Use canonical FX2-TRANS-003 with a compressed blend only on Shot 10 -> 11.

    V6 human review found a brief two-face exposure. The canonical handoff remains the
    engine, but this boundary remaps its progress so the overlap occurs under a
    face-centered light peak instead of lingering across twelve frames.
    """
    if _TRANSITION_PAIR == (9, 10):
        q = float(np.clip((float(p)-0.38)/0.24, 0.0, 1.0))
        q = q*q*(3.0-2.0*q)
        return _CANON_LIGHT_HANDOFF(self, a, b, q, origin=(0.43,0.30), strength=1.20)
    return _CANON_LIGHT_HANDOFF(self, a, b, p, origin=origin, strength=strength)


def _rename_if(out: Path, old: str, new: str):
    src, dst = out/old, out/new
    if src.exists():
        src.replace(dst)


def make_v7_review_contact(master: Path, out: Path):
    groups = [
        ("S09", [167.5,172.0,177.0,182.0,186.5]),
        ("S10", [187.5,192.0,198.5,204.5,209.5]),
        ("T10-11", [209.55,209.75,209.90,210.05,210.20]),
    ]
    cap = cv2.VideoCapture(str(master))
    rows = []
    try:
        for label, times in groups:
            thumbs=[]
            for t in times:
                cap.set(cv2.CAP_PROP_POS_MSEC, t*1000.0)
                ok, frame = cap.read()
                if not ok:
                    frame = np.zeros((216,384,3), np.uint8)
                else:
                    frame = cv2.resize(frame, (384,216), interpolation=cv2.INTER_AREA)
                cv2.rectangle(frame,(0,0),(132,25),(0,0,0),-1)
                cv2.putText(frame,f"{label} {t:.2f}s",(5,18),cv2.FONT_HERSHEY_SIMPLEX,.45,(255,255,255),1,cv2.LINE_AA)
                thumbs.append(frame)
            rows.append(np.hstack(thumbs))
    finally:
        cap.release()
    cv2.imwrite(str(out), np.vstack(rows), [cv2.IMWRITE_JPEG_QUALITY, 92])


def finalize_v7(out: Path):
    # First run all V6 export/effect/motion gates against the V7-rendered pixels.
    _V6_FINALIZE(out)

    _rename_if(out, "IRONFLAME_V6_REFERENCE_CALIBRATED_720p24.mp4", "IRONFLAME_V7_HUMAN_CORRECTED_720p24.mp4")
    _rename_if(out, "IRONFLAME_V6_CONTACT_12.jpg", "IRONFLAME_V7_CONTACT_12.jpg")
    _rename_if(out, "IRONFLAME_V6_CONTROL_SUMMARY.json", "IRONFLAME_V7_CONTROL_SUMMARY.json")
    _rename_if(out, "IRONFLAME_V6_DIRECTED_EFFECT_EVIDENCE.json", "IRONFLAME_V7_DIRECTED_EFFECT_EVIDENCE.json")

    old_qc = out/"IRONFLAME_V6_FINAL_QC.json"
    qc = json.loads(old_qc.read_text()) if old_qc.exists() else {}
    if old_qc.exists():
        old_qc.unlink()

    master = out/"IRONFLAME_V7_HUMAN_CORRECTED_720p24.mp4"
    scene9 = qc.get("motion_flow_qc",{}).get("per_scene",{}).get("scene09",{}).get("mean_flow_px",0.0)
    dm = qc.get("directed_transform_metrics",{})
    reflection_ok = dm.get("underground_reflection_life",{}).get("frames",0) > 0 and dm.get("underground_reflection_life",{}).get("delta_max",0) > 0
    reframe_ok = dm.get("forge_reframe",{}).get("frames",0) > 0 and dm.get("forge_reframe",{}).get("delta_max",0) > 0
    scene9_improved = scene9 >= 0.12
    correction_gate = reflection_ok and reframe_ok and scene9_improved

    qc["title"] = "IronFlame V7 Human-Corrected Canon"
    qc["master"] = master.name
    qc["sha256"] = v4.sha256(master)
    qc["v6_human_review_corrections"] = {
        "shot09_locked_camera_internal_life": "stronger protected water texture, sparse chamber ash, moving narrative ember/ripples, reflection dawn migration",
        "shot10_portal_read": "progressive heroine-centered crop de-emphasizes the source circular arch while preserving broken forged arcs",
        "transition_10_to_11": "canonical FX2-TRANS-003 retained; blend progress compressed under a face-centered light peak to suppress double-face ghosting",
    }
    qc["v7_correction_gate"] = {
        "underground_reflection_life_used": reflection_ok,
        "forge_reframe_used": reframe_ok,
        "scene09_mean_flow_px": scene9,
        "scene09_minimum": 0.12,
        "result": "PASS" if correction_gate else "FAIL",
    }
    qc["status"] = "HUMAN_REVIEW_CANDIDATE" if qc.get("status") == "DIRECTED_DELIVERY_CANDIDATE" and correction_gate else "QC_FAIL"
    (out/"IRONFLAME_V7_FINAL_QC.json").write_text(json.dumps(qc, indent=2))

    if master.exists():
        make_v7_review_contact(master, out/"IRONFLAME_V7_REVIEW_CONTACT.jpg")
    if not correction_gate:
        raise RuntimeError(f"V7 human correction gate failed: {qc['v7_correction_gate']}")


def main():
    # Patch only project-level wrappers. Canonical runtime file and FX lock remain unchanged.
    v6.patched_camera_frame = v7_camera_frame
    v6.patched_render_scene_frame = v7_render_scene_frame
    v6.finalize_v6 = finalize_v7
    FXRuntime.light_peak_handoff = identity_safe_light_handoff
    v6.main()


if __name__ == "__main__":
    main()
