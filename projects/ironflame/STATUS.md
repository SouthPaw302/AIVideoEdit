# IronFlame — Current Production Status

**Updated:** 2026-09-05 02:16 EDT  
**Branch:** `song/ironflame-20260905-0216`  
**State:** **Timestamped V2 reference-motion pass rendered, QC scanned, and durably stored for review**  
**Role:** Follow-up production pass based on three new user-supplied animated visual references

## Current timestamped pass

A new pass was created from the canonical `song/ironflame` branch without overwriting V1 history. The literal nested ref `song/ironflame/20260905-0216` cannot coexist with the existing Git ref `song/ironflame`, so the valid equivalent branch is `song/ironflame-20260905-0216`.

Render: `IRONFLAME_20260905_V2_REFERENCE_MOTION_720p24.mp4`

- duration: 244.680 s
- resolution/fps: 1280x720 @ 24 fps
- codecs: H.264 + AAC 48 kHz stereo
- bytes: 163,692,507
- SHA-256: `1444c80e9ef5a3bd11bce47f660938f0a5e0b6f59aec0607239db63baa5d8815`
- Library ID: `libfile_59bccc6ffb5c8191b2785e7f1b886d61`
- Library path: `/IRONFLAME_20260905_V2_REFERENCE_MOTION_720p24.mp4`
- exported-file QC: runtime/probe pass; no >=0.5 s black stretches detected; no >=3 s accidental freezes detected

See `runs/20260905-0216/RUN.md` and `runs/20260905-0216/QC.json` for source-reference hashes, mapping, render identity, and QC evidence.

This V2 pass is a review checkpoint, not yet declared the replacement canonical master. The new references define motion/composition language but do not contain the canonical female IronFlame identity; a later identity-forward pass should preserve the strongest motion language while restoring the recurring woman where the story requires her.

## Non-negotiable canon

- The IronFlame is a woman and the recurring mythic protagonist.
- Preserve the approved dark-folk/mythic-fantasy visual DNA and female character identity for identity-bearing scenes.
- Keep further IronFlame work on an IronFlame production branch, not directly on `main`.
- The film must remain directed and music-shaped, not a slideshow or generic visualizer.

## Canonical source package

- Lossless source: `Ironflame (Remastered).wav`
- Duration: 244.680 seconds
- Sample rate/channels: 48 kHz stereo
- SHA-256: `76679c5e0d0c905635e80904ff67ba03b52c11893d3a71f09433e17feff0f962`
- Recoverable lossless parts: `assets/audio/canonical-wav.parts/`
- Recoverable working reference parts: `assets/audio/working-reference.parts/`
- Reconstruction instructions: `AUDIO_RECOVERY.md`

## Historical V1 record

V1 was previously rendered and delivered as a twelve-scene 1280x720 master plus a 540p compact delivery, but its exact final MP4 archive identity remains unrecovered. Its source audio, stills, prompts, timing plan, and reconstruction data remain preserved on `song/ironflame`.

## Continuous checkpoint rule

After any new IronFlame work, update status, manifest/identity records, render history, QC, and affected assets before ending the work phase or switching chats.
