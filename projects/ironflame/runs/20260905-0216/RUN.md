# IronFlame — 2026-09-05 02:16 EDT production pass

Branch: `song/ironflame-20260905-0216`  
Base: `song/ironflame`

## Intent

Create a new IronFlame film pass from the canonical remastered WAV and the three user-supplied animated visual references, while preserving the canonical IronFlame lyric/story map and the repository rule that the result must be a directed music film rather than a generic visualizer or simple clip playlist.

## Source audio

`Ironflame (Remastered).wav`

- duration: 244.680 s
- 48 kHz stereo PCM
- SHA-256: `76679c5e0d0c905635e80904ff67ba03b52c11893d3a71f09433e17feff0f962`

## New user motion references

1. `imagine-22d97f7e.mp4`
   - 464x688, 24 fps, 6.041667 s
   - silhouette reaching toward a vast cosmic face with moving luminous points
   - SHA-256 `717608f9a8e83819a921f7a1af276f89b0ed41ecd7fbe3dba89c4cbe1a2ecb03`
2. `imagine-3324e842.mp4`
   - 464x688, 24 fps, 6.041667 s
   - silhouette interacting with a glowing vapor-like face / hand-held light
   - SHA-256 `402adf8e580ba5105f7ebf17df28107ad4ab5e5323fb8d0a8adc42835013cde7`
3. `imagine-ae835deb.mp4`
   - 464x688, 24 fps, 6.041667 s
   - faceted dark head with flowing translucent energy ring / wave
   - SHA-256 `da4e50dae75ca498692975e3ef80b498572f537c4a6bbd5de46cca030d65e464`

These references are motion/style DNA, not literal story canon and not identity anchors for the IronFlame woman.

## Film mapping

The existing canonical 12-scene timing map was retained because it is already derived from the exact 244.680 s WAV. The new references were mapped symbolically:

- faceted head + energy: memory/iron, sleeping distance, gravity inversion, ascendant/reactive passages
- cosmic reaching silhouette: inward windows, speaking walls, endless hallway, reaching the stranger, legacy mark
- glowing vapor face: dust/forge memory, unmade day, underground recognition, morning entering

Each 6 s reference was converted to a forward/reverse ping-pong motion ingredient before use to avoid hard loop resets. Each scene receives separate grade, movement, framing, mirroring/rotation where applicable, blurred spatial extension to 16:9, and scene-specific motion density.

## Render

`IRONFLAME_20260905_V2_REFERENCE_MOTION_720p24.mp4`

- 1280x720
- 24 fps
- H.264 video + AAC 256 kb/s audio
- exact duration: 244.680 s
- size: 163,692,507 bytes
- SHA-256: `1444c80e9ef5a3bd11bce47f660938f0a5e0b6f59aec0607239db63baa5d8815`
- persistent ChatGPT Library ID: `libfile_59bccc6ffb5c8191b2785e7f1b886d61`
- Library path: `/IRONFLAME_20260905_V2_REFERENCE_MOTION_720p24.mp4`

## QC performed on exported file

- probed final mux: H.264 1280x720 @ 24 fps; AAC 48 kHz stereo
- runtime verified: 244.680 s
- SHA-256 recorded after final mux
- `blackdetect` scan (0.5 s threshold): no detected black stretches
- `freezedetect` scan (3 s threshold): no detected accidental freezes
- audio is the exact supplied remastered WAV source, encoded only at final delivery mux

## Status

This is a completed reference-motion V2 pass and a durable checkpoint, not yet declared the replacement canonical IronFlame master. The visual references are abstract/portrait-oriented and do not themselves contain the canonical female IronFlame identity, so any later hero-character rebuild should preserve this pass's motion language while restoring the canonical recurring woman in identity-bearing scenes.
