#!/usr/bin/env python3
"""Full MainV2 production run for Mountain Noir — After Midnight.

This runner starts from canonical source media, provisions/uses Beat This ONNX,
runs the deterministic FX resolver + precompile gate, renders the living-scene
manifest, applies a bounded canonical FXRuntime pass driven by master-audio
evidence, performs delivery assembly/text, and emits technical/temporal QC.
"""
from __future__ import annotations

import bisect
import hashlib
import json
import math
import os
import shutil
import subprocess
import sys
import time
import urllib.request
import wave
from array import array
from pathlib import Path

import cv2
import numpy as np

REPO = Path(__file__).resolve().parents[2]
PROJECT = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MN_MAINV2_OUT", "/tmp/mountain-noir-mainv2")).resolve()
MEDIA_TAG = "media-mountain-noir-after-midnight"
RELEASE_BASE = f"https://github.com/SouthPaw302/AIVideoEdit/releases/download/{MEDIA_TAG}"

ASSETS = [
    ("assets/audio/Irish_eyes_Remastered.wav", "source__Irish_eyes_Remastered.wav", "8b0ccd2e57a6e683d526d950bd88b42af0f0867b06e3d1b014a2b3131f3cfb1e"),
    ("assets/audio/Leave_It_by_the_Door.wav", "source__Leave_It_by_the_Door.wav", "3354715f5873df14e7d245a1e8f094ff38aade95264f16da3b4bbd71563f4a82"),
    ("assets/audio/Silver_Coin_Remastered.wav", "source__Silver_Coin_Remastered.wav", "6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92"),
    ("assets/audio/El_Viento_trae_tu_nombre_Instrumental.wav", "source__El_Viento_trae_tu_nombre_Instrumental.wav", "8d451360246378db551282c3703add4cd474c9ad3a4c6cf778390ae727820fe0"),
    ("assets/source/irish/IE_L21_ROAD_RAIN_GLASS_16x9_V3.mp4", "source__IE_L21_ROAD_RAIN_GLASS_16x9_V3.mp4", "161dcefb278f9f09eb96f3d96041110b338f9bbe84c87469b547f860eac6821d"),
    ("assets/source/irish/IE_L22_WARM_WINDOW_CANDLE_16x9_V1.mp4", "source__IE_L22_WARM_WINDOW_CANDLE_16x9_V1.mp4", "69814efe52df37fa7db1ba6ae1d89f59be27c91df027c033e831c9e5f58d4af2"),
    ("assets/source/irish/IE_L23_DARK_LAKE_RIDGE_16x9_V2.mp4", "source__IE_L23_DARK_LAKE_RIDGE_16x9_V2.mp4", "9bce0b9fd9f0f3eb29a8d2ea0c7bc75dd3e46ceb72e009f7fe7ee904cfb4cb0a"),
    ("assets/source/silver-coin/01_enchanted_woodland_coin_portrait.png", "source__01_enchanted_woodland_coin_portrait.png", "0783a34aaf19bedc5d98a74beb6a86c4f5a1d881b3c0acd4e9d71240ce119475"),
    ("assets/source/silver-coin/04_twilight_inn_beneath_the_flower_crown.png", "source__04_twilight_inn_beneath_the_flower_crown.png", "81cfa4e39aa944782978ec921bac45078dfe4ad8adb4372f9ba132168cc3a723"),
    ("assets/source/el-viento/shot_03_ocean_memory.png", "source__shot_03_ocean_memory.png", "e8864ecbfb037fa156bfd7817190e98e605653bf77157d7c50a45b46dfc404af"),
    ("assets/source/el-viento/shot_07_veil_of_memory.png", "source__shot_07_veil_of_memory.png", "31adc42ffef33b9166351797c65609c08da9e5427262c9aae54eba953dda3410"),
    ("assets/source/el-viento/02_female_fort_rain.png", "source__02_female_fort_rain.png", "f194c6f8bfac223e9744a8a2b129177f5c6394b60eca7b946d096cc725750315"),
    ("assets/source/el-viento/01_male_fort_sunset.png", "source__01_male_fort_sunset.png", "59b738fbcdcbb0f335d352607f6b5ea24131a441376958f373ba20f8216d26c7"),
    ("assets/source/el-viento/shot_10_glowing_thread.png", "source__shot_10_glowing_thread.png", "fc6c883d778c9b991800eaea79753f2eae5de55549cad3655068b1338d221954"),
]

