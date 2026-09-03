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

## 3. Source-first / frame-by-frame rule

Use the user's original video whenever the required visual can be recovered or derived from it.

- Extract the full source at native frame cadence before fabricating substitute imagery.
- Treat individual source frames, neighboring frame windows, and short motion segments as reusable photographic assets.
- Prefer enhancement, restoration, interpolation, retiming, looping, masking, depth separation, optical compositing, and environmental extension of real frames over generating a replacement shot.
- Generated content may fill missing environmental information, but it must inherit perspective, lighting, texture, grain, color, and motion from the real source.
- Every loop must be built from actual motion or intentionally synthesized motion tied to the real source frame sequence. Do not repeat a clip with an obvious jump.
- Loop candidates should be tested for entry/exit similarity, motion direction, subject continuity, exposure continuity, and visible seam quality.
- Frame enhancement must preserve facial identity and natural skin texture. Over-sharpening, waxy denoise, hallucinated eyes/teeth/hair, or temporal face drift fails QC.

## 4. PlayCanvas is an implementation tool, not inspiration

The PlayCanvas ecosystem is approved as an actual rendering/effects toolchain for this production.

Reference projects:

- `playcanvas/engine` — WebGL/WebGPU graphics runtime.
- `playcanvas/supersplat` — open-source 3D Gaussian Splat editor.
- `playcanvas/supersplat-viewer` — high-performance Gaussian-splat viewer/rendering path.

When PlayCanvas is named in a shot/effect plan, it must be used in that shot's real render path. Do not write "PlayCanvas effect" and then deliver an untreated FFmpeg slideshow.

## 5. PlayCanvas effects approved for Irish Eyes

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

## 6. Gaussian splat / SuperSplat rule

3D Gaussian Splatting is allowed primarily for the South Florida waterfront/background environment.

- Extract usable source frames with real parallax before attempting reconstruction.
- Build/test the environment separately from the Brandi foreground plate.
- Inspect, crop, clean, optimize, and test splats before compositing.
- Use SuperSplat for inspection/editing/optimization/presentation of splat assets when applicable.
- Camera travel through a splat must remain physically plausible and modest; do not expose holes, floaters, stretched geometry, or missing coverage.
- If the source footage does not provide enough spatial information for a convincing splat, fall back to 2.5D parallax rather than forcing a bad 3D reconstruction.

## 7. 2.5D parallax rule

For strong source frames that lack enough multi-view coverage for 3DGS:

- separate subject, water/midground, skyline/shore, sky, and foreground optical elements;
- create or estimate depth masks;
- move the virtual camera conservatively;
- protect the subject silhouette and hair edges;
- animate water/clouds/reflections independently where appropriate;
- hide layer seams with atmosphere, light, natural motion, and matched grain.

A 2.5D shot must contain actual depth differential. A uniform Ken Burns zoom does not qualify.

## 8. Audio-reactive implementation rule

Audio reactivity must be computed from `Irish eyes (Remastered).wav` and mapped to real effect parameters.

Suggested mapping:

- low-frequency energy -> atmospheric weight, very subtle camera energy, reflection intensity;
- midrange -> water/cloth/environment motion density;
- high-frequency energy -> sun glints, bloom sparkle, fine reflection highlights;
- transients -> restrained cut/light/refraction accents;
- sustained vocal/reverb energy -> diffusion, depth, atmospheric expansion.

The mapping must be smoothed and bounded. No strobing, random pulsing, or generic spectrum overlay.

A saved analysis/automation file must document the signal-to-effect mapping used in the final render.

## 9. Effect-proof workflow

Before any full-song render:

### Gate A — Source extraction

Create representative source frames and short clips from the 2017 video, while retaining a complete native-cadence frame extraction for frame-level work.

### Gate B — Effect laboratory

Build 3–10 second effect proofs for each major technique:

- PlayCanvas grade/bloom;
- water/reflection shader;
- 2.5D parallax;
- Gaussian-splat environment if viable;
- depth of field;
- audio-reactive modulation;
- dream/reflection transition;
- enhanced real-frame loop.

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
- no excessive bloom or fake bokeh;
- loops do not visibly jump at the seam.

### Gate D — Sequence integration

Only approved proof techniques may be used in the timeline.

### Gate E — Full render QC

Sample the final render at scene boundaries and at regular intervals. A final export fails if planned effects silently disappeared, were bypassed, or rendered differently from approved proofs.

## 10. Fallback rule

If a PlayCanvas/3D technique cannot be made reliable with the available source, do not fake success.

Use the strongest physically plausible fallback:

1. PlayCanvas full 3D / Gaussian environment when viable;
2. PlayCanvas 2.5D scene with subject masks/depth layers;
3. high-quality FFmpeg/OpenCV compositing, retiming, grading, or optical treatment;
4. original footage preserved cleanly.

The fallback and reason must be recorded in the project decision log.

## 11. Reusable-effect promotion rule

Any new effect, shader, compositor, loop builder, analysis utility, transition, render pass, or reusable preset created during Irish Eyes must not remain trapped in the song branch.

- Develop and prove the effect on `song/irish-eyes` first.
- Once it passes effect-proof QC and is genuinely reusable, save/promote its generic implementation and documentation into the repository-wide reusable library on the canonical branch.
- This repository's canonical/default branch is `main`; treat `main` as the project-wide master branch unless the repository is deliberately renamed later.
- Project-specific parameters stay in `projects/irish-eyes`; generic effect code, shader code, reusable presets, and documentation belong under `general/reusable/` on `main`.
- A reusable effect must include purpose, required inputs, parameters, example usage, limitations, and proof/QC notes.
- Future songs should be able to call the effect without depending on Irish Eyes-specific paths.

## 12. Artifact/checkpoint rule

Keep production state recoverable on the `song/irish-eyes` branch.

At minimum preserve text/configuration artifacts for:

- source analysis;
- full-frame extraction manifest;
- loop candidates and loop QC;
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

## 13. No slideshow rule

The 31.77-second source cannot simply be looped, frozen, or converted into a sequence of slow zooms for a 3:07 song.

The finished video must contain meaningful motion generated from the real source world: original motion, retimed footage, living-frame motion, environmental extension, parallax, reconstructed camera travel, reflection/cloud/water movement, and music-driven optical behavior.

## 14. Restraint rule

The objective is not to show every available effect. The objective is a believable cinematic memory.

Use effects where the song asks for expansion. Return repeatedly to untouched or minimally treated real footage so the viewer never loses the photographic truth of the original moment.

## 15. Chat/workspace rule

Keep this production in the current ChatGPT project/chat workflow. Do not move Irish Eyes into ChatGPT Work or another workspace unless the user explicitly requests that move.

## 16. Final acceptance rule

Irish Eyes is not ready for delivery unless all of the following are true:

- the source subject is recognizable and photoreal throughout;
- effects are visibly present in the exported file, not only in plans/code;
- major effects have proof clips/frames and recorded settings;
- the edit contains genuine dimensional/environmental motion beyond zooms;
- source video has been exploited at frame level where useful rather than replaced unnecessarily;
- loops derived from the real footage pass seam and temporal-continuity QC;
- PlayCanvas/SuperSplat usage, when claimed, is tied to actual rendered assets;
- audio-reactive behavior is driven by measured song data;
- any new reusable effect created for Irish Eyes has a documented promotion path to `main/general/reusable/`;
- the final 3:07 sequence feels like one coherent South Florida memory rather than a demo reel.
