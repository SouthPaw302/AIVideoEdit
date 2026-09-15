#!/usr/bin/env python3
"""Scene 03 deterministic matched-angle loop adapter.

Creates small, bounded horizontal viewpoint changes from an approved 2D hero plate
using a 3D-plane Y-axis projection. The adapter never generates or inpaints pixels;
it overscans and reflect-pads the approved plate so identity and topology remain
source-locked. Existing registered localized FX may be supplied frame-by-frame before
the viewpoint transform.
"""
from __future__ import annotations
import argparse, math
from pathlib import Path
import cv2
import numpy as np
from PIL import Image

DEFAULT_YAW_DEG = 0.85
DEFAULT_OVERSCAN = 1.025
DEFAULT_FOCAL_PX = 1700.0


def homography_yaw(width: int, height: int, yaw_deg: float, focal_px: float) -> np.ndarray:
    theta = math.radians(yaw_deg)
    c, s = math.cos(theta), math.sin(theta)
    cx, cy = (width - 1) / 2.0, (height - 1) / 2.0
    src = np.float32([[0,0],[width-1,0],[width-1,height-1],[0,height-1]])
    dst=[]
    for x,y in src:
        X, Y = x-cx, y-cy
        Xp = c * X
        Zp = -s * X
        denom = focal_px + Zp
        dst.append([focal_px * Xp / denom + cx, focal_px * Y / denom + cy])
    return cv2.getPerspectiveTransform(src, np.float32(dst))


def matched_angle(rgb: np.ndarray, yaw_deg: float, overscan: float=DEFAULT_OVERSCAN, focal_px: float=DEFAULT_FOCAL_PX) -> np.ndarray:
    h,w = rgb.shape[:2]
    w2,h2 = int(w*overscan), int(h*overscan)
    big = cv2.resize(rgb,(w2,h2),interpolation=cv2.INTER_LANCZOS4)
    matrix = homography_yaw(w2,h2,yaw_deg,focal_px)
    warped = cv2.warpPerspective(big,matrix,(w2,h2),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REFLECT_101)
    x0,y0=(w2-w)//2,(h2-h)//2
    return warped[y0:y0+h,x0:x0+w]


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument('input',type=Path)
    p.add_argument('output_a',type=Path)
    p.add_argument('output_b',type=Path)
    p.add_argument('--yaw',type=float,default=DEFAULT_YAW_DEG)
    p.add_argument('--overscan',type=float,default=DEFAULT_OVERSCAN)
    p.add_argument('--focal',type=float,default=DEFAULT_FOCAL_PX)
    a=p.parse_args()
    rgb=np.array(Image.open(a.input).convert('RGB'))
    Image.fromarray(matched_angle(rgb,-a.yaw,a.overscan,a.focal)).save(a.output_a)
    Image.fromarray(matched_angle(rgb,+a.yaw,a.overscan,a.focal)).save(a.output_b)
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
