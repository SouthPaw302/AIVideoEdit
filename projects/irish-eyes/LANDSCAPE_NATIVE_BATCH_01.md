# Irish Eyes — Landscape Native Batch 01

Branch: `song/irish-eyes`

Purpose: rebuild important real-Brandi shots directly from the 953 extracted source frames at final working aspect ratio instead of relying on portrait proof enlargements.

## Rendered masters

### L15 Arrival Real

`landscape_16x9/masters/IE_L15_ARRIVAL_REAL_16x9_V1.mp4`

- 1280x720 / 30 fps
- 5.033333 s / 151 frames
- 0 black frames / 0 freeze candidates
- mean frame delta `2.1286863088348764`
- SHA-256 `38a2213e3bdc9521f4b072a5f0dd922470a76772008ee3016836efe2764c12d4`
- decision: KEEP

### L16 Irish Eyes Portrait

`landscape_16x9/masters/IE_L16_IRISH_EYES_PORTRAIT_16x9_V1.mp4`

- 1280x720 / 30 fps
- 3.366667 s / 101 frames
- 0 black frames / 0 freeze candidates
- mean frame delta `1.6496843749999999`
- SHA-256 `41e4e7157a62189731a2f8f14e461ad04e70f45e4de706bef58846bbada35745`
- decision: KEEP

### L17 Hair Real Motion

`landscape_16x9/masters/IE_L17_HAIR_REAL_MOTION_16x9_V1.mp4`

- 1280x720 / 30 fps
- 2.866667 s / 86 frames
- 0 black frames / 0 freeze candidates
- mean frame delta `8.668883837997003`
- SHA-256 `1614cf2934039f80505e46db12b77f500feb970f8c64f1b7dfef3627e1f800d3`
- decision: KEEP

### L18 Full-Body Waterfront 2.5D

V1 was rendered and rejected during QC because the background plate still contained a giant partial Brandi at frame left, producing an obvious duplicate-person artifact.

V2:
`landscape_16x9/masters/IE_L18_FULL_BODY_WATERFRONT_25D_16x9_V2.mp4`

- 1280x720 / 30 fps
- real frame-420 Brandi alpha subject
- background rebuilt only from the clean right-side real frame-520 waterfront, mirrored/extended into 16:9
- only one Brandi is present
- independent subject/background motion + restrained moving water
- SHA-256 `08ef5521787fa935ab3aca157a1c5ce8b5b4ec665782777d5cdaf3a33cf231e1`
- decision: QC HOLD until the V2 full visual scan completes; never use V1

### L19 Last Look Real

`landscape_16x9/masters/IE_L19_LAST_LOOK_REAL_16x9_V1.mp4`

- 1280x720 / 30 fps
- 4.466667 s / 134 frames
- 0 black frames / 0 freeze candidates
- mean frame delta `3.453348018483709`
- SHA-256 `95d7b61aef858553f5e269cebde08619c68dbce037db62e9b96937df46d0d763`
- decision: KEEP; final face/shadow matching remains part of editorial finishing

## QC

Batch contact sheet:
`landscape_16x9/qc/LANDSCAPE_MASTERS_L15_L19_QC.jpg`

The sheet caught the L18 V1 duplicate-person failure before rough assembly. This is exactly why landscape rebuilds must still pass QC even when the underlying source/effect family was already approved in portrait proof mode.

## Next

1. complete L18 V2 visual scan;
2. rebuild landscape-native L20–L23 environmental masters;
3. begin the 187.12-second 16:9 visual rough from `ROUGH_CUT_16X9_PLAN_V1.md`;
4. restore the Irish Eyes remastered WAV before calling the rough song-synced.