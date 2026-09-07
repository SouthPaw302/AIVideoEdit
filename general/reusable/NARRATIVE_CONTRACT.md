# Narrative / Music / Media Evidence Contract

This contract closes a class of failures where a technically valid render can pass while the intended story media was never created.

## 1. Resolve lyrics status
Every production must explicitly record one of:
- `present`
- `instrumental`
- `none_confirmed`

If lyrics are present, preserve a verified `LYRICS.md` and use lyrics plus musical analysis as story/script authority.

If lyrics are absent, the music itself is the primary narrative source. Instrumental does **not** mean narrative-free.

## 2. Resolve genre authority
The agent may infer genre only when it is reasonably confident. `MUSIC_ANALYSIS.json` uses:
- `genre.status = "confident"` with confidence >= 0.65; or
- `genre.status = "user_confirmed"` when the user supplies the song type.

If the agent cannot identify the type confidently, it must ask the current user before visual/story lock. Do not silently choose a cultural/genre language.

## 3. Analyze musical directing cues
`MUSIC_ANALYSIS.json` must preserve:
- tempo/pulse or explicit non-metric status;
- meter/groove;
- section boundaries;
- energy changes;
- meaningful instrument/texture entrances and exits;
- drops/builds/tension/release/recurring motifs;
- per-section musical cues;
- per-section narrative function.

These are directing inputs. They control story progression, shot timing, animation intensity, transition timing, and FX escalation.

## 4. Script after storyboard
The storyboard establishes the route. The production script makes it executable.

Before shot packages:
- create `SCRIPT.md` for humans;
- create `SCRIPT.json` for machines;
- cover the entire target frame range without gaps;
- map each frame span to story action, visual media, animation behavior, musical cues, lyric cues when applicable, and transition.

The render/assembly process follows the script; it may not invent a substitute story at compile time.

## 5. Real media is mandatory
A declared capability is not an asset.

If the media plan selects generated stills/support imagery/living paintings, actual generated visual assets must appear in `ASSET_MANIFEST.json`.

Every shot package must include hashed `media_evidence` for actual source/generated/derived media. A folder containing only README/JSON metadata is not a shot package.

Procedural geometry, gradients, particles, or placeholder shapes can be support FX, but they cannot silently replace scripted characters, environments, actions, memories, locations, or other required story media.

## 6. Preview semantics
A user may ask to keep chat light, avoid intermediate downloads, or avoid reviewing every preview. That instruction does **not** mean “do not generate images.”

If the active generation runtime necessarily exposes generated-image previews in chat, those previews are allowed as part of creating the real production assets. Keep surrounding chatter minimal.

## 7. Final creative QC
Technical checks such as duration, decode success, freeze detection, and black-frame detection are necessary but insufficient.

Before `FINAL_QC_PASSED`, compare the full export to the locked `SCRIPT.json`. The project fails creative QC if major scripted story sections are absent, collapsed into a repeated motif, or replaced by placeholder geometry.
