# Irish Eyes — 3D Gaussian Splatting Pipeline

Purpose: convert real captured source imagery into a navigable/renderable spatial scene rather than hallucinating a replacement video.

## What 3DGS means here

The input must be real photographs or frames extracted from real video that contain enough viewpoint/parallax coverage. A Structure-from-Motion stage estimates camera poses and a sparse point cloud; a Gaussian-splat trainer then optimizes 3D Gaussian primitives against those real views. The resulting scene can be navigated with a new virtual camera and rendered in real time.

This is distinct from Gaussian-shaped light/bloom fields and distinct from text/image-to-video generation.

## PlayCanvas / SuperSplat role

PlayCanvas/SuperSplat is the preferred real-time editing, inspection, camera-animation and video-render layer once a trained splat exists.

Important: PlayCanvas does not itself train source images into a splat. A separate SfM/training pipeline must produce a compatible splat, usually `.ply` or another supported splat format.

SuperSplat can then be used to:

- inspect and clean splats;
- remove floaters / bad coverage;
- optimize/compress;
- animate cameras on a timeline;
- import real camera poses where applicable;
- render high-quality video from the camera animation;
- export/host an interactive viewer when useful.

## Candidate training paths

Preferred candidates to evaluate before writing a custom trainer:

1. Nerfstudio `splatfacto` / gsplat ecosystem where CUDA-capable compute is available;
2. another proven trainer recommended by the current PlayCanvas Gaussian-splat tooling;
3. a remote/GPU workflow only when required by the available source and justified by the shot.

Do not spend time forcing 3DGS on a source window with insufficient viewpoint coverage. Use source-derived 2.5D when it is the stronger result.

## Irish Eyes source test

The original `Brandi South Florida 2017.mp4` is 31.766344 s / 953 frames at 30 fps. Before attempting training:

1. isolate a background/environment window with maximum real camera parallax and minimum moving-subject obstruction;
2. mask or exclude Brandi where possible so the moving person does not become unstable scene geometry;
3. subsample frames for sufficient baseline rather than training 953 near-duplicates;
4. run camera/SfM viability first;
5. only proceed to Gaussian training if camera recovery is stable and scene coverage is adequate;
6. keep Brandi as a real photographic foreground plate when the shot uses the reconstructed environment.

## Intended artistic use

Do not use splats merely because they are technologically impressive. Use them for shots where the viewer should feel that a captured photograph/shoreline suddenly becomes spatial and the camera can move into or around the real moment.

Potential Irish Eyes roles:

- modest lateral/orbit travel around the waterfront;
- pull-back that reveals spatial shoreline depth;
- push through a real reflection/horizon into a reconstructed space;
- impossible-looking but source-grounded camera moves that would not be possible from a single flat image.

## Magic Gate

A 3DGS proof only passes when:

- the scene remains recognizably the real South Florida source;
- no floaters/holes/stretched splats dominate;
- the camera move creates a meaningful spatial revelation;
- Brandi remains photographically stable when composited;
- the proof is more compelling than the equivalent 2.5D treatment;
- the exported render is inspected, not merely the interactive viewer.
