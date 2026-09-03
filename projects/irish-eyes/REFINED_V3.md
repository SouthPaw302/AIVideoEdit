# Irish Eyes — Refined V3

Source: `IRISH_EYES_FULL_ROUGH_v2_BROLL.mp4`

## Refinement goals completed

- replaced hard B-roll boundaries with short overlapping crossfades centered on the existing song-structure cut points;
- preserved total video timing by overlapping source windows instead of shortening the timeline;
- preserved the existing song audio track without remixing or re-encoding its content;
- applied one restrained unifying image treatment across the full movie:
  - contrast 1.025
  - brightness +0.003
  - saturation 1.035
  - gamma 0.995
  - slight warm balance: R +0.010, G +0.003, B -0.008
  - subtle unsharp recovery 0.20
- normalized every transition segment to 30 fps / common timebase before crossfade to prevent render instability.

## Transition anchors

The refined transitions are centered on:

- 00:57.59
- 01:08.45
- 01:19.31
- 01:27.31
- 01:39.40
- 01:49.40
- 02:11.56
- 02:21.56

Transition duration: 0.45 seconds each.

These anchors retain the established Act II / Act III structural timing rather than drifting the edit away from the song.

## Render strategy

The complete filter graph was too expensive for one runtime render window, so it was rendered as three contiguous video-only chunks (0–75 s, 75–125 s, 125 s–end), using identical encoding and grading parameters. The chunks were concatenated and then remuxed with the unchanged V2 audio stream.

This is a production workaround only; it does not alter scene timing or effect behavior.

## Output

`IRISH_EYES_REFINED_V3.mp4`

- resolution: 720x1280
- frame rate: 30 fps
- video codec: H.264 / yuv420p
- audio codec: AAC, copied from Rough V2
- container duration: 187.033333 s
- video frames: 5611
- audio duration: 186.986 s (same carried source stream behavior as V2)
- file size: 235,466,589 bytes
- SHA-256: `c1e4485ab0be26ad20297f5db1fc257c247dca69cc15d991cc98eb01681844c1`

## QC

- no black-frame runs >= 0.15 s detected;
- no freeze runs >= 1.5 s detected;
- video remains 720x1280 at constant 30 fps;
- audio remains present and unchanged in content from Rough V2;
- transition points no longer use abrupt hard cuts;
- global grade is intentionally restrained to preserve documentary realism and Brandi's photographic identity.

## Status

Refined V3 is the current review master. Further changes should be driven by visual review or newly supplied B-roll rather than another storyboard/concept pass.
