# Irish Eyes — Final Export QC

Canonical master: `IRISH_EYES_V1_3_FINAL_YouTube_720p30.mp4`
Status: **PASS**

## V1.3 scope

V1.3 is an audio revision only. The accepted V1.2 H.264 picture stream was copied without re-encoding, so all V1.2 visual/freeze repairs remain exactly preserved.

## Stream verification

Final artistic master:

- video: H.264 / yuv420p / Rec.709-tagged
- dimensions: 1280x720
- frame rate: 30/1
- picture duration: 187.133333 s
- audio: AAC-LC
- sample rate: 48,000 Hz
- channels: 2
- song audio duration: 187.120000 s
- size: 232,364,425 bytes
- SHA-256: `d0ace58c5e2b226cd08a928fc6f9b5ebcd3e2a949805adaa37fc94647ba603ae`

YouTube upload package with outro:

- duration: 192.154000 s
- size: 238,095,490 bytes
- SHA-256: `857b690b49e29724bcd625998e79f2fdc4873dc201c238628952ad4f53cc0763`

## Picture identity verification

Artistic master video-stream MD5:
- V1.2: `9f65035bc4bccd4716c22a1f8767a11f`
- V1.3: `9f65035bc4bccd4716c22a1f8767a11f`

Upload-with-outro video-stream MD5:
- V1.2: `cab7b37955fd3fcead3a68b4d529099a`
- V1.3: `cab7b37955fd3fcead3a68b4d529099a`

This proves the final V1.2 picture bitstream was preserved exactly through the V1.3 remux.

## Visual/freeze QC inherited exactly from V1.2

V1.2 had already passed the full export Magic Gate after repairing earlier material freeze tells near ~20.7 s and ~51.0 s.

A stricter 0.30 s detector reported two borderline low-motion intervals near ~73.23 s and ~102.10 s; before/during/after frame inspection verified continuous intentional motion, not corruption.

Because V1.3 contains the identical picture stream, those findings remain authoritative:

- no black-frame events at the production threshold;
- no unresolved corrupt/frozen picture intervals;
- no sideways source footage;
- no blurred portrait sidebars;
- no duplicate-Brandi L18 V1 failure;
- no mirrored/symmetrical L18 V2 construction;
- no generated Brandi identity replacement;
- no white-goggle portal behavior;
- no broken final-review masks detected;
- final refrain returns progressively to reality;
- water/light ending remains intact.

V1.3 also passed a complete video decode after the audio remux.

## New authoritative audio verification

Source: `Irish eyes (Remastered) FINAL SOURCE.wav`

- source SHA-256: `b4255e04f31cf7c137ceea82222138c9e07ccc27de4aa8b83b8334814c4d5f46`
- duration: 187.120000 s
- PCM 16-bit stereo / 48 kHz
- integrated loudness: approximately -15.0 LUFS
- loudness range: 5.7 LU
- true peak: approximately -2.4 dBFS

The AAC-LC encode in V1.3 was produced once from this WAV at approximately 320 kb/s; it does not reuse the rough cut or the V1.2 compressed audio stream. Post-roll audio is silence after the song by design.

## Persistent files

Canonical artistic master:
- Library path: `/Video Creation/Irish Eyes/Final/IRISH_EYES_V1_3_FINAL_YouTube_720p30.mp4`
- Library ID: `libfile_188ada3ee1c88191ae217eeb834402cd`

Canonical upload with outro:
- Library path: `/Video Creation/Irish Eyes/Final/IRISH_EYES_V1_3_FINAL_UPLOAD_WITH_OUTRO_720p30.mp4`
- Library ID: `libfile_0c67dfde60ec8191a37a97e520139892`

Authoritative WAV:
- Library path: `/Video Creation/Irish Eyes/Final/Irish eyes (Remastered) FINAL SOURCE.wav`
- Library ID: `libfile_721852b16ee4819187b553f2e13f459a`

V1.2 QC evidence remains preserved in `/Video Creation/Irish Eyes/QC/` and is valid for V1.3 because the picture stream is identical.

## Verdict

**V1.3 passes final export QC and is the canonical completed Irish Eyes master.**
