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

# This wrapper intentionally reuses the already-gated V4 production renderer as the
# base engine, then replaces its generic camera/effect behavior with shot-specific
# canon direction. The underlying FX2 calls still run through the V4 renderer and
# remain covered by the fail-closed FX lock gate.
import render_canon_motion_v4 as v4
from general.reusable.fx_v2.runtime import FXContext

v4.FXContext = FXContext

_ORIGINAL_CAMERA = v4.camera_frame
_ORIGINAL_RENDER = v4.render_scene_frame
_ORIGINAL_EFFECTS = v4.scene_effects

DIRECTED_METRICS = {
    name: {"frames": 0, "samples": 0, "delta_sum": 0.0, "delta_max": 0.0}
    for name in (
        "subject_edge_flow",
        "gravity_inversion",
        "focus_pull",
        "palette_migration",
        "forged_waveform",
        "rack_focus",
        "wall_relief_breath",
    )
}
EVIDENCE: dict[str, tuple[np.ndarray, np.ndarray]] = {}


def _grid(shape):
    h, w = shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    return yy, xx


def _ellipse(shape, center, radius, blur=16.0):
    h, w = shape[:2]
    yy, xx = _grid(shape)
    cx, cy = center
    rx, ry = radius
    m = ((((xx-cx*w)/(rx*w+1e-6))**2 + ((yy-cy*h)/(ry*h+1e-6))**2) <= 1.0).astype(np.float32)
    if blur:
        m = cv2.GaussianBlur(m, (0, 0), blur)
    return np.clip(m, 0.0, 1.0)


def _blend(a, b, mask):
    m = np.clip(mask, 0.0, 1.0).astype(np.float32)
    return np.clip(a.astype(np.float32)*(1.0-m[..., None]) + b.astype(np.float32)*m[..., None], 0, 255).astype(np.uint8)


def _record(name: str, before: np.ndarray, after: np.ndarray, gi: int):
    m = DIRECTED_METRICS[name]
    m["frames"] += 1
    if gi % 24 == 0:
        d = float(np.mean(np.abs(after.astype(np.float32)-before.astype(np.float32))))
        m["samples"] += 1
        m["delta_sum"] += d
        m["delta_max"] = max(m["delta_max"], d)
    if name not in EVIDENCE:
        EVIDENCE[name] = (before.copy(), after.copy())


def subject_edge_flow(frame, idx: int, gi: int, e: float):
    # Move cloak/hair/outer silhouette while strongly protecting the face/core.
    cx, cy, rx, ry = v4.SCENE_FOCUS[idx]
    outer = _ellipse(frame.shape, (cx, cy), (rx*1.02, ry*1.04), blur=18)
    core = _ellipse(frame.shape, (cx, cy-ry*0.10), (rx*0.42, ry*0.40), blur=20)
    ring = np.clip(outer*(1.0-core), 0.0, 1.0)
    yy, xx = _grid(frame.shape)
    p = gi / v4.FPS
    amp = 2.0 + 2.4*e
    dx = amp*(0.65*np.sin(yy/43.0 + p*1.7) + 0.35*np.sin((xx+yy)/79.0 - p*1.1))
    dy = amp*(0.55*np.sin(xx/59.0 - p*1.3))
    warped = cv2.remap(frame, xx+dx.astype(np.float32), yy+dy.astype(np.float32), cv2.INTER_CUBIC,
                       borderMode=cv2.BORDER_REFLECT_101)
    return _blend(frame, warped, ring*0.66)


