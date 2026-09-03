# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V4 hybrid NeRF visual pass working with 21 cleaned narrative frames; reusable effects, NeRF, and audio-analysis tools are committed; canonical WAV bytes are now the blocking dependency for full-song timing/sync

## Completed

- User explicitly selected Neural Radiance Fields as the spatial rendering method.
- Created dedicated branch `song/silver-coin` and persisted project recovery/style decisions.
- Fingerprinted the canonical 207.440-second remastered WAV and indexed its Library reference.
- Inspected both six-second visual reference clips and locked **Living Pre-Raphaelite Folk Romanticism** as the primary visual language.
- Added the style and rendering decisions to repository-wide recovery/catalog documentation.
- Built and QC'd the first ten recovered Silver Coin narrative keyframes.
- Recovered an expanded **21-frame** painted narrative set covering village labor, miller, wagon, first toast, chorus, fiddler, merchant/barmaid, empty cup, silver coin, defiance, chorus returns, and final celebratory images.
- Removed left-edge storyboard titles and bottom lyric/caption contamination through deterministic crop/recomposition rather than generative inpainting.
- Implemented reusable CPU painterly effects: pseudo-depth parallax, localized mesh motion, advected atmosphere, motivated rain/embers, firelight breath, wet reflection ripple, heat haze, motivated light shafts, portrait depth-focus breath, localized metal/coin glint, performance transient warp, pigment dissolve, object/coin portal, and temporal canvas lock.
- Added reusable effect code under `tools/video_fx/` and documented the methods in `docs/EFFECTS_METHOD_CATALOG.md`.
- Added `tools/audio/analyze_edit_map.py`; synthetic validation correctly recovered deliberately placed section changes and produced beat/transient/sync candidates.
- Implemented `tools/video_fx/tiny_nerf_volume.py`, an actual compact trained MLP mapping 3D position + view direction to density/RGB using Fourier features and CPU volume rendering.
- Produced V4 local QC using all 21 cleaned frames plus five trained NeRF scene-family fields (`village`, `threshold`, `tavern`, `coin`, `dawn`).
- Recorded V4 train/validation metrics and QC configuration in `NERF_V4_QC.json`.

## V4 NeRF validation metrics

V4 QC used seed 302, 5,500 samples and 80 training steps per family.

- village validation MSE: ~0.1329
- threshold validation MSE: ~0.1327
- tavern validation MSE: ~0.1447
- coin validation MSE: ~0.1859
- dawn validation MSE: ~0.1578

The NeRF remains a low-opacity learned atmospheric/light volume; the painted keyframes retain faces, hands, instruments, clothing, architecture, and narrative detail.

## Current approved direction

Maintain the visibly hand-painted Pre-Raphaelite folk-romantic world while making it feel continuously alive. Use coherent camera/depth motion, controlled cloth/crowd movement, motivated rain/embers, smoke/mist, wet reflection, fire/candle response, performance transients, and brief coin-driven transitions.

Allowed technical description: **hybrid neural-radiance-field spatial rendering**.

Do not describe this as photogrammetric scene reconstruction, Nerfstudio, Instant-NGP, or a physically complete 3D model.

## Canonical source assets

See `ASSET_MANIFEST.json`.

- Audio: `Silver Coin  (Remastered).wav`
- Style clip A: `imagine-d04b484c.mp4`
- Style clip B: `imagine-5558fc80.mp4`
- GitHub still: `references/living-pre-raphaelite-style-reference.jpg`
- GitHub motion preview: `references/living-pre-raphaelite-motion-preview.mp4`

## Blocking dependency

The Library metadata for the canonical WAV is available, but the active runtime receives HTTP 403 when attempting to materialize the WAV bytes. Full song analysis/sync therefore requires the user to attach `Silver Coin  (Remastered).wav` to the active production chat.

No other file is currently required.

## Not completed

- Real audio edit map for the 207.440-second master.
- Verified full lyric transcription/timing.
- Audio-driven rather than placeholder performance transient envelopes.
- Final scene durations/cut points.
- Full 207.440-second 16:9 master render with canonical audio.
- Final continuity/artifact QC and archive.

## Exact next action

1. Receive/mount the canonical WAV bytes.
2. Run `tools/audio/analyze_edit_map.py` and commit the real edit-map JSON/overview.
3. Verify lyric/section labels against the waveform/listening pass.
4. Replace preview-cycle transients with audio-derived envelopes for fiddle, foot stamps, coin glints, light, camera, and transitions.
5. Assemble the 21-frame/NeRF/effects production into the complete 207.440-second timeline.
6. QC, repair, final render, archive, and update GitHub.

## Checkpoint rule

After each meaningful production or tooling phase, update this file and affected manifest/decision/method files on GitHub before continuing.
