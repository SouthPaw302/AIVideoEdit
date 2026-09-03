# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** Full-length V5.1 hybrid-NeRF/audio-reactive render validated; V5.2 720p painterly delivery encode complete; temporal QC passed with zero unexplained risks

## Completed

- Locked **Living Pre-Raphaelite Folk Romanticism** as the primary visual language from the two supplied six-second reference clips.
- Locked **hybrid neural-radiance-field spatial rendering** as the spatial method: a compact trained CPU NeRF supplies learned atmosphere/light while painted layers retain faces, hands, instruments, architecture, clothing, and narrative detail.
- Recovered the canonical `Silver Coin  (Remastered).wav` in the active runtime and verified SHA-256 `6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92`.
- Verified the re-uploaded style clips against the original recorded hashes.
- Ran the real audio edit-map analysis and recovered the working song structure:
  - Verse 1: 0:00–0:39.3
  - Chorus 1: 0:39.3–1:22.7
  - Verse 2: 1:22.7–1:43.7
  - Chorus 2: 1:43.7–2:18.2
  - Bridge: 2:18.2–3:03.3
  - Final Chorus: 3:03.3–3:27.4
- Recovered and cleaned a 29-scene narrative timeline from the storyboard material.
- Removed storyboard titles/captions by deterministic crop/recomposition rather than large generative inpainting.
- Calibrated motion against the supplied reference clips. At 280 px analysis width, measured mean optical flow was ~0.428 px/frame for the quieter reference and ~1.566 px/frame for the more active reference.
- Audio-reactive V5 controls drive camera/parallax, localized painted motion, atmosphere/fire/haze, rain/embers/glints, fiddler bow response, and light shafts from the actual master.
- Rebuilt the bridge as a **narrative ribbon** preserving the multi-character storyboard composition and moving the camera farmer → smith → carter → maid → lovers → dawn → wine.
- Rendered complete V5.1 source: `Silver_Coin_V51_Full.mp4`.
- Validated V5.1 container: H.264 854×480 at 15 fps + 48 kHz stereo AAC, 207.466667 s.
- V5.1 SHA-256: `21a51d8e0ca6ae9bba5d2a6442ea74055513597eebab9ce08d9328342870fdd4`.
- Added reusable temporal QC scanner at `tools/video_qc/temporal_qc.py`.
- Temporal QC result: 50 expected transition/motion events and **0 unexplained temporal risks** using robust z-score plus absolute magnitude floors. See `V51_QC_REPORT.json`.
- Created V5.2 painterly delivery encode: `Silver_Coin_V52_720p_Delivery.mp4`, 1280×720 at 15 fps, 207.466667 s.
- V5.2 SHA-256: `1e3099dd6dd0fbc93192098176d9763045fad263f2364050cc79cd83f9e3d2ed`.
- V5.2 is explicitly documented as a Lanczos/upscale delivery from the validated 854×480 source, not as native 720p scene rendering.
- Expanded `docs/EFFECTS_METHOD_CATALOG.md` with reference-motion calibration, narrative-ribbon reframing, temporal QC, and documented painterly delivery-upscale rules.

## Current approved direction

Maintain the visibly hand-painted folk-romantic world while making it continuously alive through restrained depth/camera motion, cloth/crowd movement, motivated rain/embers, smoke/mist, wet reflection, fire/candle response, audio transients, and brief coin-driven transitions.

Allowed technical description: **hybrid neural-radiance-field spatial rendering**.

Do not describe this as photogrammetric scene reconstruction, Nerfstudio, Instant-NGP, or a physically complete 3D model.

## Delivery artifacts

See `DELIVERY_V52.json` and `V51_QC_REPORT.json`.

- Native validated working render: `Silver_Coin_V51_Full.mp4`
- Current delivery encode: `Silver_Coin_V52_720p_Delivery.mp4`
- Large video binaries are runtime delivery artifacts; GitHub stores the reproducible code, timing data, hashes, method documentation, and QC records.

## Remaining improvement work

- User review of V5.2 pacing, scene selection, and overall visual feel.
- Optional targeted repair if user identifies a scene that should be replaced or re-framed.
- Optional higher-resolution native rerender when a faster/GPU render environment is available; do not confuse an upscale with native rendering.
- Continue expanding reusable effects/method documentation as new methods prove useful.

## Checkpoint rule

After every meaningful production/tooling phase, update GitHub before moving on so another agent can resume from the branch without the original chat.