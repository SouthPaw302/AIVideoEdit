# Irish Eyes — Actual Movie Asset Manifest

This file tracks **rendered movie assets**, not storyboard/concept material.

## Batch 01 — 2.5D real-source shots

All three shots are built from real extracted frames of `Brandi South Florida 2017.mp4` using the approved continuous-depth 2.5D renderer, soft subject protection, inpainted background disocclusion, restrained cinematic restoration, and highlight halation.

### shot_25d_001_arrival.mp4

- source key frame: `frame_00100.png`
- purpose: Act I arrival / intimate establishing portrait
- camera treatment: restrained push with depth-differential motion
- duration: 6 s
- frame rate: 30 fps
- dimensions: 720×1280 portrait
- bytes: 1,946,846
- SHA-256: `4a710d21fbc8ac8a7bf7eaefd9fa0fe1852e77b6ee4705eb41e01e5cfb34eaee`
- QC: approved for timeline use

### shot_25d_002_hair_water.mp4

- source key frame: `frame_00600.png`
- purpose: hair/wind + water memory passage; strong candidate for the `Spanish hair` motif
- camera treatment: lateral depth drift; stronger environmental separation
- duration: 6 s
- frame rate: 30 fps
- dimensions: 720×1280 portrait
- bytes: 1,494,957
- SHA-256: `eef5280b68494150a7acbb0ee1176fca5789cd0d0a89d48a6b7bcdee197d9f0d`
- QC: approved for timeline use

### shot_25d_003_horizon.mp4

- source key frame: `frame_00850.png`
- purpose: horizon / final-reflection / recurring memory anchor
- camera treatment: eased shallow orbit with depth-differential foreground/background movement
- duration: 6 s
- frame rate: 30 fps
- dimensions: 720×1280 portrait
- bytes: 1,467,208
- SHA-256: `3fb2744ceac299d277aaeb4c8bc57e4cb1caf45223a0e7c85634ca40d80763c7`
- QC: approved for timeline use

## Binary-storage note

The active runtime produced the MP4 binaries in the production workspace. The GitHub connector available in this session writes repository text/Git objects but does not directly accept a local binary path, so this manifest records exact filenames, sizes, source frames, roles, and cryptographic hashes for recovery. Do not claim these binaries are committed to Git unless a later binary-ingestion step actually writes them.

## Next rendered asset batch

- reflection-to-water dream transition;
- real-motion loop set with seam QC;
- source-footage cinematic restoration passages;
- 2.5D + independent water motion composite;
- Act I assembled sequence with the remastered song audio.