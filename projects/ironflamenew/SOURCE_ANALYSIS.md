# IronFlameNew Source Analysis

## Master audio
`Ironflame Redux(1).wav`
- SHA-256: `76679c5e0d0c905635e80904ff67ba03b52c11893d3a71f09433e17feff0f962`
- Duration: 244.68 s
- PCM s16le, 48 kHz, stereo
- Estimated tempo: ~89.10 BPM half-time / ~178.21 BPM double-time
- Tonal estimate: F minor
- Canonical 24 fps reactive-control pass generated in sandbox using `general/reusable/generative-engine/audio/reactive_core.py` algorithm.
- Control frames: 5,873
- Control-bus SHA-256: `9caa2507b79b785dd8ad11cdf1dbd9cdd220521ce0d1e224e13082304627e0de`

## Reference A — `1 (1)(1).mp4`
- SHA-256: `717608f9a8e83819a921f7a1af276f89b0ed41ecd7fbe3dba89c4cbe1a2ecb03`
- 464x688, H.264, 24 fps, 6.0417 s
- Giant blue contour/cosmic face + human silhouette + traveling warm orb.
- Motion sample: mean frame delta 3.35; sampled optical-flow mean ~0.40 px, 95th ~1.42 px.

## Reference B — `1 (2)(1).mp4`
- SHA-256: `402adf8e580ba5105f7ebf17df28107ad4ab5e5323fb8d0a8adc42835013cde7`
- 464x688, H.264, 24 fps, 6.0417 s
- Human profile + warm translucent presence emerging from hand and making face contact.
- Motion sample: mean frame delta 1.63; sampled optical-flow mean ~0.06 px, 95th ~0.30 px. This is the quiet-motion reference.

## Reference C — `1 (3)(1).mp4`
- SHA-256: `da4e50dae75ca498692975e3ef80b498572f537c4a6bbd5de46cca030d65e464`
- 464x688, H.264, 24 fps, 6.0417 s
- Crystalline/faceted face + blue fluid ribbons + circular white energy trace.
- Motion sample: mean frame delta 7.74; sampled optical-flow mean ~2.71 px, 95th ~10.64 px. This is the high-energy reference.

## Interpretation
The references define three complementary energy states: **quiet contact (B), conscious encounter (A), and high-flow transformation (C)**. Production should modulate between them according to the song rather than use one motion intensity throughout.
