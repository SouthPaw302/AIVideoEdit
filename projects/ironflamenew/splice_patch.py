from __future__ import annotations
import argparse, json, os, subprocess
from pathlib import Path
FPS=24

def probe(path: str|Path):
    raw=subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=nb_frames,r_frame_rate,width,height','-of','json',str(path)])
    s=json.loads(raw)['streams'][0]
    n=int(s['nb_frames']) if s.get('nb_frames') not in (None,'N/A') else None
    return {'frames':n,'fps':s.get('r_frame_rate'),'width':int(s['width']),'height':int(s['height'])}

def main():
    ap=argparse.ArgumentParser(description='Frame-exact patch splice: reuse base master, replace only declared video ranges, preserve base audio.')
    ap.add_argument('--base',required=True)
    ap.add_argument('--patch',action='append',nargs=3,metavar=('START_FRAME','END_FRAME','PATCH_MP4'),required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    base=probe(a.base)
    if base['fps'] != '24/1': raise SystemExit(f"base fps must be 24/1, got {base['fps']}")
    if not base['frames']: raise SystemExit('base nb_frames unavailable')
    patches=sorted((int(s),int(e),p) for s,e,p in a.patch)
    for i,(s,e,p) in enumerate(patches):
        if not (0 <= s < e <= base['frames']): raise SystemExit(f'invalid patch range {s}:{e}')
        if i and s < patches[i-1][1]: raise SystemExit('overlapping patch ranges')
        pp=probe(p); exp=e-s
        if pp['frames'] != exp: raise SystemExit(f'patch {p} has {pp["frames"]} frames; expected {exp}')
        if pp['fps'] != '24/1' or pp['width'] != base['width'] or pp['height'] != base['height']:
            raise SystemExit(f'patch {p} stream geometry/fps differs from base')
    inputs=['-i',a.base]
    for _,_,p in patches: inputs += ['-i',p]
    parts=[]; labels=[]; cur=0
    for idx,(s,e,p) in enumerate(patches, start=1):
        if s>cur:
            lab=f'b{idx}a'; parts.append(f'[0:v]trim=start_frame={cur}:end_frame={s},setpts=PTS-STARTPTS[{lab}]'); labels.append(f'[{lab}]')
        lab=f'p{idx}'; parts.append(f'[{idx}:v]setpts=PTS-STARTPTS[{lab}]'); labels.append(f'[{lab}]')
        cur=e
    if cur < base['frames']:
        lab='btail'; parts.append(f'[0:v]trim=start_frame={cur}:end_frame={base["frames"]},setpts=PTS-STARTPTS[{lab}]'); labels.append(f'[{lab}]')
    parts.append(''.join(labels)+f'concat=n={len(labels)}:v=1:a=0[vout]')
    out=Path(a.out); tmp=out.with_suffix(out.suffix+'.tmp.mp4')
    cmd=['ffmpeg','-y','-hide_banner','-loglevel','error',*inputs,'-filter_complex',';'.join(parts),'-map','[vout]','-map','0:a?','-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-fps_mode','cfr','-c:a','copy','-movflags','+faststart',str(tmp)]
    subprocess.check_call(cmd)
    final=probe(tmp)
    if final['frames'] != base['frames'] or final['fps'] != '24/1':
        tmp.unlink(missing_ok=True); raise SystemExit(f'patched master validation failed: {final} vs base {base}')
    os.replace(tmp,out)
    print(json.dumps({'result':'PASS','base_frames':base['frames'],'patches':patches,'out':str(out),'output_frames':final['frames']}))
if __name__=='__main__': main()