def gravity_inversion(frame, gi: int, start: int, end: int, e: float, onset: float):
    q = np.clip((gi-start)/max(1, end-start-1), 0.0, 1.0)
    # The architecture visibly loses orientation, but the scale protects borders.
    angle = 5.8*math.sin(math.pi*q) + 2.2*math.sin(3.0*math.pi*q)*(0.35+0.65*e)
    scale = 1.075 + 0.018*math.sin(math.pi*q)
    h, w = frame.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), angle, scale)
    M[0, 2] += math.sin(q*math.tau)*4.0
    M[1, 2] -= math.sin(math.pi*q)*5.0
    out = cv2.warpAffine(frame, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT_101)

    # Suspended debris is deterministic and rises/falls against gravity pressure.
    rng = np.random.default_rng(707)
    pts = rng.random((46, 4), dtype=np.float32)
    overlay = out.copy()
    for x, y, s, ph in pts:
        px = int((x*w + 18*math.sin(q*math.tau + ph*6.0)) % w)
        py = int(np.clip(y*h - math.sin(math.pi*q)*(35+55*s) + 8*math.sin(q*math.tau*2+ph*7), 0, h-1))
        r = max(1, int(1+s*2.2 + onset*1.5))
        c = int(105 + 70*s)
        cv2.circle(overlay, (px, py), r, (c, c, min(255, c+18)), -1, cv2.LINE_AA)
    return cv2.addWeighted(out, 0.90, overlay, 0.10+0.07*onset, 0)


def focus_pull(frame, q: float, center_a=(0.17, 0.72), center_b=(0.53, 0.46)):
    h, w = frame.shape[:2]
    blur = cv2.GaussianBlur(frame, (0, 0), 7.0)
    cx = center_a[0]*(1-q) + center_b[0]*q
    cy = center_a[1]*(1-q) + center_b[1]*q
    sharp = _ellipse(frame.shape, (cx, cy), (0.22, 0.28), blur=32)
    return _blend(blur, frame, sharp)


def palette_migration(frame, q: float, e: float, strength=1.0):
    # Iron-blue/ash shadows gradually yield to dawn-gold highlights.
    f = frame.astype(np.float32)
    lum = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)/255.0
    highlight = cv2.GaussianBlur(np.clip((lum-0.34)/0.55, 0, 1), (0, 0), 8)
    gold = np.array([38.0, 84.0, 146.0], np.float32)  # BGR warmth lift
    blue = np.array([28.0, 12.0, -8.0], np.float32)
    shift = blue*(1.0-q) + gold*q
    alpha = (0.045 + 0.095*q + 0.035*e)*strength
    f += highlight[..., None]*shift[None, None, :]*alpha
    # Quietly desaturate the deepest ash before gold arrives.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gray3 = np.repeat(gray[..., None], 3, axis=2)
    ash = (1.0-highlight)[..., None]*(0.04*(1.0-q))
    f = f*(1.0-ash) + gray3*ash
    return np.clip(f, 0, 255).astype(np.uint8)


def wall_relief_breath(frame, q: float, e: float):
    # Reveal wall relief/faces only through moving side light, avoiding global morphing.
    h, w = frame.shape[:2]
    yy, xx = _grid(frame.shape)
    left = np.exp(-(((xx-w*0.18)/(w*0.24))**2 + ((yy-h*0.48)/(h*0.55))**2)).astype(np.float32)
    right = np.exp(-(((xx-w*0.83)/(w*0.24))**2 + ((yy-h*0.48)/(h*0.55))**2)).astype(np.float32)
    pulse = 0.5 + 0.5*math.sin(q*math.tau*1.4)
    mask = np.clip((left+right)*0.5, 0, 1)
    edges = cv2.Laplacian(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.CV_32F, ksize=3)
    edges = cv2.GaussianBlur(np.abs(edges), (0, 0), 1.2)
    edges /= float(np.percentile(edges, 97)+1e-6)
    lift = (0.55 + 0.45*np.clip(edges, 0, 1))*mask*(12.0+14.0*e)*pulse
    out = frame.astype(np.float32) + lift[..., None]*np.array([0.55, 0.78, 1.0], np.float32)
    return np.clip(out, 0, 255).astype(np.uint8)


