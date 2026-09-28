#!/usr/bin/env python3
"""Directed Shifting Cycles rough-cut renderer.

Consumes the ten canonical Recursive Horizon stills plus Shifting Cycles.wav.
Each scene has a distinct motion grammar; this is intentionally not a generic
slideshow/zoompan loop. Output is a review rough cut, not a final master.
"""
from __future__ import annotations
import argparse, json, subprocess
from pathlib import Path

SCENES = [
    ("01_recursive_horizon_anchor.png", 20.5, "emergence"),
    ("02_celestial_orrery_observatory.png", 16.0, "reveal"),
    ("03_golden_orbital_harmony_cityscape.png", 15.5, "rhythm"),
    ("04_golden_causeway_beneath_orbital_rings.png", 25.5, "forward"),
    ("05_celestial_ruins_cloudsea.png", 16.5, "dissolve"),
    ("06_celestial_rings_golden_dawn.png", 21.5, "align"),
    ("07_celestial_golden_ring_metropolis.png", 27.5, "lift"),
    ("08_golden_orbital_metropolis_sunset.png", 30.5, "interlock"),
    ("09_cosmic_arcology_radiant_horizon.png", 44.5, "climax"),
    ("10_concentric_rings_twilight.png", 29.16, "resolve"),
]

def vf(mode: str, dur: float) -> str:
    n = max(1, int(round(dur * 24)))
    base = "scale=1480:833:force_original_aspect_ratio=increase,crop=1480:833"
    motion = {
        "emergence": f"zoompan=z='1.02+0.000035*on':x='(iw-iw/zoom)/2+10*sin(on/38)':y='(ih-ih/zoom)/2+4*cos(on/45)':d={n}:s=1280x720:fps=24,eq=brightness='0.015*sin(t*0.7)':saturation=1.06",
        "reveal": f"zoompan=z='1.08-0.00005*on':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2+12*sin(on/55)':d={n}:s=1280x720:fps=24,eq=contrast=1.04:brightness='0.012*sin(t*1.0)'",
        "rhythm": f"zoompan=z='1.035+0.00002*on':x='(iw-iw/zoom)/2+18*sin(on/28)':y='(ih-ih/zoom)/2+8*sin(on/41)':d={n}:s=1280x720:fps=24,eq=saturation='1.02+0.04*sin(t*1.7)'",
        "forward": f"zoompan=z='1.01+0.00009*on':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2-10*sin(on/60)':d={n}:s=1280x720:fps=24,eq=brightness='0.01+0.012*sin(t*0.9)'",
        "dissolve": f"zoompan=z='1.055+0.00001*on':x='(iw-iw/zoom)/2+6*cos(on/48)':y='(ih-ih/zoom)/2+14*sin(on/65)':d={n}:s=1280x720:fps=24,gblur=sigma='0.3+0.22*(1+sin(t*0.55))',eq=brightness='0.008*sin(t*0.6)'",
        "align": f"zoompan=z='1.06-0.00003*on':x='(iw-iw/zoom)/2+10*sin(on/52)':y='(ih-ih/zoom)/2':d={n}:s=1280x720:fps=24,eq=contrast='1.03+0.02*sin(t*0.8)'",
        "lift": f"zoompan=z='1.04+0.000035*on':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2-18*sin(on/70)':d={n}:s=1280x720:fps=24,eq=brightness='0.012+0.014*sin(t*1.2)':saturation=1.05",
        "interlock": f"zoompan=z='1.045+0.00002*on':x='(iw-iw/zoom)/2+16*sin(on/31)':y='(ih-ih/zoom)/2+10*cos(on/47)':d={n}:s=1280x720:fps=24,eq=contrast='1.04+0.015*sin(t*1.5)':saturation='1.03+0.03*cos(t*1.1)'",
        "climax": f"zoompan=z='1.015+0.000075*on':x='(iw-iw/zoom)/2+12*sin(on/24)':y='(ih-ih/zoom)/2+7*cos(on/33)':d={n}:s=1280x720:fps=24,eq=contrast=1.07:brightness='0.018+0.025*sin(t*1.4)':saturation=1.08",
        "resolve": f"zoompan=z='1.075-0.000045*on':x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2+5*sin(on/65)':d={n}:s=1280x720:fps=24,eq=brightness='0.012*sin(t*0.45)':saturation=1.03",
    }[mode]
    return base + "," + motion + ",format=yuv420p"

def run(cmd):
    subprocess.run(cmd, check=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--media-dir", required=True)
    ap.add_argument("--audio", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--work-dir", default=".render-shifting-cycles")
    args = ap.parse_args()
    media = Path(args.media_dir)
    audio = Path(args.audio)
    out = Path(args.out)
    work = Path(args.work_dir)
    work.mkdir(parents=True, exist_ok=True)
    scene_files = []
    for idx, (name, dur, mode) in enumerate(SCENES, 1):
        target = work / f"scene_{idx:02d}.mp4"
        run(["ffmpeg","-y","-loop","1","-i",str(media/name),"-t",str(dur),
             "-vf",vf(mode,dur),"-an","-c:v","libx264","-preset","medium","-crf","18",
             "-r","24","-pix_fmt","yuv420p",str(target)])
        scene_files.append(target)
    concat = work / "concat.txt"
    concat.write_text("".join(f"file '{p.resolve()}'\n" for p in scene_files), encoding="utf-8")
    video = work / "picture.mp4"
    run(["ffmpeg","-y","-f","concat","-safe","0","-i",str(concat),"-c","copy",str(video)])
    run(["ffmpeg","-y","-i",str(video),"-i",str(audio),"-map","0:v:0","-map","1:a:0",
         "-c:v","copy","-c:a","aac","-b:a","320k","-shortest","-movflags","+faststart",str(out)])
    print(json.dumps({"output":str(out),"scenes":len(scene_files)}, indent=2))

if __name__ == "__main__":
    main()