def run(cmd, *, cwd=REPO, stdout=None, stderr=None):
    print("+", " ".join(map(str, cmd)), flush=True)
    subprocess.run([str(x) for x in cmd], cwd=str(cwd), check=True, stdout=stdout, stderr=stderr)

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def download(url: str, dest: Path, expected: str):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_file() and sha256(dest)==expected:
        return
    req=urllib.request.Request(url, headers={"User-Agent":"AIVideoEdit-MainV2-production/1"})
    with urllib.request.urlopen(req, timeout=180) as r, dest.open("wb") as w:
        shutil.copyfileobj(r,w)
    got=sha256(dest)
    if got!=expected:
        raise RuntimeError(f"hash mismatch for {dest.name}: {got} != {expected}")

def acquire_media():
    for rel,remote,digest in ASSETS:
        download(f"{RELEASE_BASE}/{remote}", PROJECT/rel, digest)
    derived=PROJECT/"assets/derived"
    derived.mkdir(parents=True, exist_ok=True)
    loops=[
        ("IE_L21_ROAD_RAIN_GLASS_16x9_V3.mp4","IE_L21_ROAD_RAIN_GLASS_frame.png"),
        ("IE_L22_WARM_WINDOW_CANDLE_16x9_V1.mp4","IE_L22_WARM_WINDOW_CANDLE_frame.png"),
        ("IE_L23_DARK_LAKE_RIDGE_16x9_V2.mp4","IE_L23_DARK_LAKE_RIDGE_frame.png"),
    ]
    for src,out in loops:
        run(["ffmpeg","-y","-loglevel","error","-ss","2.0","-i",str(PROJECT/"assets/source/irish"/src),"-frames:v","1",str(derived/out)])

def onnx_analysis():
    from general.reusable.tools.music_beat_worker import analyze_music
    evdir=OUT/"onnx"
    evdir.mkdir(parents=True,exist_ok=True)
    tracks=[
        PROJECT/"assets/audio/Irish_eyes_Remastered.wav",
        PROJECT/"assets/audio/Leave_It_by_the_Door.wav",
        PROJECT/"assets/audio/Silver_Coin_Remastered.wav",
        PROJECT/"assets/audio/El_Viento_trae_tu_nombre_Instrumental.wav",
    ]
    results={}
    for p in tracks:
        ev=analyze_music(p)
        if ev.get("engine")!="beat_this_onnx" or "CPUExecutionProvider" not in ev.get("providers",[]):
            raise RuntimeError(f"ONNX authority failed for {p.name}: {ev}")
        (evdir/f"{p.stem}.json").write_text(json.dumps(ev,indent=2)+"\n")
        results[p.name]=ev
    return results

def build_audio():
    aud=PROJECT/"assets/audio"
    master=aud/"Mountain_Noir_After_Midnight_15min_MASTER.wav"
    run([
        "ffmpeg","-y","-loglevel","error",
        "-i",str(aud/"Irish_eyes_Remastered.wav"),
        "-i",str(aud/"Leave_It_by_the_Door.wav"),
        "-i",str(aud/"Silver_Coin_Remastered.wav"),
        "-i",str(aud/"El_Viento_trae_tu_nombre_Instrumental.wav"),
        "-filter_complex_script",str(PROJECT/"AUDIO_RENDER_FILTER.txt"),
        "-map","[master]","-c:a","pcm_s16le",str(master)
    ])
    run(["ffmpeg","-y","-loglevel","error","-i",str(master),"-c:a","aac","-b:a","256k","-ar","48000",str(aud/"Mountain_Noir_After_Midnight_15min_MASTER.m4a")])
    return master