def forged_waveform(frame, gi: int, e: float, low: float, mid: float, high: float, onset: float):
    # In-world radial forged waveform: a restrained iron/ember ring, not a generic HUD.
    h, w = frame.shape[:2]
    cx, cy = int(w*0.52), int(h*0.55)
    overlay = frame.copy()
    n = 72
    phase = gi*0.045
    base_r = min(w, h)*(0.19 + 0.015*low)
    pts = []
    for i in range(n+1):
        a = (i/n)*math.tau
        band = (0.48*low*math.sin(a*2+phase) + 0.33*mid*math.sin(a*5-phase*0.8) + 0.19*high*math.sin(a*11+phase*1.4))
        r = base_r*(1.0 + 0.10*band + 0.035*onset*math.sin(a*9+phase*2))
        pts.append([int(cx+math.cos(a)*r), int(cy+math.sin(a)*r)])
    pts = np.asarray(pts, np.int32).reshape((-1, 1, 2))
    warm = int(np.clip(138 + 85*high + 20*onset, 0, 255))
    cv2.polylines(overlay, [pts], False, (34, 88, warm), 1+(1 if onset>0.72 else 0), cv2.LINE_AA)
    # Sparse radial sparks at transients.
    if onset > 0.45:
        for i in range(0, n, 8):
            a = (i/n)*math.tau + phase*0.08
            r0, r1 = base_r*1.02, base_r*(1.05+0.07*onset)
            p0 = (int(cx+math.cos(a)*r0), int(cy+math.sin(a)*r0))
            p1 = (int(cx+math.cos(a)*r1), int(cy+math.sin(a)*r1))
            cv2.line(overlay, p0, p1, (28, 102, min(255, warm+20)), 1, cv2.LINE_AA)
    return cv2.addWeighted(frame, 0.80, overlay, 0.20+0.12*e, 0)


def rack_focus(frame, q: float):
    # Final scene: imperfect legacy mark resolves first; heroine resolves second.
    blur = cv2.GaussianBlur(frame, (0, 0), 8.0)
    mark = _ellipse(frame.shape, (0.36, 0.64), (0.18, 0.20), blur=28)
    hero = _ellipse(frame.shape, (0.61, 0.46), (0.20, 0.28), blur=28)
    # Cross-focus with a short overlap so the handoff feels optical rather than a cut.
    a = np.clip(1.0 - q*1.35, 0, 1)
    b = np.clip((q-0.28)/0.72, 0, 1)
    sharp = np.clip(mark*a + hero*b, 0, 1)
    return _blend(blur, frame, sharp)


def patched_camera_frame(base, global_i, scene_idx, cuts, energy):
    frame, k, q = _ORIGINAL_CAMERA(base, global_i, scene_idx, cuts, energy)
    # Shot 09 is canonically a locked-camera recognition scene; undo generic camera drift.
    if scene_idx == 8:
        frame = base.copy()
    # Shot 08 wants a deep hallway push; strengthen depth without increasing cut rate.
    elif scene_idx == 7:
        z = 1.00 + 0.055*q
        M = cv2.getRotationMatrix2D((v4.INTERNAL_W/2, v4.INTERNAL_H/2), 0, z)
        frame = cv2.warpAffine(frame, M, (v4.INTERNAL_W, v4.INTERNAL_H), flags=cv2.INTER_CUBIC,
                               borderMode=cv2.BORDER_REFLECT_101)
    # Shot 10 is the ascendant push through the forge gate.
    elif scene_idx == 9:
        z = 1.00 + 0.045*q
        M = cv2.getRotationMatrix2D((v4.INTERNAL_W/2, v4.INTERNAL_H/2), 0, z)
        frame = cv2.warpAffine(frame, M, (v4.INTERNAL_W, v4.INTERNAL_H), flags=cv2.INTER_CUBIC,
                               borderMode=cv2.BORDER_REFLECT_101)
    return frame, k, q


