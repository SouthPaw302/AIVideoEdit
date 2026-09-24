# Silver Coin Test 2 — Revision 5 QC

## Deliverable

- File: `outputs/silver-coin-test-2/Silver_Coin_Test2_v5_New_Stills_Mountain_Noir_1280x720_24fps.mp4`
- SHA-256: `9aadaeea0cc6cf87f036c23599c3b773cdee9df9038cfa4650c2cf3aa44ffcf4`
- Video: H.264, 1280×720, 24 fps, 4,978 frames
- Audio: AAC, stereo, 48 kHz, sourced from `Silver Coin (Remastered).wav`
- Duration: 207.416667 seconds

## Checks

- Full video/audio decode: PASS
- Missing media in 30-scene manifest: NONE
- Black-frame and frozen-frame scan: no reportable events
- Intro export-frame review: PASS — Mountain Noir, song title, and channel tagline are legible
- SC15 coin-hand export-frame review: PASS — hand and coin orientation read naturally
- SC19 architecture/fire export-frame review: PASS — heroine remains visually stable
- SC27 rafter/fire escalation export-frame review: PASS
- Outro export-frame review: PASS — Mountain Noir closing reads over the dawn departure scene

## Known timing note

The canonical scene-duration sum rounds to 4,979 frames while the source picture encoder emits 4,978 frames. The FX driver now clamps to the actual encoded frame count. The difference is one frame (about 0.023 seconds) and does not truncate a lyric or audible phrase.
