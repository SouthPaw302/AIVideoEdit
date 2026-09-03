# Silver Coin — Status

**Updated:** 2026-09-03 UTC  
**Branch:** `song/silver-coin`  
**Current state:** **V8 complete / final QC passed / YouTube delivery archived.** V8 fixes the rejected V7 approach by rebuilding the locked paintings into real frame-by-frame animated effect clips, then assembling those clips into six music-synced sections before final delivery.

## Canonical visual rule

The two user-supplied sample videos remain the visual source of truth:

- `imagine-d04b484c.mp4`
- `imagine-5558fc80.mp4`

The blonde flower-crowned woman from sample A remains the recurring protagonist. No replacement paintings were generated for V8.

## Locked hero paintings

V8 uses the eight accepted V6 paintings only:

- woodland / silver coin portrait
- woodland path / village reveal
- workers at sunset
- twilight inn exterior
- first-toast tavern scene
- clapping / rhythm tavern scene
- fiddler scene
- communal dance scene

All are backed up in ChatGPT Library and indexed in GitHub. See `BINARY_ARCHIVE.md`.

## V8 effect library

V8 contains real reusable effect clips rendered from those paintings:

1. forest / hair / flower-crown breathing
2. coin glint
3. tavern firelight + smoke
4. fiddler/bow impact motion
5. communal crowd sway
6. lightning + wet-road reflection
7. Gaussian light shafts
8. fog/pigment travel
9. explicit 2.5D depth-parallax scene graph
10. recursive coin portal
11. temporal dusk-to-night painting
12. real-audio waveform on the fiddler/bow (Chorus 1)
13. workers/procession motion
14. clap/hand/crowd rhythm response
15. shadow wipe
16. localized candle heat haze
17. real-audio waveform on the fiddler/bow (Chorus 2)
18. real-audio waveform on the fiddler/bow (Final Chorus)

Effect binaries are backed up under `/Video Creation/Silver Coin/Effect Assets/` and their recipes/hashes are checkpointed in GitHub.

## Six rebuilt V8 sections

- Section 1: `0.0–39.3` — depth parallax, Gaussian shafts, workers motion, shadow wipe, temporal night, music-aligned lightning
- Section 2: `39.3–82.7` — fire/smoke, heat haze, clap response, fiddler impact, real-audio bow waveform, crowd sway
- Section 3: `82.7–103.7` — coin glint, recursive coin portal, tavern fire/heat
- Section 4: `103.7–138.2` — Chorus 2 fire/clap/fiddle/dance plus the correct 127.4 s bow waveform
- Section 5: `138.2–188.0` — temporal night, reverse fog travel, forest breath/depth, coin return, forward fog travel, late bridge lightning aligned near 183.3/185.0/187.3 s
- Section 6: `188.0–207.44` — clap/fiddle/dance, correct 193.3 s final-chorus waveform, reverse coin portal to forest, coin-glint resolution

Each section was individually rendered, visually QC'd, hashed, and backed up before full assembly. See `V8_SECTION_INDEX.json`.

## Final master

`Silver_Coin_V8_FINAL_YouTube_720p24.mp4`

- final status: **QC PASSED**
- duration: **210.461333 s**
- song: **207.44 s** + ~3 s ending card
- video: **1280x720, 24 fps, H.264 High profile**
- audio: **AAC LC, 48 kHz stereo**
- bytes: **155,101,031**
- SHA-256: `b996cc251a73e93540abdcc7b8e1077959b5d82dcfb3396aa49c990302216d70`
- persistent Library ID: `libfile_acfb04300bd88191b67e23b2ad736870`

See `V8_FINAL_META.json`.

## Final QC

- full high-bitrate candidate decode: **PASS**, zero decode errors
- delivery beginning/middle/end sample decode: **PASS**
- unintended black-frame scan during song: **PASS**
- section timing drift vs music map: approximately **<= 8 ms**
- protagonist continuity: **PASS**
- visual effect presence: **PASS**
- motion scan confirms substantial frame-level movement instead of V7-style global treatment:
  - Verse 1: 88.34% of frames > 0.5 frame-delta
  - Chorus 1: 96.54%
  - Verse 2: 83.93%
  - Chorus 2: 94.57%
  - Bridge: 81.59%
  - Final chorus: 98.50%

See `V8_QC_REPORT.md`.

## Archive state

A complete Silver Coin runtime snapshot was checksummed before V8 production:

- 181 media files
- 150 images
- 30 videos
- 1 canonical WAV
- just over 1 GB total

Verified ZIP archive volumes and the full SHA-256 ledger are stored under `/Video Creation/Silver Coin/Archive Snapshots/`.

The final candidate, QC assets, all six sections, all effect packs, canonical source videos/audio, hero paintings, and final YouTube master are backed up in persistent Library storage.

## Historical versions

- V5.1 / V5.2: technically valid, rejected image direction
- V6: accepted picture direction and sync base
- V7: rejected for insufficient localized/frame-level effects
- **V8: current final delivery**

## Next action

Do not rerender by default. Treat V8 as the current final. Only modify specific sections/effects in response to user review, preserving the six-section recovery workflow and all existing archive checkpoints.
