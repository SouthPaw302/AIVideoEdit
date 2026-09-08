# Narrative / Music / Media Evidence Contract

This contract closes a class of failures where a technically valid render can pass while the intended story media was never created.

## 1. Resolve lyrics status and directing use
Every production must explicitly record one of:
- `present`
- `instrumental`
- `none_confirmed`

If lyrics are present, preserve a verified `LYRICS.md`.

By default, present lyrics are active directing authority and must be used with musical analysis as script authority.

A current user may explicitly exclude otherwise-present lyrics from directing. In that case `MUSIC_ANALYSIS.json` must keep `lyrics.status = "present"` and record:
- `lyrics.directing_use = "excluded_by_current_user"`
- `lyrics.exclusion_source = "current_user_instruction"`
- the current user's exclusion instruction

When lyrics are explicitly excluded, they remain archived source material but must not appear in `SCRIPT.basis` or `lyric_cue` fields. Music analysis becomes the primary narrative/directing authority.

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

## 8. Reference-role separation
A visual reference must have an explicit production role. Examples include motion language, palette, lighting, composition, effect behavior, source footage, or source stills.

A reference authorized for **style or motion language only** teaches those properties only. It does **not** authorize reuse of its subject, scene, source frames, or footage as final-picture content.

Reusing reference content in the final picture requires an explicit current-user instruction authorizing that content role. Do not convert “make it move like this” into “make the movie out of this.”

Generated companion media must materially expand the production world rather than merely reproduce the reference subject with minor stylistic changes.

## 9. Creative rejection overrides prior acceptance
A technical or contract pass never outranks a current-user creative rejection.

If the current user rejects a proof, generated-media set, visual direction, or final export:
- mark the affected proof/assets/export as `rejected`;
- clear any dependent acceptance/final-QC booleans;
- roll the project back to the earliest production stage that must be rebuilt;
- do not promote rejected media or techniques as accepted canon.

A previously passing export may therefore become non-final without any change to its technical decode/QC metrics.
