# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V3.1 CPU living-painting effects stack implemented and QC-cleaned; reusable renderer/method docs committed; full-song audio edit map and final NeRF-integrated assembly remain in progress

## Completed

- User explicitly selected Neural Radiance Fields as the spatial rendering method.
- Runtime capability checked: no GPU, PyTorch, Nerfstudio, COLMAP, or packaged NeRF stack is available.
- Locked an honest CPU hybrid: a compact trained neural radiance-field MLP supplies volumetric density/color and view-dependent atmosphere, composited with painted multi-plane scenes. This is not described as full photogrammetric reconstruction.
- Created dedicated branch `song/silver-coin`.
- Fingerprinted and inspected the canonical remastered WAV metadata.
- Inspected both supplied six-second visual reference clips across their timelines.
- Named the visual language **Living Pre-Raphaelite Folk Romanticism**.
- Added that style to the repository-wide visual style catalog.
- Defined Silver Coin's project-specific visual DNA and effects plan.
- Recorded original filenames, technical metadata, SHA-256 hashes, and Library references.
- Created a small GitHub contact sheet and motion preview so future agents can identify the style without the original chat attachments.
- Indexed Silver Coin in the repository and project recovery files.
- Recovered ten useful narrative keyframes from the existing Silver Coin storyboard for local production tests.
- Built V2 motion preview proving painterly upscale, depth-derived parallax, advected atmosphere, motivated rain/embers, firelight breathing, pigment dissolve, and silver-coin portal transitions.
- Built V3 motion methods adding localized micro-warp, depth-gated volumetric light, wet-ground reflection shimmer, and chroma pigment transport.
- Rejected the first V3 cleanup because residual storyboard title fragments remained visible.
- Replaced broad inpainting with deterministic edge reframing; V3.1 cleaned keyframes passed visual inspection with title fragments removed.
- Added reusable repo tooling: `tools/video_fx/painterly_cpu_fx.py` and `tools/video_fx/render_painterly_sequence.py`.
- Added repository-wide `docs/EFFECTS_METHOD_CATALOG.md` and project-specific `FX_METHODS.md`.
- Added `render-config-v3.json` so the current scene-family/effect configuration is recoverable by future agents.

## Current approved direction

Apply the reference clips' luminous, visibly painted, Pre-Raphaelite folk-romantic surface and natural animation to Silver Coin's own village/road/tavern narrative. The blonde flower-crowned woman and square framing are not mandatory story elements.

Motion should read as a living painting rather than a slideshow or a morph demo: coherent parallax, cloth/crowd micro-motion, motivated weather/embers, smoke/mist, firelight, wet reflections, and selective object-driven transitions.

## Canonical source assets

See `ASSET_MANIFEST.json`.

- Audio: `Silver Coin  (Remastered).wav`
- Style clip A: `imagine-d04b484c.mp4`
- Style clip B: `imagine-5558fc80.mp4`
- GitHub still: `references/living-pre-raphaelite-style-reference.jpg`
- GitHub motion preview: `references/living-pre-raphaelite-motion-preview.mp4`

## Not completed

- Canonical lyrics have not yet been fully recovered and verified in this branch.
- Full audio analysis, beats, sections, transitions, and high-value sync points have not yet been committed.
- Recurring character identity sheets are not yet locked beyond the recovered storyboard imagery.
- The compact trained CPU NeRF layer described in `NERF_PLAN.md` has not yet been integrated into the V3.1 sequence renderer.
- The final 207.440-second master timeline has not yet been assembled.
- The original full-resolution reference clips remain external; GitHub contains reduced recovery previews.

## Exact next action

1. Obtain usable runtime bytes for the canonical WAV and analyze the full 207.440-second master into an edit map.
2. Recover/verify lyrics and align the known narrative to song sections without inventing missing words.
3. Add audio-derived transient/energy envelopes to the reusable renderer.
4. Integrate the compact CPU NeRF atmosphere/radiance layer into the approved scene families.
5. Expand/repair production imagery as needed, then assemble the full-song 16:9 draft.
6. Run artifact/continuity QC, repair failures, render final master, archive outputs, and update GitHub.

## Dependency rule

Do not ask the user for files preemptively. The canonical WAV is indexed in the project Library. If the runtime cannot access its bytes when Step 1 begins, then request that exact WAV in the active production chat.

## Checkpoint rule

After each meaningful production or tooling phase, update this file and any affected manifest/decision/method files on GitHub before continuing.
