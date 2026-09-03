# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V6 is being rebuilt directly from the two user-supplied sample videos. The blonde flower-crowned woodland woman from sample A is the recurring protagonist and visual anchor. The first 39.3-second music-directed motion proof is rendered and QC'd; reusable camera/effect presets are now committed.

## Canonical visual rule

**Recreate Silver Coin from the visual language contained in the two sample videos themselves.**

- Sample A: `imagine-d04b484c.mp4`
- Sample B: `imagine-5558fc80.mp4`
- Sample A's opening woman defines protagonist identity, face, hair, crown, costume family, painted surface, palette and woodland world.
- The old tavern/laborer storyboard may inform narrative beats only. Its visual designs are rejected.

## V6 storyboard progress

Completed:

- Verified both canonical uploads: 560x560, 24 fps, 6.041667 s each.
- Extracted **24 exact representative sample frames** from the two originals.
- Locked the recurring woman and world continuity in `V6_STORYBOARD_PLAN.md`.
- Created a full 20-beat V6 story from woodland -> village/work -> tavern -> fiddle/dance -> merchant/coin -> defiance -> night threshold -> dawn/woodland return.
- Added `V6_REFERENCE_FRAME_INDEX.md` for continuity/QC recovery.
- Built a local storyboard blueprint using only the supplied sample-video imagery as the visual source.
- Generated the first four final-direction 16:9 paintings: forest/coin, village path, workers at sunset, and twilight inn.

## V6 music-directed motion proof

Rendered opening proof against the real master:

- Duration: **39.333333 s**
- Delivery: **1280x720 H.264, 12 fps + AAC audio**
- Local artifact: `Silver_Coin_V6_Opening_MusicDirected_720p.mp4`
- SHA-256: `b2be989731d3ffe0f8e1ffbd6a3a73e1d43b03932a237948ca4dbbac1c22bd6a`

Scene mapping:

- 0:00–0:10 `forest_coin`
- 0:10–0:20 `path_reveal`
- 0:20–0:30 `labor_end`
- 0:30–0:39.3 `threshold_gold`

Music directs:

- transient-qualified micro zooms
- slow push/pull speed
- lateral crop travel
- sub-degree angle drift/settle
- exposure/practical-light response
- section transition timing

Reusable effects used:

- 2D Gaussian light-splat atmosphere
- Gaussian-defocus light bridge transition
- stable vignette
- warm/cool threshold response
- wet-road shimmer
- non-destructive crop/parallax-like travel

Important terminology guard: the Gaussian light field in this proof is **2D image-space Gaussian diffusion/splats**, not true 3D Gaussian Splatting.

## Reusable files added

- `projects/silver-coin/V6_EFFECT_PRESETS.json`
- `projects/silver-coin/V6_MUSIC_CAMERA_GRAMMAR.md`
- `projects/silver-coin/V6_OPENING_MOTION_META.json`
- `tools/video_fx/render_music_directed_living_painting.py`

## GitHub source-video recovery

The branch contains each sample separately as a lightweight full-duration visual recovery proxy:

- `projects/silver-coin/references/source-clips/imagine-d04b484c-github-reference.mp4`
- `projects/silver-coin/references/source-clips/imagine-5558fc80-github-reference.mp4`

The canonical originals remain the uploaded 560x560/24fps files; their SHA-256 hashes and metadata in `ASSET_MANIFEST.json` are authoritative.

## Canonical audio / structure

Audio: `Silver Coin  (Remastered).wav`  
SHA-256: `6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92`  
Duration: 207.44 s

Working structure:

- Verse 1: 0:00–0:39.3
- Chorus 1: 0:39.3–1:22.7
- Verse 2: 1:22.7–1:43.7
- Chorus 2: 1:43.7–2:18.2
- Bridge: 2:18.2–3:03.3
- Final Chorus: 3:03.3–3:27.4

## Production rule

The static artwork must be excellent before animation. Use the full bag of tricks—loops, zooms, changing angles, Gaussian atmosphere, NeRF depth, reflections, light, transitions, audio cues—but only when the music asks for them and without damaging the painting.

## Exact next action

1. Finish generating/QC'ing the remaining V6 hero paintings with the same woman and sample-video visual language.
2. Build the chorus motion presets (`first_toast`, `chorus_clap`, `fiddler_energy`, `communal_dance`).
3. Extend the music-directed renderer through Chorus 1.
4. Continue section by section to the 207.44-second master.
5. Checkpoint every useful effect/method and every meaningful render phase to GitHub.

## Checkpoint rule

After every meaningful production/tooling phase, update GitHub before moving on so another agent can resume without the original chat.