def patched_scene_effects(idx: int, e: float):
    effects = _ORIGINAL_EFFECTS(idx, e)
    # Approved water-flow effect becomes the puddle/wet-ground layer in Shot 01.
    if idx == 0 and not any(x["id"] == "FX2-MOTION-003" for x in effects):
        effects.append({"id": "FX2-MOTION-003", "strength": 0.34+0.20*e, "roi": [0.0, 0.72, 1.0, 1.0], "reflect": False})
    # Rain belongs to exterior planes; make the threshold pass less like a full-frame overlay.
    if idx == 1:
        for fx in effects:
            if fx["id"] == "FX2-ATM-002":
                fx["roi"] = [0.0, 0.0, 0.58, 1.0]
    return effects


def patched_render_scene_frame(base, idx, gi, scene_start, scene_end, cuts, features, runtime, lp, depth, metrics):
    frame = _ORIGINAL_RENDER(base, idx, gi, scene_start, scene_end, cuts, features, runtime, lp, depth, metrics)
    q = np.clip((gi-scene_start)/max(1, scene_end-scene_start-1), 0.0, 1.0)
    e = float(features["rms"][gi])
    onset = float(features["onset"][gi])
    low = float(features["low"][gi]); mid = float(features["mid"][gi]); high = float(features["high"][gi])

    # Character/cloth micro-motion in journey, emergence and legacy scenes.
    if idx in (4, 5, 9, 10, 11):
        before = frame
        frame = subject_edge_flow(frame, idx, gi, e)
        _record("subject_edge_flow", before, frame, gi)

    if idx == 3:
        before = frame
        frame = wall_relief_breath(frame, q, e)
        _record("wall_relief_breath", before, frame, gi)

    if idx == 5:
        before = frame
        frame = palette_migration(frame, q, e, strength=0.72)
        _record("palette_migration", before, frame, gi)

    if idx == 6:
        before = frame
        frame = gravity_inversion(frame, gi, scene_start, scene_end, e, onset)
        _record("gravity_inversion", before, frame, gi)

    if idx == 7:
        before = frame
        frame = focus_pull(frame, q)
        _record("focus_pull", before, frame, gi)

    if idx == 9:
        before = frame
        frame = forged_waveform(frame, gi, e, low, mid, high, onset)
        _record("forged_waveform", before, frame, gi)

    if idx == 10:
        before = frame
        frame = palette_migration(frame, q, e, strength=1.00)
        _record("palette_migration", before, frame, gi)

    if idx == 11:
        before = frame
        frame = rack_focus(frame, q)
        _record("rack_focus", before, frame, gi)

    return frame


def output_dir_from_argv() -> Path:
    if "--output-dir" not in sys.argv:
        raise RuntimeError("--output-dir is required for V5 evidence finalization")
    return Path(sys.argv[sys.argv.index("--output-dir")+1]).resolve()


def analyze_motion(path: Path):
    cap = cv2.VideoCapture(str(path))
    fps = cap.get(cv2.CAP_PROP_FPS) or 24.0
    step = max(1, int(round(fps)))
    i = 0
    prev = None
    means = []
    p90s = []
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if i % step == 0:
            g = cv2.cvtColor(cv2.resize(frame, (320, 180), interpolation=cv2.INTER_AREA), cv2.COLOR_BGR2GRAY)
            if prev is not None:
                flow = cv2.calcOpticalFlowFarneback(prev, g, None, 0.5, 3, 15, 3, 5, 1.1, 0)
                mag = np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)
                means.append(float(np.mean(mag)))
                p90s.append(float(np.percentile(mag, 90)))
            prev = g
        i += 1
    cap.release()
    return {
        "sample_interval_seconds": 1.0,
        "samples": len(means),
        "mean_flow_px": float(np.mean(means)) if means else 0.0,
        "p90_flow_px_mean": float(np.mean(p90s)) if p90s else 0.0,
        "max_mean_flow_px": float(np.max(means)) if means else 0.0,
    }


