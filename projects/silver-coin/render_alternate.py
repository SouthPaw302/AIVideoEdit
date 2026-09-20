#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, subprocess, shutil
from pathlib import Path

EXPECTED = {
"Silver Coin (Remastered).wav":"6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92",
"V8_FX01_forest_breath_hair_garland.mp4":"99ea7fcb651485a6c58c72deebb762ca51b6b9a75e5b4b7321784842422f3f0c",
"V8_FX02_coin_glint.mp4":"35cfd8e1af3bf690c70fa1baab0a3d511aefd8153eeab932991a1ed8dee947f8",
"V8_FX03_tavern_firelight_smoke.mp4":"fd06f0a65bf2a59d3331b8511d7f3c309676f5ede6ead9e038510c2fb1d4303a",
"V8_FX04_fiddler_impact.mp4":"a80a20c303952fdae80880cc8ae5b2622dbe535a06ff0cb6665992131089008b",
"V8_FX05_communal_crowd_sway.mp4":"c7f1c296673ba9e927f6ba49cb51654b534727bbe8622c77639389d36eed9845",
"V8_FX06_lightning_wet_reflection.mp4":"5acb928a337c499fdf240e94371dd37ad6b128cf5749e5bc010e83fe07f06ef4",
"V8_FX07_gaussian_light_shafts.mp4":"bf71a7bdeb1c1e172ae5a5676d888fa95153bc01db05e79646cea31c3edba90a",
"V8_FX08_fog_pigment_travel.mp4":"88a24b139f14ced56d97f118ae68d07a9a8427f5eb5c60ce8da60e77000c4588",
"V8_FX09_depth_parallax_scenegraph.mp4":"3c89782e20127d77eb5015ce8dd5d3b4773ca8350e26cfa12046e0fda6f4e51b",
"V8_FX10_recursive_coin_portal.mp4":"5dda3d17930a8fd9e6d4f5d1b3954ce904fee28a645be3d2cd0a79e6cafb4e82",
"V8_FX11_temporal_dusk_to_night.mp4":"5136caa8722a8c4db8caeadc41f11c7cbaea0ca943ba6117dfc3b7fe5ad92d7d",
"V8_FX13_workers_sunset_procession.mp4":"2c7873ae5576a83f7467cc2ce231d26b2a5f99d263bea01822916e31f9ee19ed",
"V8_FX14_clap_rhythm_response.mp4":"5f685c4b5aae58a65ec0b3dfbdeca5372359d79b290d975bee015af2d05a09de",
"V8_FX15_shadow_wipe.mp4":"4d12adb4097143c7834e159d2356b37ec0484e5e29b72545512ee0c6a1d021c6",
"V8_FX16_candle_heat_haze.mp4":"96fb489f5147bb71a50fc148dd5aa9d3dfdc347645ddfe908326517a3a69f88b"
}

def sha256(p: Path):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

def run(cmd):
    subprocess.run(cmd,check=True)

def probe_duration(p: Path):
    x=subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nw=1:nk=1",str(p)],text=True)
    return float(x.strip())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--project-dir",required=True)
    ap.add_argument("--media-root",required=True)
    ap.add_argument("--out-dir",required=True)
    args=ap.parse_args()
    project=Path(args.project_dir)
    media=Path(args.media_root)
    out=Path(args.out_dir)
    out.mkdir(parents=True,exist_ok=True)
    plan=json.loads((project/"ASSEMBLY_PLAN.json").read_text())
    for name,expected in EXPECTED.items():
        p=media/name
        if not p.is_file(): raise SystemExit(f"missing input: {p}")
        got=sha256(p)
        if got!=expected: raise SystemExit(f"hash mismatch: {name} {got} != {expected}")
    work=out/"segments"
    work.mkdir(exist_ok=True)
    shot_outputs=[]
    for shot in plan["shots"]:
        target=shot["end"]-shot["start"]
        parts=[]
        remain=target
        idx=0
        while remain>0.001:
            src=media/shot["clips"][idx%len(shot["clips"])]
            dur=min(4.0,remain)
            part=work/f'{shot["id"]}_{idx:02d}.mp4'
            vf=["fps=24","scale=1280:720:flags=lanczos","setsar=1"]
            if idx>=len(shot["clips"]) and idx%2==1:
                vf.insert(0,"reverse")
            run(["ffmpeg","-y","-v","error","-i",str(src),"-t",f"{dur:.6f}","-an","-vf",",".join(vf),"-c:v","libx264","-preset","medium","-crf","16","-pix_fmt","yuv420p",str(part)])
            parts.append(part)
            remain-=dur
            idx+=1
        concat=work/f'{shot["id"]}_concat.txt'
        concat.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts))
        shot_out=work/f'{shot["id"]}.mp4'
        run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",str(concat),"-t",f"{target:.6f}","-an","-c","copy",str(shot_out)])
        shot_outputs.append(shot_out)
    master_list=work/"shots_concat.txt"
    master_list.write_text("".join(f"file '{p.as_posix()}'\n" for p in shot_outputs))
    picture=out/"picture.mp4"
    run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",str(master_list),"-t","207.44","-an","-c","copy",str(picture)])
    final=out/plan["output"]["assembly_filename"]
    run(["ffmpeg","-y","-v","error","-i",str(picture),"-i",str(media/"Silver Coin (Remastered).wav"),"-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","aac","-b:a","320k","-ar","48000","-t","207.44","-movflags","+faststart",str(final)])
    report={
      "schema":"aivideoedit.assembly-report.v1",
      "output":final.name,
      "sha256":sha256(final),
      "duration_seconds":probe_duration(final),
      "fps":24,
      "resolution":[1280,720],
      "shots":[{"id":s["id"],"start":s["start"],"end":s["end"],"clips":s["clips"]} for s in plan["shots"]],
      "input_hash_verification":"PASS",
      "workflow":["WF-RENDER-DELIVERY","WF-LIVING-SCENE-ASSEMBLY","WF-LYRIC-LIVING-SCENE","WF-SOURCE-DERIVED-LOOPS","WF-IDENTITY-SAFE-LOOP-25D-QC"]
    }
    (out/plan["output"]["report_filename"]).write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
if __name__=="__main__":
    main()
