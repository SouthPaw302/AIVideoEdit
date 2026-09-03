# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V5/V5.2 are historical technical experiments. V6 is being rebuilt from the two user-supplied sample videos themselves; sample A's opening blonde flower-crowned woodland woman is the recurring protagonist/style anchor.

## Decisive user correction

The earlier diagnosis that Silver Coin simply needed fewer images was incomplete.

The user clarified that the main problem is **the image set itself**. The old tavern/laborer storyboard did not match the quality or visual identity of the supplied sample videos.

### Current canonical visual rule

**Recreate the film from the visual language contained in the two sample videos.**

- Sample A: `imagine-d04b484c.mp4`
- Sample B: `imagine-5558fc80.mp4`
- The first scene of sample A, featuring the blonde flower-crowned woman in the green woodland, is the starting character and world anchor.
- Extract frames from the sample videos and use those frames to define face/character continuity, painting surface, palette, lighting, vegetation, costume/fabric language, composition, camera behavior, and motion feel.
- Build an entirely new Silver Coin storyboard whose scenes look as though they belong to the same painted world.
- The recovered V5 tavern/laborer panels may inform narrative beats only; **their image designs are rejected as the final visual source.**

## GitHub source-video recovery

The branch now contains each source clip separately as a dedicated full-duration visual recovery proxy:

- `projects/silver-coin/references/source-clips/imagine-d04b484c-github-reference.mp4`
- `projects/silver-coin/references/source-clips/imagine-5558fc80-github-reference.mp4`

These are lightweight 96x96/4fps silent GitHub recovery proxies made from the canonical uploads. They are intentionally small enough to persist through the repository connector while retaining the complete visual sequence of each six-second clip.

The canonical originals remain the uploaded 560x560/24fps files, identified permanently by SHA-256 in `ASSET_MANIFEST.json`. Do not confuse the GitHub proxy encode with the original binary.

## Canonical audio / structure

Canonical audio: `Silver Coin  (Remastered).wav`  
SHA-256: `6b6d7a134959086157f88baf3751718597bf61f73886a48281f6d8b2c3361a92`  
Duration: 207.44 s

Working structure derived from the real master:

- Verse 1: 0:00–0:39.3
- Chorus 1: 0:39.3–1:22.7
- Verse 2: 1:22.7–1:43.7
- Chorus 2: 1:43.7–2:18.2
- Bridge: 2:18.2–3:03.3
- Final Chorus: 3:03.3–3:27.4

## Reusable production technology retained

The technical work from V3–V5 remains useful **after** the new image set is correct:

- audio edit-map analysis
- compact CPU neural-radiance-field atmosphere
- pseudo-depth / parallax
- restrained atmosphere, rain, smoke, embers, reflection, practical light
- object/coin match transitions
- reference-motion calibration
- temporal QC

Do not use effects to compensate for weak source imagery.

## Historical V5 artifacts

- `Silver_Coin_V51_Full.mp4`
- `Silver_Coin_V52_720p_Delivery.mp4`

They passed technical/container/temporal QC but are not the aesthetic target.

## Exact next action

1. Extract representative and sequential frames from both canonical sample videos.
2. Build a visual/character bible from sample A's opening woman and both clips' painterly environment/motion language.
3. Create a new full-song storyboard with the woman recurring through Silver Coin's narrative.
4. Generate/QC the new consistent scene set before animation.
5. Apply the existing rendering/effects stack only after the storyboard passes visual QC.
6. Assemble against the real 207.44-second master and checkpoint every meaningful phase to GitHub.

## Checkpoint rule

After every meaningful production/tooling phase, update GitHub before moving on so another agent can resume without the original chat.
