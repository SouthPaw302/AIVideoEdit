from pathlib import Path
import json, math, cv2, numpy as np, subprocess
master=Path('/work/master.mp4'); audio=Path('/work/music.wav'); outdir=Path('/work/out'); outdir.mkdir(parents=True,exist_ok=True)
FPS=24; W,H=960,540
shots=[
(0.000,7.803,'video',0.0,1,1.00,1.06,(.50,.50),(.50,.48),'wide_hold'),
(7.803,18.484,'video',9.0,1,1.04,1.18,(.50,.50),(.56,.47),'slow_push'),
(18.484,29.165,'video',20.5,2,1.02,1.16,(.45,.50),(.56,.49),'lateral_reframe'),
(29.165,44.119,'video',36.5,3,1.08,1.28,(.52,.50),(.57,.46),'detail_push'),
(44.119,46.255,'still','/work/04_golden_causeway_beneath_orbital_rings.png',4,1.28,1.36,(.50,.54),(.52,.50),'detail_punch'),
(46.255,56.936,'video',52.0,4,1.03,1.23,(.50,.52),(.53,.48),'forward_push'),
(56.936,65.481,'video',77.5,5,1.02,1.15,(.50,.48),(.46,.46),'fog_drift_camera'),
(65.481,69.754,'diff',(83.0,85.0),5,1.12,1.20,(.48,.47),(.53,.45),'differential_loop'),
(69.754,82.571,'video',94.0,6,1.22,1.02,(.54,.48),(.50,.50),'reverse_reveal'),
(82.571,95.388,'video',115.5,7,1.05,1.19,(.44,.50),(.56,.48),'lateral_reframe'),
(95.388,110.342,'video',143.0,8,1.02,1.24,(.50,.50),(.55,.46),'slow_push'),
(110.342,112.478,'still','/work/09_cosmic_arcology_radiant_horizon.png',9,1.30,1.38,(.52,.50),(.55,.46),'detail_punch'),
(112.478,125.296,'video',173.5,9,1.02,1.18,(.50,.49),(.54,.45),'climax_push'),
(125.296,138.113,'video',186.5,9,1.12,1.28,(.54,.46),(.46,.44),'climax_reframe'),
(138.113,140.249,'still','/work/10_concentric_rings_twilight.png',10,1.32,1.24,(.53,.49),(.50,.50),'detail_release'),
(140.249,150.931,'diff',(221.0,223.0),10,1.18,1.10,(.52,.50),(.48,.50),'differential_reflection_loop'),
(150.931,163.120,'video',218.0,10,1.18,1.00,(.52,.49),(.50,.50),'final_pullback')]
def fit_image(path):
 im=cv2.imread(str(path)); h,w=im.shape[:2]; s=max(W/w,H/h); nw,nh=int(round(w*s)),int(round(h*s)); im=cv2.resize(im,(nw,nh),interpolation=cv2.INTER_LANCZOS4); x=(nw-W)//2; y=(nh-H)//2; return im[y:y+H,x:x+W]
def camera(fr,z,cx,cy):
 h,w=fr.shape[:2]; cw=max(2,int(round(w/z))); ch=max(2,int(round(h/z))); x=int(round(cx*w-cw/2)); y=int(round(cy*h-ch/2)); x=max(0,min(w-cw,x)); y=max(0,min(h-ch,y)); return cv2.resize(fr[y:y+ch,x:x+cw],(W,H),interpolation=cv2.INTER_LANCZOS4)
def grab(t):
 c=cv2.VideoCapture(str(master)); c.set(cv2.CAP_PROP_POS_MSEC,t*1000); ok,fr=c.read(); c.release()
 if not ok: raise RuntimeError(t)
 return fr
silent=outdir/'Shifting_Cycles_Music_Revamp_CAMERA_PASS_silent.mp4'; wr=cv2.VideoWriter(str(silent),cv2.VideoWriter_fourcc(*'mp4v'),FPS,(W,H)); log=[]
for o0,o1,kind,src,scene,z0,z1,c0,c1,move in shots:
 n=max(1,int(round((o1-o0)*FPS)))
 if kind=='video':
  cap=cv2.VideoCapture(str(master)); cap.set(cv2.CAP_PROP_POS_MSEC,float(src)*1000)
 elif kind=='still': A=fit_image(src)
 else: A=grab(src[0]); B=grab(src[1])
 for i in range(n):
  p=0 if n==1 else i/(n-1); e=p*p*(3-2*p); z=z0+(z1-z0)*e; cx=c0[0]+(c1[0]-c0[0])*e; cy=c0[1]+(c1[1]-c0[1])*e
  if kind=='video':
   ok,fr=cap.read()
   if not ok: fr=grab(float(src)+i/FPS)
  elif kind=='still': fr=A
  else:
   ph=0.5-0.5*math.cos(2*math.pi*(p*2.0)); fr=cv2.addWeighted(A,1-ph,B,ph,0)
  wr.write(camera(fr,z,cx,cy))
 if kind=='video': cap.release()
 log.append({'out_start':o0,'out_end':o1,'kind':kind,'scene':scene,'camera_move':move,'zoom':[z0,z1]})
wr.release()
final=outdir/'Shifting_Cycles_Recursive_Horizon_MUSIC_REVAMP_CAMERA_PASS_v1.mp4'
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(silent),'-i',str(audio),'-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-shortest','-movflags','+faststart',str(final)],check=True)
(outdir/'CAMERA_PASS_PLAN.json').write_text(json.dumps({'project':'Shifting Cycles — Recursive Horizon','baseline_master':master.name,'music_revamp_audio':audio.name,'visual_policy':'Approved baked FX preserved. Camera/edit pass only; original 1672x941 stills used for brief deep-detail coverage; differential shots use neighboring baked-master frames.','shots':log},indent=2))
print(final)
