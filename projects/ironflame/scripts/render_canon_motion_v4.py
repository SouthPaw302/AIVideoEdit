#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
import wave
from pathlib import Path

import cv2
import numpy as np

FPS = 24.0
INTERNAL_W = 960
INTERNAL_H = 540
OUT_W = 1280
OUT_H = 720

SCENE_FOCUS = [
    (0.53,0.55,0.24,0.34), (0.52,0.55,0.25,0.36), (0.50,0.55,0.23,0.34),
    (0.53,0.46,0.22,0.29), (0.53,0.56,0.24,0.34), (0.52,0.55,0.23,0.35),
    (0.50,0.55,0.24,0.35), (0.50,0.50,0.23,0.33), (0.50,0.56,0.24,0.35),
    (0.50,0.56,0.25,0.35), (0.50,0.54,0.24,0.34), (0.61,0.46,0.23,0.31),
]
SPATIAL_SCENES = {0, 5, 8, 11}

# Same mixed vocabulary that survived the earlier IronFlame transition proofs.
TRANSITION_MATRIX = [
    "FX2-TRANS-003", "FX2-TRANS-001", "FX2-TRANS-001", "FX2-TRANS-003",
    "FX2-TRANS-001", "FX2-TRANS-003", "FX2-TRANS-001", "FX2-TRANS-003",
    "FX2-TRANS-003", "FX2-TRANS-001", "FX2-TRANS-003",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fit_cover(img: np.ndarray, w: int, h: int) -> np.ndarray:
    ih, iw = img.shape[:2]
    s = max(w / iw, h / ih)
    nw, nh = int(round(iw * s)), int(round(ih * s))
    r = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_LANCZOS4)
    x0 = max(0, (nw - w) // 2)
    y0 = max(0, (nh - h) // 2)
    return r[y0:y0+h, x0:x0+w].copy()


def read_wav_mono(path: Path):
    with wave.open(str(path), "rb") as wf:
        if wf.getsampwidth() != 2:
            raise RuntimeError("expected PCM16 WAV")
        sr = wf.getframerate(); ch = wf.getnchannels(); n = wf.getnframes()
        raw = wf.readframes(n)
    a = np.frombuffer(raw, dtype="<i2").astype(np.float32) / 32768.0
    if ch > 1:
        a = a.reshape(-1, ch).mean(axis=1)
    return a, sr


def normalize_percentile(x: np.ndarray, lo=5, hi=95):
    a, b = np.percentile(x, [lo, hi])
    return np.clip((x - a) / (b - a + 1e-9), 0.0, 1.0)


def analyze_audio(path: Path, frames: int):
    mono, sr = read_wav_mono(path)
    hop = int(round(sr / FPS))
    rms = np.zeros(frames, np.float32)
    flux = np.zeros(frames, np.float32)
    low = np.zeros(frames, np.float32)
    mid = np.zeros(frames, np.float32)
    high = np.zeros(frames, np.float32)
    prev = None
    window = np.hanning(hop).astype(np.float32)
    freqs = np.fft.rfftfreq(hop, 1.0 / sr)
    il = freqs < 180
    im = (freqs >= 180) & (freqs < 2200)
    ih = freqs >= 2200
    for i in range(frames):
        s = i * hop
        seg = mono[s:s+hop]
        if len(seg) < hop:
            seg = np.pad(seg, (0, hop-len(seg)))
        rms[i] = math.sqrt(float(np.mean(seg * seg)) + 1e-12)
        spec = np.abs(np.fft.rfft(seg * window)).astype(np.float32)
        mag = spec / (float(spec.sum()) + 1e-9)
        if prev is not None:
            flux[i] = float(np.maximum(mag - prev, 0).sum())
        prev = mag
        p = spec * spec
        low[i] = float(p[il].sum()); mid[i] = float(p[im].sum()); high[i] = float(p[ih].sum())
    return {
        "rms": normalize_percentile(rms),
        "onset": normalize_percentile(flux),
        "low": normalize_percentile(np.log1p(low)),
        "mid": normalize_percentile(np.log1p(mid)),
        "high": normalize_percentile(np.log1p(high)),
        "sample_rate": sr,
    }


def scene_microcuts(s: int, e: int, energy: np.ndarray, onset: np.ndarray):
    cuts = [s]
    cur = s
    mean_e = float(np.mean(energy[s:e])) if e > s else 0.0
    target_sec = 3.9 if mean_e > 0.58 else (4.6 if mean_e > 0.34 else 5.4)
    target = int(target_sec * FPS)
    min_gap = int(3.0 * FPS)
    max_gap = int(6.4 * FPS)
    search = int(1.05 * FPS)
    while e - cur > max_gap:
        wanted = cur + target
        a = max(cur + min_gap, wanted - search)
        b = min(e - min_gap, wanted + search)
        if b > a:
            local = onset[a:b]
            c = a + int(np.argmax(local))
            if onset[c] < 0.38:
                c = wanted
        else:
            c = wanted
        c = max(cur + min_gap, min(c, cur + max_gap, e - min_gap))
        if c <= cur:
            break
        cuts.append(c); cur = c
    if cuts[-1] != e:
        cuts.append(e)
    return cuts


def authored_depth(shape, scene_idx: int):
    h, w = shape[:2]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    # Explicit scene-space layers: far upper field, middle architecture/terrain,
    # foreground floor/ground, and a feathered protagonist layer.
    depth = 0.18 + 0.22 * (yy / max(1, h-1))
    cx, cy, rx, ry = SCENE_FOCUS[scene_idx]
    d = ((xx - cx*w)/(rx*w+1e-6))**2 + ((yy-cy*h)/(ry*h+1e-6))**2
    subj = np.clip(1.0 - (d - 0.65) / 0.55, 0, 1)
    subj = cv2.GaussianBlur(subj, (0,0), 15)
    depth = depth * (1 - 0.62*subj) + 0.86 * (0.62*subj)
    fg = np.clip((yy/h - 0.68) / 0.30, 0, 1)
    depth = np.maximum(depth, 0.48 + 0.20*fg)
    depth = cv2.GaussianBlur(depth, (0,0), 4.0)
    return np.clip(depth, 0, 1).astype(np.float32)


def camera_frame(base, global_i, scene_idx, cuts, energy):
    k = max(0, min(len(cuts)-2, bisect.bisect_right(cuts, global_i)-1))
    a, b = cuts[k], cuts[k+1]
    q = (global_i - a) / max(1, b - a - 1)
    # Alternating push/pull and lateral direction makes each derived shot read differently.
    direction = -1 if (scene_idx + k) % 2 else 1
    push = (scene_idx + k) % 3 != 1
    z0, z1 = (1.025, 1.090) if push else (1.095, 1.035)
    z = z0 + (z1-z0) * (q*q*(3-2*q)) + 0.008*float(energy[global_i])
    dx = direction * (0.012 + 0.008 * math.sin((scene_idx+1)*1.7)) * INTERNAL_W * (q-0.5)
    dy = (0.008 * INTERNAL_H) * math.sin((q-0.5)*math.pi)
    rot = direction * (0.18 + 0.30*float(energy[global_i])) * math.sin(math.pi*q)
    M = cv2.getRotationMatrix2D((INTERNAL_W/2, INTERNAL_H/2), rot, z)
    M[0,2] += dx; M[1,2] += dy
    return cv2.warpAffine(base, M, (INTERNAL_W, INTERNAL_H), flags=cv2.INTER_CUBIC,
                          borderMode=cv2.BORDER_REFLECT_101), k, q


def scene_effects(idx: int, e: float):
    # Approved FX2 runtime IDs only. Strength is song-shaped but bounded.
    effects = [
        {"id":"FX2-MOTION-002", "strength":0.66 + 0.34*e, "roi":[0,0,1,1]},
        {"id":"FX2-LIGHT-001", "strength":0.52 + 0.42*e, "roi":[0,0,1,1]},
        {"id":"FX2-LIGHT-002", "strength":0.55 + 0.48*e, "origin":[0.74,0.18]},
        {"id":"FX2-SURFACE-001", "strength":0.30, "key":f"ironflame-scene-{idx+1:02d}"},
    ]
    if idx in (0,1,6):
        effects += [{"id":"FX2-ATM-002", "strength":0.36+0.26*e, "roi":[0,0,1,1]}]
    if idx in (0,1,3,4,5,6,7,8,9,10):
        effects += [{"id":"FX2-ATM-001", "strength":0.24+0.26*e, "roi":[0,0,1,1]}]
    if idx in (2,9,11):
        effects += [{"id":"FX2-FIRE-002", "strength":0.38+0.48*e, "roi":[0,0,1,1]}]
    if idx in (2,9):
        effects += [{"id":"FX2-FIRE-001", "strength":0.34+0.48*e,
                    "roi":[0.03,0.48,0.40,0.98] if idx==2 else [0.58,0.45,0.97,0.98]}]
    if idx == 8:
        effects += [{"id":"FX2-MOTION-003", "strength":0.45+0.28*e, "roi":[0,0.62,1,1], "reflect":True}]
    return effects


def render_scene_frame(base, idx, gi, scene_start, scene_end, cuts, features, runtime, lp, depth, metrics):
    e = float(features["rms"][gi]); onset = float(features["onset"][gi])
    frame, micro_idx, micro_q = camera_frame(base, gi, idx, cuts, features["rms"])
    # Genuine FX2-SPATIAL-004 code path on four selected scenes using a provided,
    # scene-authored layered depth map; never use living_parallax's fallback here.
    if idx in SPATIAL_SCENES and depth is not None:
        ph = ((gi - scene_start) / max(1, scene_end-scene_start)) * math.tau
        dx = math.sin(ph) * 0.62
        dy = math.sin(ph*2.0) * 0.20
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
        rgb = lp.warp(rgb, depth, dx, dy, 0.020 + 0.006*e)
        frame = cv2.cvtColor((rgb*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
        metrics["FX2-SPATIAL-004"]["frames"] += 1
    cx, cy, rx, ry = SCENE_FOCUS[idx]
    protect = runtime.ellipse_mask(frame.shape, (cx,cy), (rx*0.72,ry*0.62), blur=25,
                                   key=f"protect:{idx}")
    ctx = FXContext(t=gi/FPS, duration=(scene_end-scene_start)/FPS, frame_index=gi,
                    fps=FPS, energy=e, transient=onset, brightness=float(features["high"][gi]))
    for fx in scene_effects(idx, e):
        before = frame
        frame = runtime.apply(frame, fx, ctx, protect=protect if fx["id"]=="FX2-MOTION-002" else None)
        if gi % 24 == 0:
            d = float(np.mean(np.abs(frame.astype(np.float32)-before.astype(np.float32))))
            m = metrics[fx["id"]]; m["samples"] += 1; m["delta_sum"] += d; m["delta_max"] = max(m["delta_max"], d)
        metrics[fx["id"]]["frames"] += 1
    return frame


def parse_qc(stderr: str):
    black = len(re.findall(r"black_start:", stderr))
    freeze = len(re.findall(r"freeze_start:", stderr))
    return black, freeze


def make_contact(frames, out: Path):
    thumbs=[]
    for f in frames:
        t=cv2.resize(f,(320,180),interpolation=cv2.INTER_AREA)
        thumbs.append(t)
    while len(thumbs)<12:
        thumbs.append(np.zeros((180,320,3),np.uint8))
    rows=[np.hstack(thumbs[r*4:(r+1)*4]) for r in range(3)]
    cv2.imwrite(str(out), np.vstack(rows))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=Path.cwd())
    ap.add_argument("--audio", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, required=True)
    ap.add_argument("--ffmpeg", default="ffmpeg")
    args=ap.parse_args()
    root=args.repo.resolve(); out=args.output_dir.resolve(); out.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(root))
    from general.reusable.fx_v2.runtime import FXRuntime, FXContext
    lp_path=root/"general/reusable/generative-engine/spatial/living_parallax.py"
    spec=importlib.util.spec_from_file_location("ironflame_living_parallax",lp_path)
    lp=importlib.util.module_from_spec(spec); assert spec and spec.loader; spec.loader.exec_module(lp)

    manifest=json.loads((root/"projects/ironflame/ASSET_MANIFEST.json").read_text())
    duration=float(manifest["source_audio"]["duration_seconds"])
    expected_audio=manifest["source_audio"]["sha256"]
    actual_audio=sha256(args.audio)
    if actual_audio != expected_audio:
        raise RuntimeError(f"canonical audio hash mismatch {actual_audio}")
    total_frames=int(math.ceil(duration*FPS))
    features=analyze_audio(args.audio,total_frames)

    stills=[]; starts=[]; ends=[]
    for x in manifest["production_stills"]:
        p=root/"projects/ironflame"/x["path"]
        im=cv2.imread(str(p),cv2.IMREAD_COLOR)
        if im is None: raise FileNotFoundError(p)
        stills.append(fit_cover(im,INTERNAL_W,INTERNAL_H))
        starts.append(int(round(float(x["start"])*FPS)))
        ends.append(min(total_frames,int(round(float(x["end"])*FPS))))
    ends[-1]=total_frames

    cuts=[scene_microcuts(starts[i],ends[i],features["rms"],features["onset"]) for i in range(12)]
    depths=[None]*12
    depth_dir=out/"depth_maps"; depth_dir.mkdir(exist_ok=True)
    for idx in SPATIAL_SCENES:
        d=authored_depth(stills[idx].shape,idx); depths[idx]=d
        cv2.imwrite(str(depth_dir/f"shot{idx+1:02d}_authored_depth.png"),(d*255).astype(np.uint8))

    runtime=FXRuntime(seed=302)
    ids=["FX2-MOTION-002","FX2-MOTION-003","FX2-ATM-001","FX2-ATM-002","FX2-FIRE-001","FX2-FIRE-002","FX2-LIGHT-001","FX2-LIGHT-002","FX2-SURFACE-001","FX2-SPATIAL-004"]
    metrics={k:{"frames":0,"samples":0,"delta_sum":0.0,"delta_max":0.0} for k in ids}
    transition_counts={"FX2-TRANS-001":0,"FX2-TRANS-003":0}

    output=out/"IRONFLAME_V4_CANON_MOTION_720p24.mp4"
    cmd=[args.ffmpeg,"-y","-loglevel","error","-f","rawvideo","-pix_fmt","bgr24","-s",f"{INTERNAL_W}x{INTERNAL_H}","-r",str(FPS),"-i","-",
         "-i",str(args.audio),"-vf",f"scale={OUT_W}:{OUT_H}:flags=lanczos,format=yuv420p","-c:v","libx264","-preset","fast","-crf","18",
         "-c:a","aac","-b:a","256k","-ar","48000","-ac","2","-shortest","-movflags","+faststart",str(output)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    assert proc.stdin is not None
    contact=[None]*12
    scene_idx=0
    for gi in range(total_frames):
        while scene_idx < 11 and gi >= ends[scene_idx]:
            scene_idx += 1
        idx=scene_idx
        frame=render_scene_frame(stills[idx],idx,gi,starts[idx],ends[idx],cuts[idx],features,runtime,lp,depths[idx],metrics)
        # Transition occupies the tail of a scene and hands completely to the next scene.
        if idx < 11:
            tid=TRANSITION_MATRIX[idx]
            n=12 if tid=="FX2-TRANS-003" else 6
            if gi >= ends[idx]-n:
                p=(gi-(ends[idx]-n))/max(1,n-1)
                # Sample the incoming scene from its own opening transition frames rather than
                # extrapolating its camera path backward into the outgoing scene's time range.
                ngi=min(ends[idx+1]-1, starts[idx+1] + (gi-(ends[idx]-n)))
                nxt=render_scene_frame(stills[idx+1],idx+1,ngi,starts[idx+1],ends[idx+1],cuts[idx+1],features,runtime,lp,depths[idx+1],metrics)
                if tid=="FX2-TRANS-003":
                    frame=runtime.light_peak_handoff(frame,nxt,p,origin=(0.74,0.18),strength=0.42)
                else:
                    frame=runtime.pigment_gate(frame,nxt,p,key=f"if-{idx:02d}-{idx+1:02d}",softness=5.8)
                transition_counts[tid]+=1
        # Gentle authored head/tail fade only; not counted as a scene transition.
        if gi < 12:
            frame=(frame.astype(np.float32)*(gi/11.0)).astype(np.uint8)
        if gi >= total_frames-12:
            frame=(frame.astype(np.float32)*((total_frames-1-gi)/11.0)).astype(np.uint8)
        mid=(starts[idx]+ends[idx])//2
        if contact[idx] is None and gi>=mid:
            contact[idx]=frame.copy()
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    if proc.wait()!=0: raise RuntimeError("ffmpeg master encode failed")
    make_contact([x if x is not None else np.zeros((INTERNAL_H,INTERNAL_W,3),np.uint8) for x in contact],out/"IRONFLAME_V4_CONTACT_12.jpg")

    # Normalize metrics.
    for k,m in metrics.items():
        m["sample_delta_mean"]=(m["delta_sum"]/m["samples"]) if m["samples"] else 0.0
        m.pop("delta_sum",None)

    probe=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels","-of","json",str(output)],text=True))
    qc_run=subprocess.run([args.ffmpeg,"-v","info","-i",str(output),"-vf","blackdetect=d=0.5:pix_th=0.10,freezedetect=n=-50dB:d=1.5","-an","-f","null","-"],capture_output=True,text=True)
    black,freeze=parse_qc(qc_run.stderr)
    qc={
        "title":"IronFlame V4 Canon Motion",
        "status":"DELIVERY_CANDIDATE" if black==0 and freeze==0 else "QC_FAIL",
        "master":output.name,
        "sha256":sha256(output),
        "audio_sha256":actual_audio,
        "duration_target":duration,
        "fps":FPS,
        "resolution":[OUT_W,OUT_H],
        "scene_count":12,
        "derived_microshot_count":int(sum(max(0,len(c)-1) for c in cuts)),
        "microshot_boundaries_seconds":[[round(x/FPS,3) for x in c] for c in cuts],
        "transition_counts":transition_counts,
        "effect_metrics":metrics,
        "spatial":{
            "id":"FX2-SPATIAL-004",
            "scenes":[i+1 for i in sorted(SPATIAL_SCENES)],
            "depth_mode":"provided scene-authored layered depth maps; synthetic fallback not used",
            "claim":"2.5D image-space depth warp only; no NeRF/3DGS claim"
        },
        "black_events":black,
        "freeze_events_ge_1_5s":freeze,
        "ffprobe":probe,
    }
    (out/"IRONFLAME_V4_FINAL_QC.json").write_text(json.dumps(qc,indent=2))
    (out/"IRONFLAME_V4_CONTROL_SUMMARY.json").write_text(json.dumps({
        "frames":total_frames,"sample_rate":features["sample_rate"],
        "rms_mean":float(np.mean(features["rms"])),"onset_mean":float(np.mean(features["onset"])),
        "rms_peak":float(np.max(features["rms"])),"onset_peak":float(np.max(features["onset"]))
    },indent=2))
    if black or freeze:
        raise RuntimeError(f"export QC failed: black={black} freeze={freeze}")
    print(json.dumps(qc,indent=2))

if __name__=="__main__":
    main()
