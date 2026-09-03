# Silver Coin — Reference Motion Signature

The two user-supplied six-second style clips are treated as **motion-language references**, not literal scene/character sources.

Measured with `tools/video_fx/analyze_motion_signature.py` at a normalized 280×280 analysis size.

## Reference A — `imagine-d04b484c.mp4`

- 24 fps, 145 frames, 6.0417 s
- mean optical-flow magnitude: **~1.566 px/frame**
- median frame P90 flow: **~2.214 px/frame**
- median frame P99 flow: **~3.235 px/frame**
- mean normalized frame difference: **~0.0456**
- mean absolute phase-correlation shift: ~0.56 px horizontal / ~0.79 px vertical per frame
- mean saturation: ~0.515
- mean luminance: ~0.438

Interpretation: the more animated reference. It permits visible character/environment motion and camera drift while remaining painterly.

## Reference B — `imagine-5558fc80.mp4`

- 24 fps, 145 frames, 6.0417 s
- mean optical-flow magnitude: **~0.428 px/frame**
- median frame P90 flow: **~0.545 px/frame**
- median frame P99 flow: **~1.346 px/frame**
- mean normalized frame difference: **~0.0149**
- mean absolute phase-correlation shift: ~0.18 px horizontal / ~0.07 px vertical per frame
- mean saturation: ~0.563
- mean luminance: ~0.386

Interpretation: the restrained reference. Portraits, quiet narrative scenes, and held emotional beats should live closer to this envelope.

## Production rule

Silver Coin V5+ maps song sections between these two measured motion densities rather than applying one constant Ken-Burns/zoom speed:

- verses / portraits → near restrained-reference density
- tavern chorus → between references, biased toward the active reference
- fiddle/dance transients → may briefly approach active-reference P90/P99 motion
- bridge → medium motion with deliberate subject changes
- final chorus → active reference envelope, but canvas/face stability still wins over raw motion

This is a reusable method: **reference-motion calibration**. It can be applied to any future project when one or more visual clips define the desired animation character.
