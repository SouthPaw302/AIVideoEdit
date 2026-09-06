from __future__ import annotations
import cv2, json, math, subprocess, sys, hashlib, os
import numpy as np
from pathlib import Path
ROOT=Path(os.environ.get('AIVIDEOEDIT_PROJECT_ROOT','/mnt/data/ironflamenew_clean'))
sys.path.insert(0,str(ROOT/'canonical'))
from runtime import FXRuntime,FXContext
W,H=1280,720;FPS=24
controls=json.loads((ROOT/'analysis/reactive_controls_24fps.json').read_text())['frames']
recipes=json.loads((ROOT/'analysis/shot_recipes.json').read_text())
shot_npz=np.load(ROOT/'analysis/shot_assets.npz')
assets=[]
for i,r in enumerate(recipes,1):
    assets.append({'base':shot_npz[f'base_{i:02d}'],'flow':shot_npz[f'flow_{i:02d}'],'protect':shot_npz[f'protect_{i:02d}'],'presence':shot_npz[f'presence_{i:02d}'],'ribbon':shot_npz[f'ribbon_{i:02d}'],'recipe':r})
drivers=np.load(ROOT/'analysis/reference_motion_drivers.npz')
rt=FXRuntime(seed=302)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)

def smoothstep(q):q=float(np.clip(q,0,1));return q*q*(3-2*q)
def interp_driver(kind,q):
    seq=drivers[kind]
    x=np.clip(q,0,1)*(len(seq)-1);i=int(x);j=min(len(seq)-1,i+1);a=x-i
    small=cv2.addWeighted(seq[i],1-a,seq[j],a,0)
    return cv2.resize(small,(W,H),interpolation=cv2.INTER_CUBIC)

def draw_orb(fr,cx,cy,scale,energy,onset):
    rr=(xx-cx)**2+(yy-cy)**2;sig=(25+7*energy)*scale;halo=np.exp(-rr/(2*sig*sig));core=np.exp(-rr/(2*(6.5*scale)**2));f=fr.astype(np.float32);f+=halo[...,None]*np.array([24,90,205],np.float32)*(1+.25*onset);f+=core[...,None]*np.array([110,155,250],np.float32);return np.clip(f,0,255).astype(np.uint8),np.exp(-rr/(2*(60*scale)**2)).astype(np.float32)
def overlay_driver(fr,drv,kind,energy):
    a=drv.astype(np.float32)/255
    if kind=='A':col=np.array([150,80,28],np.float32);alpha=.24+.18*energy
    elif kind=='B':col=np.array([80,165,245],np.float32);alpha=.08+.12*energy
    else:col=np.array([220,170,75],np.float32);alpha=.10+.17*energy
    return np.clip(fr.astype(np.float32)+a[...,None]*col*alpha,0,255).astype(np.uint8)
def draw_dynamic_ring(fr,q,energy,onset,kind):
    if kind not in ('crystalline_transformation','second_energy_cycle','integration_peak'):return fr
    center=(620 if kind!='integration_peak' else 650,345);pulse=1+.045*math.sin(q*math.tau*2)+.035*onset;rx=(250 if kind!='integration_peak' else 320)*pulse;ry=(185 if kind!='integration_peak' else 235)*pulse;ov=np.zeros_like(fr);cv2.ellipse(ov,center,(int(rx),int(ry)),0,0,360,(230,190,95),2+int(2*energy),cv2.LINE_AA);ov=cv2.GaussianBlur(ov,(0,0),1.4);return cv2.addWeighted(fr,1,ov,.46+.25*energy,0)