def resolve_and_gate():
    from general.reusable.fx_v2.fx_resolver import resolve
    ctx=json.loads((PROJECT/"FX_RESOLUTION_CONTEXT.json").read_text())
    registry_path=REPO/"general/reusable/fx_v2/registry.json"
    registry=json.loads(registry_path.read_text())
    resolution=resolve(ctx,max_effects=6)
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/"FX_RESOLUTION.json").write_text(json.dumps(resolution,indent=2)+"\n")
    effects=[]; transitions=[]; applicable=[]
    for item in resolution.get("effects",[]):
        eid=item["id"]
        rec=(registry.get("effects") or {}).get(eid,{})
        kind=(rec.get("implementation") or {}).get("kind")
        if kind=="runtime_transition":
            transitions.append({"id":eid})
        else:
            effects.append({"id":eid})
            if kind=="runtime_apply":
                applicable.append(eid)
    if not effects and not transitions:
        raise RuntimeError("FX resolver produced no gateable effects")
    render_inputs=[
        "projects/mountain-noir-after-midnight/LIVING_SCENE_MANIFEST.json",
        "projects/mountain-noir-after-midnight/FX_RESOLUTION_CONTEXT.json",
        "projects/mountain-noir-after-midnight/AUDIO_RENDER_FILTER.txt",
        "projects/mountain-noir-after-midnight/run_mainv2_full.py",
    ]+[f"projects/mountain-noir-after-midnight/{rel}" for rel,_,_ in ASSETS]
    req={
        "schema":"aivideoedit.fx-requirements.v2",
        "project":"mountain-noir-after-midnight-mainv2",
        "runtime":registry.get("runtime"),
        "seed":302,
        "effects":effects,
        "transitions":transitions,
        "render_inputs":render_inputs,
    }
    req_path=OUT/"FX_REQUIREMENTS.json"
    req_path.write_text(json.dumps(req,indent=2)+"\n")
    lock=OUT/"FX_LOCK.json"
    gate=REPO/"general/reusable/fx_v2/precompile_gate.py"
    run([sys.executable,str(gate),"--manifest",str(req_path),"--lock-out",str(lock)])
    run([sys.executable,str(gate),"--manifest",str(req_path),"--verify-lock",str(lock)])
    return resolution, applicable

def analyze_master(master: Path):
    from general.reusable.tools.music_beat_worker import analyze_music
    ev=analyze_music(master)
    if ev.get("engine")!="beat_this_onnx":
        raise RuntimeError("assembled master did not use Beat This ONNX")
    (OUT/"onnx/master_15min.json").write_text(json.dumps(ev,indent=2)+"\n")
    return ev

def rms_envelope(master: Path, step_seconds=.05):
    vals=[]
    with wave.open(str(master),"rb") as wf:
        sr=wf.getframerate(); ch=wf.getnchannels(); sw=wf.getsampwidth()
        if sw!=2: raise RuntimeError("master WAV must be PCM16")
        n=max(1,int(sr*step_seconds))
        while True:
            raw=wf.readframes(n)
            if not raw: break
            a=array("h"); a.frombytes(raw)
            if not a: break
            # stereo/mono both reduce to frame-energy evidence
            rms=math.sqrt(sum(float(x)*float(x) for x in a)/len(a))/32768.0
            vals.append(rms)
    if not vals: return [0.0],step_seconds
    lo=float(np.percentile(vals,10)); hi=float(np.percentile(vals,95))
    norm=[max(0.0,min(1.0,(x-lo)/(hi-lo+1e-8))) for x in vals]
    return norm,step_seconds

def render_base(master: Path):
    base=OUT/"living_base.mp4"
    run([
        sys.executable,
        str(REPO/"general/reusable/painterly-motion/render_living_painting.py"),
        "--manifest",str(PROJECT/"LIVING_SCENE_MANIFEST.json"),
        "--output",str(base),
        "--width","960","--height","540","--fps","24"
    ])
    return base

