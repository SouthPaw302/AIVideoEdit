#!/usr/bin/env python3
"""IronFlame continuity-preserving FX pass.

The Drive reference video is the locked picture authority. This renderer never
replaces source frames; it applies approved AIVideoEdit FX additively and keeps
source edit timing, character identity and environment topology intact.
"""
from __future__ import annotations
import argparse, json, math, subprocess, sys
from pathlib import Path
import cv2
import numpy as np

PROJECT = Path(__file__).resolve().parents[1]
REPO = PROJECT.parents[1]
sys.path.insert(0, str(REPO))
from general.reusable.fx_v2.promoted_effects import apply_effect

ID_TO_NAME = {
    "FX2-ATM-021":"atmospheric_fog",
    "FX2-ATM-022":"forge_motion_furnace_sparks",
    "FX2-ATM-025":"wet_road_rain_reflection",
    "FX2-DISTORT-021":"heat_haze",
    "FX2-LIGHT-023":"firelight_breath",
    "FX2-LIGHT-025":"temporal_grade_shift",
    "FX2-LIGHT-027":"volumetric_light_shafts",
    "FX2-MOTION-024":"localized_micro_warp",
    "FX2-SPATIAL-021":"pseudo_depth_field",
    "FX2-CAMERA-024":"rack_focus_heat_pulse",
}

def load_json(p): return json.loads(Path(p).read_text(encoding="utf-8"))

PLAN = load_json(PROJECT/"production/FX_PLAN.json")
AUDIO = load_json(PROJECT/"analysis/audiomap.json")

def clamp(x,a=0.0,b=1.0): return max(a,min(b,float(x)))

def energy_at(t):
    buckets=AUDIO.get("energy",{}).get("buckets",[])
    if not buckets: return .55
    idx=min(max(int(t),0),len(buckets)-1)
    return clamp(buckets[idx].get("energy",.55))

def transient_at(t):
    best=0.0
    for m in AUDIO.get("energy",{}).get("key_moments",[]):
        c=float(m.get("t",0)); d=abs(float(m.get("delta",0)))
        best=max(best, min(1.0,d*3.0)*math.exp(-((t-c)/0.20)**2))
    return clamp(best)

def active_effects(t):
    for seg in PLAN["segments"]:
        if float(seg["start"]) <= t < float(seg["end"]) or abs(t-float(seg["end"]))<1e-6:
            return seg["effects"]
    return []

def apply_stack(frame,t):
    out=frame
    e=energy_at(t); tr=transient_at(t)
    for fxid,strength in active_effects(t):
        name=ID_TO_NAME[fxid]
        processed=apply_effect(name,out,t=t,duration=8.0,energy=e,transient=tr)
        s=clamp(strength)
        out=cv2.addWeighted(out,1.0-s,processed,s,0)
    return out

def probe_source(path):
    cap=cv2.VideoCapture(str(path))
    fps=cap.get(cv2.CAP_PROP_FPS)
    w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    dur=frames/max(fps,1e-6)
    cap.release()
    if abs(fps-24)>0.01 or (w,h)!=(1280,720) or abs(dur-244.68)>.10:
        raise RuntimeError(f"source authority mismatch fps={fps} size={w}x{h} duration={dur:.3f}")
    return fps,w,h,frames

def render_window(source,start,duration,out_path):
    fps,w,h,_=probe_source(source)
    cap=cv2.VideoCapture(str(source)); cap.set(cv2.CAP_PROP_POS_MSEC,start*1000)
    total=round(duration*fps)
    cmd=["ffmpeg","-y","-hide_banner","-loglevel","error","-f","rawvideo","-pix_fmt","bgr24",
         "-s",f"{w}x{h}","-r","24","-i","-","-an","-c:v","libx264","-preset","veryfast",
         "-crf","18","-pix_fmt","yuv420p",str(out_path)]
    p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    for n in range(total):
        ok,fr=cap.read()
        if not ok: raise RuntimeError(f"source read failed at {start+n/fps:.3f}s")
        t=start+n/fps
        p.stdin.write(apply_stack(fr,t).tobytes())
    cap.release(); p.stdin.close()
    if p.wait()!=0: raise RuntimeError("proof encode failed")

def proof_metrics(source,times):
    cap=cv2.VideoCapture(str(source)); rows=[]
    for t in times:
        cap.set(cv2.CAP_PROP_POS_MSEC,t*1000); ok,src=cap.read()
        if not ok: raise RuntimeError(f"proof frame read failed at {t}")
        fx=apply_stack(src,t)
        rows.append({"t":t,"mean_abs_pixel_delta":round(float(np.mean(cv2.absdiff(src,fx))),6),
                     "effects":[x[0] for x in active_effects(t)]})
    cap.release()
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    ap.add_argument("--proof-only",action="store_true")
    args=ap.parse_args()
    args.out_dir.mkdir(parents=True,exist_ok=True)
    windows=PLAN["proof_windows"] if args.proof_only else [{"start":0.0,"duration":244.68}]
    outs=[]
    for i,w in enumerate(windows,1):
        out=args.out_dir/f"fx_proof_{i:02d}.mp4" if args.proof_only else args.out_dir/"IronFlame_fx_pass_silent.mp4"
        render_window(args.source,float(w["start"]),float(w["duration"]),out); outs.append(str(out))
    times=[float(w["start"])+float(w["duration"])/2 for w in PLAN["proof_windows"]]
    metrics={"schema":"aivideoedit.song-fx-proof.v1","source_is_picture_authority":True,
             "proof_windows":PLAN["proof_windows"],"samples":proof_metrics(args.source,times),
             "rendered_files":outs}
    (args.out_dir/"fx_proof_metrics.json").write_text(json.dumps(metrics,indent=2)+"\n")
    print(json.dumps(metrics,indent=2))

if __name__=="__main__": main()
