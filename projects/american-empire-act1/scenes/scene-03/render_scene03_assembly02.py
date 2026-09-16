#!/usr/bin/env python3
"""Rebuild Scene 03 Assembly02 from locked matched-angle GIF loops.

This script is the traceable render implementation for the current technical
candidate. Heavy media stays outside GitHub; pass --media-root to the restored
Scene 03 media workspace containing loops_v2 and the score/caption assets.
"""
from __future__ import annotations
import argparse, subprocess
from pathlib import Path
FRAME_COUNTS=[192,168,360,456,408,288,264,216]
FPS=24
TOTAL_FRAMES=2352
DURATION=98

def run(cmd:list[str])->None:
    subprocess.run(cmd,check=True)

def main()->int:
    p=argparse.ArgumentParser(); p.add_argument('--media-root',type=Path,required=True); p.add_argument('--score',type=Path,required=True); p.add_argument('--captions-ass',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    root=a.media_root.resolve(); out=a.output.resolve(); work=out.parent/'assembly02_shots'; work.mkdir(parents=True,exist_ok=True); shot_files=[]
    for i,frames in enumerate(FRAME_COUNTS,1):
        hid=f'S3H{i:02d}'; gif=root/'loops_v2'/f'{hid}_FX_ANGLE_LOOP.gif'; shot=work/f'{hid}.mp4'; shot_files.append(shot)
        run(['ffmpeg','-hide_banner','-loglevel','error','-y','-stream_loop','-1','-i',str(gif),'-vf','fps=24,scale=1280:720:flags=lanczos,format=yuv420p','-frames:v',str(frames),'-r','24','-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',str(shot)])
    concat=work/'concat.txt'; concat.write_text(''.join(f"file '{x.as_posix()}'\n" for x in shot_files),encoding='utf-8'); picture=out.parent/'Scene03_PICTURE02_ANGLE_LOOPS.mp4'
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(concat),'-c','copy',str(picture)])
    vf=f"ass={a.captions_ass.as_posix()}"
    run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(picture),'-i',str(a.score),'-filter_complex',f"[0:v]{vf}[v];[1:a]atrim=0:98,asetpts=PTS-STARTPTS[a]",'-map','[v]','-map','[a]','-frames:v',str(TOTAL_FRAMES),'-r',str(FPS),'-c:v','libx264','-preset','ultrafast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','256k','-movflags','+faststart',str(out)])
    return 0
if __name__=='__main__': raise SystemExit(main())
