# Silver Coin V8 — Final Assembly QC

**Branch:** `song/silver-coin`  
**Date:** 2026-09-03

## Candidate

`Silver_Coin_V8_Candidate_720p24.mp4`

- 1280x720
- 24 fps
- H.264 Constrained Baseline
- AAC LC, 48 kHz stereo
- duration: 210.461333 s
- canonical song portion: 207.44 s
- ending: existing `SILVER COIN / FIN` card for ~3 s
- SHA-256: `cb257753fe352b248d9d6b249e2a2b24ef4f34fa79d6d184e06a2fd27f9af70a`
- Library ID: `libfile_820895c6d558819181a15ac72c3a8262`

## Integrity checks

- Full FFmpeg decode: **PASS**, zero decode errors.
- Unintended black-frame scan during 0-207.44 s song portion: **PASS**, no black intervals detected.
- Visual section-boundary timing vs intended music map: within approximately 8 ms through the working section boundaries; no meaningful sync drift.
- Canonical audio is muxed once across the assembled film instead of concatenating six AAC section tracks.

## Motion proof

V8 was specifically rebuilt because V7 did not contain enough visible frame-level motion. A downscaled frame-to-frame motion scan across the song portion produced:

| Section | Mean frame delta | Frames > 0.5 delta | Frames > 1.0 delta |
|---|---:|---:|---:|
| Verse 1 | 2.459 | 88.34% | 67.34% |
| Chorus 1 | 4.095 | 96.54% | 85.49% |
| Verse 2 | 2.210 | 83.93% | 63.69% |
| Chorus 2 | 4.154 | 94.57% | 82.00% |
| Bridge | 1.963 | 81.59% | 62.09% |
| Final chorus | 6.430 | 98.50% | 93.79% |

This confirms that V8 is not a static-frame/global-grade pass: motion is present across the majority of frames and intentionally increases in the choruses/final drive.

Full motion JSON is stored in Library as `libfile_bc3820dccf7c8191bfe1cdda6c10f776`.

## Effects visibly represented in the assembled film

- localized forest foliage/hair/flower-crown breathing
- 2.5D depth-parallax scene graph
- Gaussian light shafts and atmospheric diffusion
- workers/procession motion
- shadow wipe
- temporal dusk-to-night painting
- lightning + wet-road reflection flashes aligned to real song transients
- tavern firelight/smoke
- localized candle heat haze
- clap/hand/crowd rhythm response
- fiddler impact motion
- audio waveform integrated along the violin bow using the correct song passages
- independent communal crowd sway
- recurring coin glint
- recursive coin portal used forward and reverse
- fog/pigment travel used forward and reverse
- music-reactive camera impacts with larger amplitude in choruses
- opening title overlay and ending card from existing project assets

## Visual review

Final QC contact sheet stored in Library: `libfile_62f4094f0df88191b7fd78745d926a07`.

The review confirmed:

- protagonist identity remains stable;
- no replacement paintings were introduced;
- transitions do not create black gaps;
- the real-audio bow waveform appears in Chorus 1, Chorus 2, and Final Chorus at the intended musical passages;
- late bridge lightning visibly affects sky and wet-road illumination;
- final reverse coin portal resolves back to the woodland protagonist before the end card.

## Delivery rule

The 281.9 MB candidate is a high-bitrate assembly/QC artifact. Create a separate YouTube delivery encode only after this QC report is committed. Preserve the candidate in Library and never overwrite it.
