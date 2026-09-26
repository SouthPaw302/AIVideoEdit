# Status

Stage: **SOURCE_INGESTED**

Repository / Actions status: **HEALTHY**.
Production branch: `song/mountain-noir-after-midnight`.
`main` has not been modified.

Verified GitHub Actions:
- Production Contract run `36223990802` — **PASS**
- Head: `1b03cfa05661dba4980b1452f27adb44a1488af9`

Canonical private Drive music masters:
- Irish eyes (Remastered).wav — 187.120 s
- Leave It by the Door.wav — 198.840 s
- Silver Coin (Remastered).wav — 207.440 s
- El Viento trae tu nombre Instrumental.wav — 158.640 s

Total source music: **752.040 s / 12:32.040**
Target: **900.000 s / 15:00.000**
Authored extension required: **147.960 s / 2:27.960**

Completed in this pass:
- Current-main bootstrap, production, recut and standard-workflow guards — **PASS**.
- All four Drive WAV masters analyzed with canonical `AUDIO_MAP`, `EDIT_MAP` and 20 Hz `REACTIVE_CONTROLS` evidence.
- All three authorized Drive visual references meaningfully sampled; 310 visual candidates reduced to 36 candidate frames with 204 measured near-duplicate rejections.
- Drive chapter timing copied to `CHAPTERS.txt`; source hashes and ffprobe identities preserved.

Current truth:
- Signal analysis is complete, but lyrics status remains unresolved per track; do not advance to `REFERENCES_ANALYZED` yet.
- Candidate visual manifests exist, but no still / HERO_LIBRARY is locked or canonical.
- No shot packages or canonical proof render exist.
- The sandbox 15-minute FFmpeg recut is rejected/non-canonical because it reused finished videos as the primary picture.

Exact next action:
Resolve lyric authority per track, then semantically review the measured candidate frames and lock only the strongest source-derived stills before storyboard or proof rendering.