def canonical_fx_pass(base: Path, master: Path, master_ev: dict, applicable: list[str]):
    from general.reusable.fx_v2.runtime import FXRuntime, FXContext
    manifest=json.loads((PROJECT/"LIVING_SCENE_MANIFEST.json").read_text())
    scenes=manifest["scenes"]
    starts=[]; ends=[]
    for s in scenes:
        st=float(s.get("start_seconds", starts[-1] if starts else 0.0))
        starts.append(st); ends.append(st+float(s["duration"]))
    beats=sorted(float(x) for x in master_ev.get("beat_positions_seconds",[]))
    env,env_step=rms_envelope(master)
    rt=FXRuntime(seed=302)
    cap=cv2.VideoCapture(str(base))
    fps=cap.get(cv2.CAP_PROP_FPS) or 24.0
    w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out=OUT/"canonical_fx.mp4"
    proc=subprocess.Popen([
        "ffmpeg","-y","-loglevel","error","-f","rawvideo","-pix_fmt","bgr24",
        "-s",f"{w}x{h}","-r",str(fps),"-i","-",
        "-c:v","libx264","-preset","veryfast","-crf","19","-pix_fmt","yuv420p",str(out)
    ],stdin=subprocess.PIPE)
    frame=0
    # bounded runtime application: at most one canonical single-frame FX per frame.
    priority=["FX2-ATM-002","FX2-ATM-001","FX2-MOTION-003","FX2-LIGHT-001","FX2-LIGHT-002","FX2-SURFACE-001"]
    available=[x for x in priority if x in applicable]
    while True:
        ok,bgr=cap.read()
        if not ok: break
        t=frame/fps
        si=max(0,min(len(scenes)-1,bisect.bisect_right(starts,t)-1))
        s=scenes[si]; local=max(0.0,t-starts[si]); dur=float(s["duration"])
        ei=min(len(env)-1,max(0,int(t/env_step)))
        energy=env[ei]
        j=bisect.bisect_left(beats,t)
        d=min(abs(t-beats[j]) if j<len(beats) else 999, abs(t-beats[j-1]) if j>0 else 999)
        transient=math.exp(-((d/.11)**2)) if d<.4 else 0.0
        ctx=FXContext(t=local,duration=dur,frame_index=frame,fps=fps,energy=energy,transient=transient,brightness=energy)
        eid=None
        fxnames=set(s.get("effects",[]))
        if "reflection" in fxnames and "FX2-MOTION-003" in available: eid="FX2-MOTION-003"
        elif ("particles" in fxnames or "atmosphere" in fxnames) and "FX2-ATM-002" in available and "RAIN" in s.get("image","").upper(): eid="FX2-ATM-002"
        elif ("firelight" in fxnames or "haze" in fxnames) and "FX2-ATM-001" in available: eid="FX2-ATM-001"
        elif available: eid=available[si % len(available)]
        if eid:
            strength=.18 if eid!="FX2-ATM-002" else .14
            bgr=rt.apply(bgr,{"id":eid,"strength":strength},ctx)
        proc.stdin.write(bgr.tobytes())
        frame+=1
    cap.release()
    proc.stdin.close()
    rc=proc.wait()
    if rc: raise RuntimeError(f"canonical FX encode failed: {rc}")
    return out

def assemble_delivery(video: Path, master: Path):
    final=OUT/"Mountain_Noir_After_Midnight_MAINV2_720p.mp4"
    font="/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
    filters=[
        "scale=1280:720:flags=lanczos",
        f"drawtext=fontfile={font}:text='MOUNTAIN NOIR':fontcolor=0xE8D8B6@0.58:fontsize=22:x=w-text_w-48:y=h-text_h-42:shadowcolor=black@0.55:shadowx=1:shadowy=1",
        f"drawtext=fontfile={font}:text='MOUNTAIN NOIR':fontcolor=0xE8D8B6@0.88:fontsize=54:x=(w-text_w)/2:y=h*0.36:shadowcolor=black@0.60:shadowx=2:shadowy=2:enable='between(t,1,27)'",
        f"drawtext=fontfile={font}:text='AFTER MIDNIGHT':fontcolor=0xE8D8B6@0.78:fontsize=28:x=(w-text_w)/2:y=h*0.47:shadowcolor=black@0.58:shadowx=1:shadowy=1:enable='between(t,3,27)'",
        f"drawtext=fontfile={font}:text='LEAVE IT BY THE DOOR':fontcolor=0xE8D8B6@0.74:fontsize=28:x=(w-text_w)/2:y=h*0.82:shadowcolor=black@0.58:shadowx=1:shadowy=1:enable='between(t,184.12,194.12)'",
        f"drawtext=fontfile={font}:text='SILVER COIN':fontcolor=0xE8D8B6@0.74:fontsize=28:x=(w-text_w)/2:y=h*0.82:shadowcolor=black@0.58:shadowx=1:shadowy=1:enable='between(t,379.96,389.96)'",
        f"drawtext=fontfile={font}:text='EL VIENTO TRAE TU NOMBRE':fontcolor=0xE8D8B6@0.74:fontsize=26:x=(w-text_w)/2:y=h*0.79:shadowcolor=black@0.58:shadowx=1:shadowy=1:enable='between(t,584.4,594.4)'",
        f"drawtext=fontfile={font}:text='INSTRUMENTAL':fontcolor=0xE8D8B6@0.62:fontsize=20:x=(w-text_w)/2:y=h*0.85:shadowcolor=black@0.58:shadowx=1:shadowy=1:enable='between(t,584.4,594.4)'",
        "fps=24",
    ]
    run([
        "ffmpeg","-y","-loglevel","error","-i",str(video),"-i",str(master),
        "-map","0:v:0","-map","1:a:0","-vf",",".join(filters),
        "-t","900","-c:v","libx264","-preset","veryfast","-crf","18","-pix_fmt","yuv420p",
        "-c:a","aac","-b:a","256k","-ar","48000","-movflags","+faststart",str(final)
    ])
    return final

