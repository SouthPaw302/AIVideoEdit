# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** V6 is being rebuilt directly from the two user-supplied sample videos. The blonde flower-crowned woodland woman from sample A is the recurring protagonist and visual anchor; the rejected V5 tavern/laborer image set is no longer the visual source.

## Canonical visual correction

The user clarified that the principal problem with V5 was the **image set**, not simply the amount of motion.

Current rule:

**Recreate Silver Coin from the visual language contained in the two sample videos themselves.**

- Sample A: `imagine-d04b484c.mp4`
- Sample B: `imagine-5558fc80.mp4`
- Sample A's opening woman defines protagonist identity, face, hair, crown, costume family, painted surface, palette and woodland world.
- The old tavern/laborer storyboard may inform narrative beats only. Its visual designs are rejected.

## V6 progress

Completed:

- Verified both canonical uploads: 560x560, 24 fps, 6.041667 s each.
- Extracted a 2 fps representative sequence from both originals: **24 exact sample frames total**.
- Confirmed both samples depict the same recurring blonde flower-crowned woman in the same woodland painting language.
- Locked character continuity and world rules in `V6_STORYBOARD_PLAN.md`.
- Created the full 20-beat Silver Coin V6 storyboard around her:
  woodland -> village/workers -> warm tavern -> first toast -> fiddler/dance -> merchant/coin -> defiance -> communal chorus -> night threshold -> woodland before dawn -> final coin/flower image.
- Added `V6_REFERENCE_FRAME_INDEX.md` so future agents can recover the exact reference-frame progression and QC rules.
- Built a local V6 storyboard blueprint using only frames extracted from the canonical sample videos as the continuity imagery.

## GitHub source-video recovery

The branch contains each sample separately as a lightweight full-duration visual recovery proxy:

- `projects/silver-coin/references/source-clips/imagine-d04b484c-github-reference.mp4`
- `projects/silver-coin/references/source-clips/imagine-5558fc80-github-reference.mp4`

These are intentionally reduced 96x96/4fps silent proxies because the current repository connector cannot stream the multi-megabyte original runtime binaries directly into GitHub. The canonical originals remain the uploaded 560x560/24fps files; their SHA-256 hashes and metadata in `ASSET_MANIFEST.json` are authoritative.

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

## Reusable technology retained

Keep the good technical work, but apply it only after the new image set is right:

- audio edit-map analysis
- compact CPU NeRF atmosphere
- restrained pseudo-depth/parallax
- smoke/mist/rain/embers/reflections/practical light
- coin/object match transitions
- reference-motion calibration
- temporal QC

Do not use effects to compensate for weak imagery.

## Exact next action

1. Use the 24-frame sample sequence as the character/style continuity sheet.
2. Produce the new V6 scene images for the 20 storyboard beats, keeping the same woman and painting language.
3. QC each scene against the sample frames before animation.
4. Animate only accepted images with the existing rendering/effects stack.
5. Assemble against the real 207.44-second master.
6. Checkpoint every meaningful phase to GitHub.

## Checkpoint rule

After every meaningful production/tooling phase, update GitHub before moving on so another agent can resume without the original chat.
