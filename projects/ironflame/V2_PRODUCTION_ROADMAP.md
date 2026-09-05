# IronFlame V2 — Production Roadmap

This production follows `main/general/reusable/generative-engine/PLAN.md` and the canonical song structure, with the user-supplied videos as the hard visual-style constraint.

## Phase A — reference decomposition — IN PROGRESS

- [x] Extract all 145 native frames from each of the three supplied 24 fps clips (435 frames total).
- [x] Extract 12 representative frames from each clip for contact sheets.
- [x] Select initial hero candidates around the strongest motif state in each clip.
- [x] Extract reference palettes from hero candidates.
- [x] Lock allowed and excluded effect grammar in `V2_REFERENCE_STYLE_LOCK.md`.
- [ ] Add source-video hashes and durable locations to manifest.

## Phase B — canonical song control bus — STARTED

- [x] Analyze `Ironflame (Remastered).wav` at 24 fps using the algorithm in `general/reusable/generative-engine/audio/reactive_core.py` from `main@e6ba077cabeed8e799090d3d505d82bc96d2fd02`.
- [x] Produce 5,873 frame-aligned control records (`rms`, `onset`, `low`, `mid`, `high`, raw + normalized).
- [x] Summarize controls against the canonical 12 IronFlame shot windows.
- [ ] Persist full control bus with the song package and checksum.
- [ ] Gate any reactive mapping against a short reference-matching proof before full render.

## Phase C — lyric/story hero map — NEXT

Build the full lyric structure using the existing 12 timing blocks, but replace the old literal dark-fantasy imagery with a coherent progression among three visual families:

1. **Cosmic contact** — REF-A: silhouette + giant flowing face + traveling orb.
2. **Intimate recognition** — REF-B: profile silhouette + warm translucent head in palm.
3. **Transformation / signal** — REF-C: crystalline head + ribbon field + ring/halo.

Each timing block receives:
- lyric/emotional function;
- one chosen hero image;
- generated support frames that look like adjacent frames from the same visual family;
- only reference-compatible motion/effect assignments;
- entry/exit transition chosen from reference behavior, not generic FX availability.

## Phase D — hero expansion media

For each selected hero:

- create 16:9 expansion media from the extracted source frame or a generated frame matched tightly to it;
- preserve silhouette/profile/crystalline geometry and source palette;
- create foreground/background/ribbon/orb/ring plates only where the source visual actually contains that element;
- create depth/masks only if they enable subtle reference-like motion;
- reject any expansion that becomes photoreal fantasy, environmental narrative scenery, or unrelated VFX.

## Phase E — proof-gated animation

Candidate repo systems:

- `FX2-AUDIO-001` reactive control bus;
- `FX2-MOTION-002` localized living flow;
- `FX2-MOTION-004` quiet depth breath, proof required;
- `FX2-LIGHT-001/002` restrained breathing/internal light movement;
- `FX2-LIGHT-003` tiny crystalline glints, proof required;
- `FX2-TRANS-003` light peak handoff, proof required;
- `FX2-VIS-001` organic reactive field only if shaped into the REF-C ribbon language;
- `FX2-SPATIAL-004` living parallax only when nearly invisible and supported by a suitable hero/depth map.

Do not use rain, fire, smoke, forge, generic camera shake, or unrelated transition families simply because they are available.

## Phase F — assembly and QC

- assemble only after enough finished shot packages exist;
- maintain native 24 fps timing;
- scan actual exported video for black/damaged frames, freezes, repeats, bad seams, missing effects, flicker, style drift, and full runtime/audio sync;
- create side-by-side reference contact sheets for style QC;
- update manifest/status/render history and durable file identities before handoff.