def render_frame(global_idx):
    t=global_idx/FPS
    si=len(recipes)-1
    for k,r in enumerate(recipes):
        if t < r['end']-1e-9:si=k;break
    a=assets[si];r=a['recipe'];local=t-r['start'];dur=max(1e-6,r['duration']);q=np.clip(local/dur,0,1);c=controls[min(global_idx,len(controls)-1)];energy=float(c['rms_n']);onset=float(c['onset_n']);high=float(c['high_n'])
    ctx=FXContext(local,dur,global_idx,FPS,energy,onset,high);fr=a['base'].copy()
    drv=interp_driver(r['source_dna'],q);fr=overlay_driver(fr,drv,r['source_dna'],energy)
    # approved living flow on non-identity moving regions
    flow=np.maximum(a['flow'],drv if r['source_dna']!='B' else (drv*.55).astype(np.uint8));fr=rt.localized_living_flow(fr,ctx,mask=flow.astype(np.float32)/255.0,strength=float(r['approved_fx'][0]['strength']),protect=a['protect'].astype(np.float32)/255.0)
    # source-specific breathing: warm presence / cool ribbon field
    if r['source_dna']=='B' and a['presence'].max()>0:
        pm=a['presence'].astype(np.float32)/255;warm_gain=(3+13*(.5+.5*math.sin(local*.74))+14*energy);f=fr.astype(np.float32);f+=pm[...,None]*np.array([5,18,warm_gain],np.float32);fr=np.clip(f,0,255).astype(np.uint8)
    if r['source_dna']=='C':fr=draw_dynamic_ring(fr,q,energy,onset,r['kind'])
    # recurring signal/core path
    s=np.array(r['orb_start'],np.float32);e=np.array(r['orb_end'],np.float32);qq=smoothstep(q);pos=s*(1-qq)+e*qq;fr,orbmask=draw_orb(fr,float(pos[0]),float(pos[1]),.85+(.28 if r['kind']=='integration_peak' else 0),energy,onset)
    fr=rt.practical_light_breath(fr,ctx,mask=orbmask,strength=.050+.025*onset)
    fr=rt.moving_light_field(fr,ctx,origin=(pos[0]/W,pos[1]/H),strength=.045+.025*high)
    if r['shot'] in (2,6,10):fr=rt.advected_smoke(fr,ctx,strength=.18,tint=(84,78,96))
    if r['shot']==9:fr=rt.embers(fr,ctx,strength=.24,count=46)
    fr=rt.apply_canvas(fr,key=f'shot{r["shot"]:02d}',amount=.18)
    # onset accents: localized, not whole-frame strobe
    if onset>.55:
        localglow=cv2.GaussianBlur((orbmask*255).astype(np.uint8),(0,0),10).astype(np.float32)/255;f=fr.astype(np.float32);f+=localglow[...,None]*np.array([10,24,46],np.float32)*(onset-.55);fr=np.clip(f,0,255).astype(np.uint8)
    # secondary camera drift <=2 px, internal motion remains primary
    dx=1.7*math.sin(local*.29+si*.71);dy=1.1*math.sin(local*.23+.8+si*.37);M=np.float32([[1,0,dx],[0,1,dy]]);fr=cv2.warpAffine(fr,M,(W,H),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REFLECT_101)
    return fr

def sample_only(outdir):
    outdir.mkdir(parents=True,exist_ok=True);rows=[]
    thumbs=[]
    for si,r in enumerate(recipes):
        for frac in (.08,.50,.92):
            idx=int((r['start']+r['duration']*frac)*FPS);fr=render_frame(idx);p=outdir/f'shot{si+1:02d}_{int(frac*100):02d}.jpg';cv2.imwrite(str(p),fr,[cv2.IMWRITE_JPEG_QUALITY,92]);th=cv2.resize(fr,(320,180));cv2.putText(th,f'{si+1:02d} {int(frac*100):02d}%',(8,24),cv2.FONT_HERSHEY_SIMPLEX,.65,(245,245,245),2,cv2.LINE_AA);thumbs.append(th)
    for i in range(0,len(thumbs),6):rows.append(cv2.hconcat(thumbs[i:i+6]))
    maxw=max(x.shape[1] for x in rows);rows2=[]
    for x in rows:
        if x.shape[1]<maxw:x=cv2.copyMakeBorder(x,0,0,0,maxw-x.shape[1],cv2.BORDER_CONSTANT,value=(0,0,0))
        rows2.append(x)
    cv2.imwrite(str(outdir/'qc_montage.jpg'),cv2.vconcat(rows2),[cv2.IMWRITE_JPEG_QUALITY,90])

def final_render(out):
    total=int(round(recipes[-1]['end']*FPS));audio=os.environ.get('AIVIDEOEDIT_AUDIO',str(ROOT/'source/Ironflame_Redux.wav'))
    cmd=['ffmpeg','-y','-hide_banner','-loglevel','error','-f','rawvideo','-pix_fmt','bgr24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-i',audio,'-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','fast','-crf','17','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-shortest','-movflags','+faststart',str(out)]
    proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
    for i in range(total):
        proc.stdin.write(render_frame(i).tobytes())
        if i%480==0: print(f'render {i}/{total}',flush=True)
    proc.stdin.close();rc=proc.wait()
    if rc:raise SystemExit(rc)
    print('FINAL',out)

if __name__=='__main__':
    import argparse;ap=argparse.ArgumentParser();ap.add_argument('--sample',action='store_true');ap.add_argument('--out',default='/mnt/data/IronFlameNew_FINAL_720p24.mp4');a=ap.parse_args()
    sample_only(ROOT/'analysis/final_frame_qc') if a.sample else final_render(Path(a.out))