def finalize_v5(out: Path):
    renames = {
        "IRONFLAME_V4_CANON_MOTION_720p24.mp4": "IRONFLAME_V5_DIRECTED_CANON_720p24.mp4",
        "IRONFLAME_V4_CONTACT_12.jpg": "IRONFLAME_V5_CONTACT_12.jpg",
        "IRONFLAME_V4_FINAL_QC.json": "IRONFLAME_V5_FINAL_QC.json",
        "IRONFLAME_V4_CONTROL_SUMMARY.json": "IRONFLAME_V5_CONTROL_SUMMARY.json",
    }
    for old, new in renames.items():
        src, dst = out/old, out/new
        if src.exists():
            src.replace(dst)

    evdir = out/"directed_effect_evidence"
    evdir.mkdir(exist_ok=True)
    for name, (before, after) in EVIDENCE.items():
        cv2.imwrite(str(evdir/f"{name}_before.jpg"), before)
        cv2.imwrite(str(evdir/f"{name}_after.jpg"), after)

    normalized = {}
    for name, m in DIRECTED_METRICS.items():
        normalized[name] = dict(m)
        normalized[name]["sample_delta_mean"] = (m["delta_sum"]/m["samples"]) if m["samples"] else 0.0
        normalized[name].pop("delta_sum", None)

    required = ("subject_edge_flow", "gravity_inversion", "focus_pull", "palette_migration", "forged_waveform", "rack_focus", "wall_relief_breath")
    usage_pass = all(normalized[x]["frames"] > 0 and normalized[x]["delta_max"] > 0.0 for x in required)

    master = out/"IRONFLAME_V5_DIRECTED_CANON_720p24.mp4"
    motion = analyze_motion(master) if master.exists() else {"samples": 0, "mean_flow_px": 0.0, "p90_flow_px_mean": 0.0, "max_mean_flow_px": 0.0}
    motion_pass = motion["samples"] > 50 and motion["mean_flow_px"] > 0.05

    qc_path = out/"IRONFLAME_V5_FINAL_QC.json"
    if qc_path.exists():
        qc = json.loads(qc_path.read_text())
    else:
        qc = {}
    qc["title"] = "IronFlame V5 Directed Canon"
    qc["master"] = master.name
    qc["directed_transform_metrics"] = normalized
    qc["directed_transform_usage_gate"] = "PASS" if usage_pass else "FAIL"
    qc["motion_flow_qc"] = motion
    qc["motion_flow_gate"] = "PASS" if motion_pass else "FAIL"
    qc["canon_direction"] = {
        "shot07_gravity_inversion": normalized["gravity_inversion"]["frames"] > 0,
        "shot08_focus_pull": normalized["focus_pull"]["frames"] > 0,
        "shot09_locked_camera": True,
        "shot10_forged_waveform": normalized["forged_waveform"]["frames"] > 0,
        "shot11_blue_to_gold": normalized["palette_migration"]["frames"] > 0,
        "shot12_rack_focus": normalized["rack_focus"]["frames"] > 0,
    }
    if qc.get("status") == "DELIVERY_CANDIDATE" and usage_pass and motion_pass:
        qc["status"] = "DIRECTED_DELIVERY_CANDIDATE"
    else:
        qc["status"] = "QC_FAIL"
    qc_path.write_text(json.dumps(qc, indent=2))

    evidence = {
        "result": "PASS" if usage_pass else "FAIL",
        "metrics": normalized,
        "evidence_files": sorted(str(p.relative_to(out)) for p in evdir.glob("*.jpg")),
        "note": "These are project-directed transforms layered on top of the FX2-gated base renderer; they are not misrepresented as separate FX2 registry IDs.",
    }
    (out/"IRONFLAME_V5_DIRECTED_EFFECT_EVIDENCE.json").write_text(json.dumps(evidence, indent=2))

    if not usage_pass:
        raise RuntimeError("directed transform usage gate failed")
    if not motion_pass:
        raise RuntimeError(f"motion flow gate failed: {motion}")


def main():
    v4.camera_frame = patched_camera_frame
    v4.scene_effects = patched_scene_effects
    v4.render_scene_frame = patched_render_scene_frame
    v4.main()
    finalize_v5(output_dir_from_argv())


if __name__ == "__main__":
    main()
