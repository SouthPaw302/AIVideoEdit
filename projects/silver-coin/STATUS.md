# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V5.1/V5.2 technically validated but aesthetically rejected as the target; production is pivoting to a hero-frame-first approach inspired by the strongest early IronFlame experiment

## Completed

- Locked **Living Pre-Raphaelite Folk Romanticism** as the primary visual language from the two supplied six-second reference clips.
- Locked **hybrid neural-radiance-field spatial rendering** as an available spatial method: a compact trained CPU NeRF supplies learned atmosphere/light while painted layers retain faces, hands, instruments, architecture, clothing, and narrative detail.
- Recovered the canonical `Silver Coin  (Remastered).wav` in the active runtime and verified SHA-256 `6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92`.
- Verified the re-uploaded style clips against the original recorded hashes.
- Ran the real audio edit-map analysis and recovered the working song structure:
  - Verse 1: 0:00–0:39.3
  - Chorus 1: 0:39.3–1:22.7
  - Verse 2: 1:22.7–1:43.7
  - Chorus 2: 1:43.7–2:18.2
  - Bridge: 2:18.2–3:03.3
  - Final Chorus: 3:03.3–3:27.4
- Recovered and cleaned a 29-scene narrative timeline from storyboard material.
- Built reusable CPU effects, compact NeRF volume rendering, reference-motion calibration, narrative-ribbon reframing, audio analysis, and temporal QC tooling.
- Rendered complete V5.1 source and V5.2 720p delivery encode.
- V5.1/V5.2 passed technical/container/temporal QC.

## User aesthetic review — decisive pivot

The user reported that the very first IronFlame video, built around a single static picture, looked better than Silver Coin V5/V5.2.

Treat this as a production correction, not a minor preference.

### Lesson

Technical complexity is not visual quality. V5 accumulated too many competing operations: frequent scene changes, warps, particles, parallax, transitions, depth changes, reframing, and audio-reactive motion. The result is more sophisticated on paper but gives the viewer less time to inhabit a strong composition.

### New production rule

**Hero image first. Effects must earn their existence.**

For the next Silver Coin pass:

1. Start from one exceptional hero painting or a very small number of exceptional paintings.
2. Preserve the image almost completely; do not deform faces, hands, instruments, clothing, or architectural anchors.
3. Prefer slow camera drift, crop movement, light change, smoke/mist/rain, reflection, and restrained NeRF atmosphere over mesh warping.
4. Let audio drive intensity of atmosphere/light/camera energy rather than forcing a new shot on every section or transient.
5. Use the silver coin as an occasional visual anchor, not a constant transition gimmick.
6. Keep long visual dwell times. A composition that deserves attention should stay on screen long enough to become a world.
7. Judge each effect by subtraction: if removing it makes the image stronger, remove it.
8. Technical QC remains necessary but cannot substitute for aesthetic judgment.

## Current approved direction

Build Silver Coin V6 as a **minimal living painting** rather than a multi-panel animated storyboard.

Target feeling: one beautiful painted world slowly breathing with the song.

Preferred motion hierarchy:

1. camera drift / slow push / reframing
2. practical light and shadow response
3. smoke, mist, rain, embers, reflections
4. subtle NeRF volumetric atmosphere
5. rare object glint or portal moment
6. local deformation only when absolutely necessary

The hybrid NeRF remains available, but it must stay subordinate to the hero image. Do not add an effect merely because the renderer can produce it.

## Historical V5 artifacts

See `DELIVERY_V52.json` and `V51_QC_REPORT.json`.

- `Silver_Coin_V51_Full.mp4`
- `Silver_Coin_V52_720p_Delivery.mp4`

These remain useful technical experiments and regression references, but they are **not the aesthetic target**.

## Exact next action

Select or create the strongest single Silver Coin hero composition, build a restrained 20–30 second V6 living-painting proof against the real master, compare it aesthetically to V5, then extend only if the minimal approach is clearly stronger.

## Checkpoint rule

After every meaningful production/tooling phase, update GitHub before moving on so another agent can resume from the branch without the original chat.