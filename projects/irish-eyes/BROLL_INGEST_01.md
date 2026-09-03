# Irish Eyes — B-roll Ingest 01 / Rough V2

Three user-supplied real video assets were ingested for the refinement pass.

## Source files

1. `1adc3ba8-677a-45bf-b464-1b311c1bc751-1_all_4447.mp4`
   - 1280x720, 30 fps, H.264
   - duration: 19.365442 s
   - SHA-256: `e4d65b418c0bf296a982af7ae803abbeeade8b065fdd47ec1fe05de68542116c`
   - content role: brighter storm/shoreline horizon with isolated human figure; useful as a memory/landscape cutaway.

2. `1adc3ba8-677a-45bf-b464-1b311c1bc751-1_all_4448.mp4`
   - 1280x720, 30 fps, H.264
   - duration: 68.399311 s
   - SHA-256: `e903b359d057204a8e017f506a86fd3efb0130b79387606c46d17cdb2b3f245d`
   - content role: darker storm-horizon shoreline with centered figure and dramatic cloud mass; strong Act II memory-world material.

3. `1adc3ba8-677a-45bf-b464-1b311c1bc751-1_all_4449.mp4`
   - 1280x720, 30 fps, H.264
   - duration: 67.565989 s
   - SHA-256: `eed249d26e5199b5569c3c4acfc945ab73d9752ee8940c299e42a41ac2154a25`
   - content role: South Florida beachfront / palm / high-rise environment; provides a different real-world visual layer from the waterfront portrait footage.

## Vertical adaptation

The final Irish Eyes movie remains 720x1280 / 30 fps. These landscape clips were reframed as true moving vertical footage rather than still-image crops:

- scale to full portrait height;
- crop/reframe around the active subject/environment;
- restrained contrast / saturation / gamma matching;
- subtle warm balance where useful;
- light unsharp recovery;
- no generated face/body content.

Processed assets:

- `broll_storm_4448.mp4` — SHA-256 `6e93c4cad6ebf0e8186b704bec64515f96eacf1fdccf5ec06037df1a1469cb5e`
- `broll_shore_4447.mp4` — SHA-256 `90b575363066eab286a412f2de2abe805384dc40078800aeed2e3a0f1f680c8e`
- `broll_palms_a.mp4` — SHA-256 `fdc38536ac49663db83c85816c2ea173dd0f26b61520c2a4396fc4e761b89832`
- `broll_palms_b.mp4` — SHA-256 `eb8e7985145d49187ebee5038b0335664ad927fbcdcfc3562dd6fba578df8294`

## Rough V2 replacement windows

The first 3:07 rough was visually too repetitive, so real B-roll replaced selected sections while preserving the existing song audio and overall duration.

Replacement windows in `IRISH_EYES_FULL_ROUGH_v2_BROLL.mp4`:

- 00:57.59–01:08.45 — storm-horizon B-roll from 4448
- 01:19.31–01:27.31 — brighter shoreline B-roll from 4447
- 01:39.40–01:49.40 — South Florida high-rise/palm B-roll from 4449, reframe A
- 02:11.56–02:21.56 — South Florida high-rise/palm B-roll from 4449, reframe B

All other sections continue from Rough V1 for this pass.

## Rough V2 render

`IRISH_EYES_FULL_ROUGH_v2_BROLL.mp4`

- duration: 187.006703 s
- resolution: 720x1280
- frame rate: 30 fps
- video: H.264 / yuv420p
- audio: original AAC track carried unchanged from Rough V1
- file size: 72,627,468 bytes
- SHA-256: `bc5e43ae74cbab7bf992db9b7e7715ce7dc5edfde33f44013a0cef8aff79156d`

## QC result

Representative contact-sheet QC confirms the refinement successfully breaks up the previous visual repetition with:

- real storm shoreline motion;
- real dramatic horizon/cloud movement;
- real palm/high-rise South Florida environment;
- repeated returns to Brandi as the identity/reality anchor.

No storyboard or concept-image asset was created for this pass.

## Next refinement target

Continue replacing repetitive sections with real or purpose-built moving assets, improve transitions at the B-roll boundaries, then unify grade and lyric timing before final master render.
