# Irish Eyes — Effect Proof 02: 2.5D Parallax

Status: **PASS FOR DIRECTION / approved for further shot production**

## Why the first proof failed

The first 2.5D attempt relied too heavily on a hard foreground cutout. It created visible silhouette/matte artifacts around the subject and therefore failed the project's render-proof rule.

## Revised technique

The replacement proof uses a continuous depth-field approach inspired by PlayCanvas's height-map / parallax-occlusion rendering model:

- far sky: minimal motion;
- horizon/water: small motion;
- near shoreline/foreground: larger motion;
- Brandi: protected foreground plane with slightly stronger motion;
- background behind Brandi: inpainted before camera travel;
- alpha edge: signed-distance feathering + edge-preserving smoothing;
- background camera movement: backward remap driven by continuous depth values;
- foreground camera movement: separate eased transform;
- camera path: five-second sinusoidal orbit returning smoothly to its starting position.

This avoids making the effect depend on a visibly hard silhouette edge.

## Real source

Representative key frame:

- extracted source frame: `frame_00100.png`
- real frame dimensions: 720 × 1280 portrait after rotation metadata
- no generated face/body used

## Proof render

Workspace proof:

- `proof_25d_softdepth_h264.mp4`
- 5 seconds @ 30 fps
- SHA-256 of compact QC render: `9684d2c4c8a2f32556ddb2b7e36b845a2eadedeb5be18284aca344af592a8096`

Representative frames at the start, quarter, midpoint, three-quarter, and end of the camera path were inspected side-by-side.

## QC

- actual foreground/background differential motion: PASS
- uniform Ken Burns zoom only: NO — depth-dependent displacement is present
- Brandi recognizable: PASS
- generated face/body: none
- obvious hard matte/sticker edge in representative frames: PASS after revision
- background disocclusion: hidden by inpainted plate and conservative motion
- camera path continuity: PASS
- excessive artificial depth: NO; motion intentionally restrained

The proof is not considered the final 2.5D shot. Production shots may receive more accurate hand-tuned masks/depth fields, additional water/cloud animation, restoration, and music-driven optical treatment.

## PlayCanvas technical reference

The connected GitHub source was inspected directly:

- `playcanvas/engine/examples/src/examples/materials/parallax-mapping.example.mjs`
- `playcanvas/engine/src/scene/shader-lib/glsl/chunks/standard/frag/parallax.js`

PlayCanvas's parallax-occlusion path uses a height field and view direction to march/offset texture lookup. The Irish Eyes offline renderer adopts the same core visual principle — continuous depth-driven displacement rather than only sliding cardboard planes — using original OpenCV implementation code.

## Reusable promotion

Approved implementation promoted to main:

- `general/reusable/depth-parallax-25d/README.md`
- `general/reusable/depth-parallax-25d/depth_parallax_25d.py`

## Next 2.5D production work

1. choose 3–5 strongest source key frames across the 953-frame library;
2. tune subject rectangles/mattes individually;
3. make scene-specific horizon/shore depth maps;
4. add independent water and cloud motion where useful;
5. composite with the approved restoration/halation treatment;
6. map camera amplitude to the song section rather than using one constant move;
7. use the strongest resulting 2.5D passages as bridges between real-motion footage and newly created photoreal scenes.