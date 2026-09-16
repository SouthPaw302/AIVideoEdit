#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFilter
import argparse, math

def overlay(effect_id, size, phase):
    W,H=size
    ov=Image.new('RGBA',size,(0,0,0,0)); d=ImageDraw.Draw(ov)
    idx=int(effect_id[-2:])
    if idx in (1,5,6,8):
        x0=760 if idx != 8 else 40
        for x in range(x0,W-20,65):
            y=(x*(7+idx))%max(100,H-120)+30
            d.line((x,y,x-10,y+50),fill=(180,210,225,int(28*phase)),width=2)
    if idx in (2,3,4,5,6,7):
        x=1040 if idx in (2,5) else (620 if idx==4 else 930)
        y=215 if idx==2 else (90 if idx==4 else 250)
        d.ellipse((x-85,y-55,x+85,y+55),fill=(75,205,220,int(18*phase)))
    if idx in (5,6,8):
        d.rectangle((0,int(H*.73),W,H),fill=(100,165,190,int(7*phase)))
    return ov.filter(ImageFilter.GaussianBlur(.6))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('hero'); ap.add_argument('out'); ap.add_argument('--id',required=True); ap.add_argument('--phase',type=float,default=1.0)
    a=ap.parse_args(); base=Image.open(a.hero).convert('RGBA'); out=Image.alpha_composite(base,overlay(a.id,base.size,a.phase)); out.save(a.out)
if __name__=='__main__': main()