def qc(final: Path):
    q=OUT/"qc"; q.mkdir(parents=True,exist_ok=True)
    with (q/"ffprobe.json").open("w") as f:
        run(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(final)],stdout=f)
    with (q/"blackdetect.log").open("w") as f:
        subprocess.run(["ffmpeg","-hide_banner","-i",str(final),"-vf","blackdetect=d=0.3:pix_th=0.10","-an","-f","null","-"],stdout=f,stderr=subprocess.STDOUT,check=False)
    with (q/"freezedetect.log").open("w") as f:
        subprocess.run(["ffmpeg","-hide_banner","-i",str(final),"-vf","freezedetect=n=0.001:d=3","-an","-f","null","-"],stdout=f,stderr=subprocess.STDOUT,check=False)
    run([
        sys.executable,str(REPO/"general/reusable/painterly-motion/video_fx/temporal_qc.py"),
        str(final),"--json-out",str(q/"temporal_qc.json"),
        "--sample-fps","2","--timeline",str(PROJECT/"analysis/qc/MN_TEMPORAL_QC_TIMELINE.json"),
        "--transition-window","1.0"
    ])
    run([
        "ffmpeg","-y","-loglevel","error","-i",str(final),
        "-vf","fps=1/75,scale=320:180,tile=4x3","-frames:v","1",str(q/"contact_sheet.jpg")
    ])
    probe=json.loads((q/"ffprobe.json").read_text())
    dur=float(probe.get("format",{}).get("duration",0))
    black=(q/"blackdetect.log").read_text(errors="replace")
    temporal=json.loads((q/"temporal_qc.json").read_text())
    result={
        "schema":"aivideoedit.mainv2-full-production-result.v1",
        "result":"PASS" if abs(dur-900.0)<0.25 and "black_start:" not in black else "FAIL",
        "duration_seconds":dur,
        "sha256":sha256(final),
        "video":final.name,
        "onnx_master_engine":json.loads((OUT/"onnx/master_15min.json").read_text()).get("engine"),
        "fx_lock":"FX_LOCK.json",
        "temporal_qc":{
            "risk_count":temporal.get("risk_count"),
            "unexplained_risk_count":temporal.get("unexplained_risk_count"),
        }
    }
    (OUT/"result.json").write_text(json.dumps(result,indent=2)+"\n")
    if result["result"]!="PASS":
        raise RuntimeError(f"final QC failed: {result}")
    return result

def main():
    started=time.time()
    OUT.mkdir(parents=True,exist_ok=True)
    acquire_media()
    onnx_analysis()
    master=build_audio()
    resolution,applicable=resolve_and_gate()
    master_ev=analyze_master(master)
    base=render_base(master)
    fxvideo=canonical_fx_pass(base,master,master_ev,applicable)
    final=assemble_delivery(fxvideo,master)
    result=qc(final)
    result["elapsed_seconds"]=round(time.time()-started,2)
    result["resolved_fx"]=[x["id"] for x in resolution.get("effects",[])]
    (OUT/"result.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
