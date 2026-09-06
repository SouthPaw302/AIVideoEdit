from __future__ import annotations
import argparse, json, os, subprocess, sys
from pathlib import Path
ROOT=Path(os.environ.get('AIVIDEOEDIT_PROJECT_ROOT','/mnt/data/ironflamenew_clean'))
sys.path.insert(0,str(ROOT))
import render_final as rf


def render_range(start_frame:int,end_frame:int,out:Path):
    if not (0 <= start_frame < end_frame <= len(rf.controls)):
        raise SystemExit(f'invalid frame range {start_frame}:{end_frame}')
    cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{rf.W}x{rf.H}','-r',str(rf.FPS),'-i','-',
         '-an','-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-g','48','-keyint_min','48','-sc_threshold','0','-movflags','+faststart',str(out)]
    p=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    try:
        for i in range(start_frame,end_frame):
            p.stdin.write(rf.render_frame(i).tobytes())
    finally:
        p.stdin.close()
    rc=p.wait()
    if rc: raise SystemExit(rc)


def shot_range(shot:int):
    rec=rf.recipes[shot-1]
    return int(round(rec['start']*rf.FPS)), int(round(rec['end']*rf.FPS))

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--shot',type=int)
    g.add_argument('--range',nargs=2,type=int,metavar=('START_FRAME','END_FRAME'))
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.shot is not None:
        s,e=shot_range(a.shot)
    else:
        s,e=a.range
    render_range(s,e,Path(a.out))
    print(json.dumps({'result':'PASS','start_frame':s,'end_frame':e,'frames':e-s,'fps':rf.FPS,'out':a.out}))
