# Irish Eyes — Production Rules

Branch: `song/irish-eyes`

These rules are binding for the Irish Eyes production. They exist specifically to prevent a repeat of prior failures where effects were described in planning documents but were not actually present in rendered output.

## 1. Render-proof rule

**No effect is considered implemented until a rendered proof exists.**

For every planned effect, produce a short before/after proof clip or representative rendered frames before it is allowed into the full edit. Planning text, code, shader files, parameter JSON, or screenshots of a tool do not count as proof by themselves.

Each effect must have:

1. source frame/clip;
2. implementation method;
3. parameter/preset record;
4. rendered proof;
5. visual QC result;
6. decision: keep, revise, or reject.

If an effect cannot be visibly verified in the proof, it is not finished.

## 2. Photoreal identity rule

`Brandi South Florida 2017.mp4` is the identity and reality anchor.

- Brandi's real photographic face/body must remain the primary subject plate.
- Do not reconstruct her face/body as a Gaussian splat, NeRF character, or generated lookalike.
- Masks, depth maps, rotoscoping, optical treatment, compositing, and environmental extension may surround the subject without replacing her.
- Any generated extension that changes recognizable identity, anatomy, clothing continuity, or facial geometry fails QC.

## 3. PlayCanvas is an implementation tool, not inspiration

The PlayCanvas ecosystem is approved as an actual rendering/effects toolchain for this production.

Reference projects:

- `playcanvas/engine` — WebGL/WebGPU graphics runtime.
- `playcanvas/supersplat` — open-source 3D Gaussian Splat editor.
- `playcanvas/supersplat-viewer` — high-performance Gaussian-splat viewer/rendering path.

When PlayCanvas is named in a shot/effect plan, it must be used in that shot's real render path. Do not write "PlayCanvas effect" and then deliver an untreated FFmpeg slideshow.

## 4. PlayCanvas effects approved for Irish Eyes

Use the modern PlayCanvas post-processing path where appropriate, especially `CameraFrame` / modern render passes.

Approved effects include:

- HDR bloom / natural highlight glow;
- restrained color grading and LUT treatment;
- depth of field when supported by actual depth/scene separation;
- TAA / temporal cleanup for rendered 3D or 2.5D material;
- SSAO only for reconstructed 3D environmental geometry where it remains natural;
- subtle vignette/fringing only when optically motivated;
- custom compose-shader work for water shimmer, sun/reflection modulation, atmospheric diffusion, lens/refraction behavior, and audio-reactive parameters;
- custom render passes when a screen-space compose shader is insufficient.

Effects must be restrained enough to preserve documentary realism.

## 5. Gaussian splat / SuperSplat rule

3D Gaussian Splatting is allowed primarily for the South Florida waterfront/background environment.

- Extract usable source frames with real parallax before attempting reconstruction.
- Build/test the environment separately from the Brandi foreground plate.
- Inspect, crop, clean, optimize, and test splats before compositing.
- Use SuperSplat for inspection/editing/optimization/presentation of splat assets when applicable.
- Camera travel through a splat must remain physically plausible and modest; do not expose holes, floaters, stretched geometry, or missing coverage.
- If the source footage does not provide enough spatial information for a convincing splat, fall back to 2.5D parallax rather than forcing a bad 3D reconstruction.

## 6. 2.5D parallax rule

For strong source frames that lack enough multi-view coverage for 3DGS:

- separate subject, water/midground, skyline/shore, sky, and foreground optical elements;
- create or estimate depth masks;
- move the virtual camera conservatively;
- protect the subject silhouette and hair edges;
- animate water/clouds/reflections independently where appropriate;
- hide layer seams with atmosphere, light, natural motion, and matched grain.

A 2.5D shot must contain actual depth differential. A uniform Ken Burns zoom does not qualify.

## 7. Audio-reactive implementation rule

Audio reactivity must be computed from `Irish eyes (Remastered).wav` and mapped to real effect parameters.

Suggested mapping:

- low-frequency energy -> atmospheric weight, very subtle camera energy, reflection intensity;
- midrange -> water/cloth/environment motion density;
- high-frequency energy -> sun glints, bloom sparkle, fine reflection highlights;
- transients -> restrained cut/light/refraction accents;
- sustained vocal/reverb energy -> diffusion, depth, atmospheric expansion.

The mapping must be smoothed and bounded. No strobing, random pulsing, or generic spectrum overlay.

A saved analysis/automation file must document the signal-to-effect mapping used in the final render.

## 8. Effect-proof workflow

Before any full-song render:

### Gate A — Source extraction

Create representative source frames and short clips from the 2017 video.

### Gate B — Effect laboratory

Build 3–10 second effect proofs for each major technique:

- PlayCanvas grade/bloom;
- water/reflection shader;
- 2.5D parallax;
- Gaussian-splat environment if viable;
- depth of field;
- audio-reactive modulation;
- dream/reflection transition.

### Gate C — Side-by-side QC

Compare source vs effected result and verify:

- effect is actually visible;
- effect improves the shot;
- Brandi remains photorealistic and recognizable;
- no face/body drift;
- no broken edges/masks;
- no artificial motion artifacts;
- no flicker or unstable exposure;
- no obvious CGI mismatch;
- no splat holes/floaters;
- no excessive bloom or fake bokeh.

### Gate D — Sequence integration

Only approved proof techniques may be used in the timeline.

### Gate E — Full render QC

Sample the final render at scene boundaries and at regular intervals. A final export fails if planned effects silently disappeared, were bypassed, or rendered differently from approved proofs.

## 9. Fallback rule

If a PlayCanvas/3D technique cannot be made reliable with the available source, do not fake success.

Use the strongest physically plausible fallback:

1. PlayCanvas full 3D / Gaussian environment when viable;
2. PlayCanvas 2.5D scene with subject masks/depth layers;
3. high-quality FFmpeg/OpenCV compositing, retiming, grading, or optical treatment;
4. original footage preserved cleanly.

The fallback and reason must be recorded in the project decision log.

## 10. Artifact/checkpoint rule

Keep production state recoverable on the `song/irish-eyes` branch.

At minimum preserve text/configuration artifacts for:

- source analysis;
- shot list/timeline;
- depth/mask strategy;
- PlayCanvas scene/effect configuration;
- shader/custom-pass code;
- audio-reactive mapping;
- Gaussian-splat settings/notes;
- effect proof manifest;
- QC results;
- final render manifest.

Large binaries may be archived using the repository's established binary-storage policy, but their checksums/locations must be recorded in the branch.

## 11. No slideshow rule

The 31.77-second source cannot simply be looped, frozen, or converted into a sequence of slow zooms for a 3:07 song.

The finished video must contain meaningful motion generated from the real source world: original motion, retimed footage, living-frame motion, environmental extension, parallax, reconstructed camera travel, reflection/cloud/water movement, and music-driven optical behavior.

## 12. Restraint rule

The objective is not to show every available effect. The objective is a believable cinematic memory.

Use effects where the song asks for expansion. Return repeatedly to untouched or minimally treated real footage so the viewer never loses the photographic truth of the original moment.

## 13. Final acceptance rule

Irish Eyes is not ready for delivery unless all of the following are true:

- the source subject is recognizable and photoreal throughout;
- effects are visibly present in the exported file, not only in plans/code;
- major effects have proof clips/frames and recorded settings;
- the edit contains genuine dimensional/environmental motion beyond zooms;
- PlayCanvas/SuperSplat usage, when claimed, is tied to actual rendered assets;
- audio-reactive behavior is driven by measured song data;
- the final 3:07 sequence feels like one coherent South Florida memory rather than a demo reel.
