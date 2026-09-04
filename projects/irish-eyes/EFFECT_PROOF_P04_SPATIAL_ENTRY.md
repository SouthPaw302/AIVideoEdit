# Irish Eyes — Effect Proof P04: Spatial Entry

Branch: `song/irish-eyes`

## Purpose

Test whether the real Brandi source can support the sensation that the camera actually moves past the subject and enters the captured waterfront, without requiring a synthetic replacement scene.

## Source

Primary real source window: frames 451–530 from `Brandi South Florida 2017.mp4`.

This window was selected because Brandi naturally drifts toward the left edge while the right side opens into unobstructed real water/sky. That lets the virtual camera move rightward into clean source imagery rather than fabricating the hidden background behind her.

## Rejected clean-plate experiments

Two attempted generative clean-plate edits were rejected before use because they drifted into unrelated people/locations instead of preserving the South Florida source. They are not part of the accepted lineage.

The temporal-median clean-plate experiment was also rejected because Brandi remains in nearly the same region through much of the source and her silhouette persisted in the median.

## P04 V1

Output: `IE_P04_SPATIAL_ENTRY/preview/p04_spatial_entry_v1.mp4`

- 5.0 s
- 30 fps
- 360x640 proof
- 150 frames
- 0 black frames
- mean frame difference: 4.0205
- SHA-256: `aaf20a2e8094f092d60c0e272b28794d46541aa25a5424313047bf23eaec5fa6`

Implementation:

- retained actual motion across frames 451–530;
- authored rightward camera slide and push;
- Brandi exits frame through genuine source motion plus reframing rather than a body dissolve;
- independently animated source-derived sky/cloud region;
- independently animated water region;
- motivated Gaussian-shaped light field from the real upper-right sun/highlight source;
- water glint response and haze;
- restrained saturation/contrast/halation finishing.

QC result: clean and promising, but the spatial read still leaned too much toward a sophisticated crop/push.

Decision: **REVISE**.

## P04 V2

Output: `IE_P04_SPATIAL_ENTRY/preview/p04_spatial_entry_v2.mp4`

- 5.2 s
- 30 fps
- 360x640 proof
- 156 frames
- 0 black frames
- mean frame difference: 3.3137
- SHA-256: `c5f32d69e01c08bb2f71ac1ca7933e6e99da0685b2af3b05f4d11935063416c2`

Additional implementation over V1:

- sky, far-water/horizon and near-water/shore are transformed at different rates;
- stronger depth differential during the rightward move;
- real source motion dominates the opening half;
- once Brandi naturally clears left, the shot continues inside source-derived living sky/water rather than freezing;
- camera push strengthens after the subject clears the frame;
- motivated light volume and source-water highlight response remain tied to the real scene;
- final perception move narrows into the real water/horizon instead of a synthetic destination.

## Magic Gate evaluation

P04 V2 is the first current-pass proof to solve the most important spatial problem without replacing the real scene: the viewer can move past the real subject into the real captured environment, with multiple depth bands moving differently.

It does not yet represent literal 3D Gaussian Splatting or full photogrammetric reconstruction. It is a source-derived spatial-compositing technique built from real motion, real clean visible regions, depth-band transforms and environmental motion.

Decision: **KEEP — PROVISIONAL MAGIC GATE PASS**.

Reason for provisional status: it is strong enough to enter the approved moving-asset library, but it should still be compared against a future true-3DGS/SfM proof if the source proves capable of supporting one.

## 3DGS preflight

Current sandbox tool check:

- `ffmpeg`: available
- OpenCV: available
- PyTorch CPU: available
- `colmap`: not currently exposed
- `glomap`: not currently exposed
- Nerfstudio / `ns-train`: not currently exposed

Therefore no claim of a real 3DGS reconstruction is made from this proof.

Next step is a source-camera/parallax viability test before attempting to add/install any reconstruction toolchain.
