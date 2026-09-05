# IronFlame V3 — Story Proof 00:00–00:42

Branch: `song/ironflame-20260905-0216`
Date: 2026-09-05

## Purpose

First V3 proof built according to the repository Bible: AI hero imagery is the primary film material; the supplied source clips are visual/motion DNA rather than timeline filler. The sequence covers the opening lyric block through 00:42 and is intended as a story/motion/transition proof, not a final timeline section.

## Technical identity

- Output: `IRONFLAME_V3_SEQUENCE_00_42_1080p24.mp4`
- Duration: 42.000 s
- Raster: 1920x1080
- FPS: 24
- Video: H.264
- Audio: AAC from `Ironflame (Remastered).wav`
- Library: `/AIVideoEdit/IronFlame_V3_20260905/IRONFLAME_V3_SEQUENCE_00_42_1080p24.mp4`
- Library ID: `libfile_f063a3736dc88191bd3ef8f3ab456c0d`
- SHA-256: `2f66092919593ec162b44effb3e48cfc866d088ece40fc5421c97ebc51c89fc8`

## Shot packages

### Shot 01 — Encounter — 00:00–~17.6

Hero: `cosmic_connection_through_light.png`.

Living-scene behavior:
- native 16:9 1080p crop, no vertical/mirrored filler;
- slow authored camera push;
- warm/orb/eye light mask derived from the image;
- warm glow is modulated by the canonical 24 fps `rms_n` and `onset_n` controls;
- full-frame luminance breath follows `rms_n`;
- motion remains restrained so the silhouette/face composition stays stable.

### Transition 01 — Ribbon/light transport — ~17.6–18.4

Not a portal/gate. A wavy left-to-right transport mask carries the scene from the first hero to the second, with a narrow light ridge derived from the existing ribbon/light vocabulary. Transition is explicitly rendered as its own 1080p24 asset.

### Shot 02 — Recognition — ~18.4–42.0

Hero: `luminous_ai_spirit_in_her_hand.png`.

Living-scene behavior:
- native 16:9 1080p crop;
- slow controlled push/drift;
- warm-head/palm glow mask derived from the image;
- glow intensity follows song `onset_n`;
- overall luminance breath follows `rms_n`;
- the human silhouette remains compositionally protected.

## Music authority

The sequence consumes the preserved canonical generative-engine 24 fps control bus generated from the remastered WAV. The proof currently uses RMS and onset directly for visible light/motion response. Later V3 shot packages should also consume low/mid/high controls where their scene grammar calls for it.

## Export QC

The actual exported 42-second file was scanned with FFmpeg `blackdetect` and `freezedetect`.

Result:
- black-frame events: none detected;
- freeze events >= 1.5 s at current threshold: none detected;
- runtime: exactly 42.000 s;
- aspect/raster: 1920x1080;
- frame rate: 24 fps.

This is a technical/story proof only. It has not yet passed the repository FX V2 precompile gate as a production-approved effect manifest. Before a final production compile, exact reusable FX IDs used by V3 must be declared in the song `.fx.json`, resolved against the canonical registry, proof/QC records attached, `fx.lock.json` generated, and the lock re-verified immediately before render.

## Decision

KEEP AS V3 STORY/MOTION PROOF. Do not promote V2.2 alpha footage into V3. Continue building the film from AI hero shot packages with internal animation and authored transitions, then assemble only after enough approved shot packages exist.
