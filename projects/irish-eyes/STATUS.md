# Irish Eyes — Final Status

Branch: `song/irish-eyes`

## Production state

**V1.3 FINAL COMPLETE / FULL EXPORT QC PASSED.**

Irish Eyes is a completed 16:9 Mountain Noir music film. V1.3 supersedes V1.2 only because the user supplied a distinct remastered WAV after V1.2 picture lock. The accepted V1.2 picture was preserved bit-for-bit at the H.264 elementary-stream level; V1.3 is an audio revision, not a picture rebuild.

## Canonical artistic master

File: `IRISH_EYES_V1_3_FINAL_YouTube_720p30.mp4`

- 1280x720 / 16:9 / 30 fps
- H.264 / yuv420p / Rec.709-tagged
- AAC-LC stereo / 48 kHz / ~320 kb/s
- picture duration: 187.133333 s
- song audio duration: 187.120000 s
- bytes: 232,364,425
- SHA-256: `d0ace58c5e2b226cd08a928fc6f9b5ebcd3e2a949805adaa37fc94647ba603ae`
- Library path: `/Video Creation/Irish Eyes/Final/IRISH_EYES_V1_3_FINAL_YouTube_720p30.mp4`
- Library ID: `libfile_188ada3ee1c88191ae217eeb834402cd`

This is the canonical artistic film and ends on the water/light ending without the separate post-roll channel card.

## Canonical YouTube upload package

File: `IRISH_EYES_V1_3_FINAL_UPLOAD_WITH_OUTRO_720p30.mp4`

- 1280x720 / 30 fps
- H.264 + AAC-LC stereo / 48 kHz
- duration: 192.154000 s
- bytes: 238,095,490
- SHA-256: `857b690b49e29724bcd625998e79f2fdc4873dc201c238628952ad4f53cc0763`
- Library path: `/Video Creation/Irish Eyes/Final/IRISH_EYES_V1_3_FINAL_UPLOAD_WITH_OUTRO_720p30.mp4`
- Library ID: `libfile_0c67dfde60ec8191a37a97e520139892`

The extra runtime is the separate Mountain Noir post-film card; the artistic film remains the 187.13 s master above.

## Authoritative audio source

The user-supplied remaster is now canonical:

`Irish eyes (Remastered) FINAL SOURCE.wav`

- 187.120000 s
- 48 kHz / stereo / PCM 16-bit
- bytes: 35,927,212
- SHA-256: `b4255e04f31cf7c137ceea82222138c9e07ccc27de4aa8b83b8334814c4d5f46`
- integrated loudness: approximately -15.0 LUFS
- loudness range: 5.7 LU
- true peak: approximately -2.4 dBFS
- Library ID: `libfile_721852b16ee4819187b553f2e13f459a`

See `AUDIO_REVISION_V1_3.md`.

## Picture identity / QC inheritance

The V1.3 artistic-master video stream has MD5 `9f65035bc4bccd4716c22a1f8767a11f`, identical to V1.2. The V1.3 upload-with-outro video stream has MD5 `cab7b37955fd3fcead3a68b4d529099a`, also identical to V1.2.

Therefore the V1.2 picture QC remains valid without a lossy picture re-render:

- no black-frame events at the production threshold;
- earlier freeze tells near ~20.7 s and ~51.0 s were already repaired before V1.2;
- stricter 0.30 s low-motion candidates near ~73.23 s and ~102.10 s were manually cleared as intentional continuous motion;
- no sideways source footage;
- no blurred portrait sidebars;
- no accepted duplicate-Brandi or mirrored L18 construction;
- final refrain progressively returns to photographic reality;
- water/light ending preserved.

The V1.3 container also passed full video decode verification after remuxing the new audio.

## Final picture lineage

Landscape closeout remains unchanged from V1.2:

- L18 V3 — KEEP
- L20 Water→Wet Road V3 — KEEP
- L21 Road/Rain-Glass V3 — KEEP
- L22 Warm Window/Candle V1 — KEEP
- L23 Dark Lake/Ridge V2 — KEEP

See `LANDSCAPE_NATIVE_BATCH_02.md`, `ROUGH_CUT_16X9_V1_QC.md`, `FINAL_MASTER.md`, `FINAL_QC.md`, and `AUDIO_REVISION_V1_3.md`.

## Completion rule

No further production work is required for V1.3. Future changes must increment the version and are revisions, not completion blockers.
