# Production Pipeline

This ordered method applies to every `song/<slug>` branch and is enforced by `PRODUCTION_CONTRACT.json`, `production_guard.py`, and `narrative_guard.py`.

## 0 — Initialize authority/state
Create the branch-local template files. New productions use Director Brain v2: set `director_brain_version=2` in `PROJECT_STATE.json` and create `OPERATING_ORDER.json` from the template. `SOURCE_AUTHORITY.json` allows current user inputs, current branch decisions, and current `main`; historical chats/unrelated branches are denied unless explicitly authorized.

Bootstrap current Main before production work. Read the Prime Directive and generated Second Brain before acting.

## 1 — Ingest source material
Record hashes, roles, technical metadata, and recovery/storage pointers for supplied audio/video/images.

## 2 — Extract and analyze visual references
**Video present:**
- Short video (system default: <=30 s AND <=1800 frames): extract every frame.
- Larger video: meaningful sampling is allowed. Record sampling method, extracted count, frame/time ranges and scene/motion coverage.
- Analyze style, palette, motion language, composition, identity-bearing features, camera behavior, internal motion, loop behavior, pacing, and useful frame/range mappings.

**Images present:** inspect/analyze all supplied images before deriving new media.

A reference teaches directing language unless current user authority explicitly allows content reuse. A reference video does not automatically imply cinematic production.

## 2A — Analyze music and resolve narrative authority
Create `MUSIC_ANALYSIS.json` before `REFERENCES_ANALYZED`.

Required decisions/evidence:
- lyrics status: `present`, `instrumental`, or `none_confirmed`;
- genre/song type;
- tempo/pulse or explicit non-metric status;
- groove/meter;
- section map;
- energy curve;
- instrument/texture entrances and exits;
- drops/builds/tension/release/recurring motifs;
- per-section musical cues and narrative function.

**Lyrics present:** preserve verified lyrics in `LYRICS.md`; lyrics + music analysis drive the directing interpretation unless the current user excludes lyrics.

**No lyrics:** music analysis becomes the primary directing map unless the current user supplies a stronger current direction. Instrumental music still requires deliberate visual direction, but not necessarily a cinematic narrative.

**Genre unclear:** do not guess. Ask the current user. Record their exact declaration in `MUSIC_ANALYSIS.json` with `genre.status=user_confirmed`, `genre.source=current_user_instruction`.

## 2B — No visual references: Visual Direction Selection Gate
- Do not silently choose the visual style and do not generate production media yet.
- Build at least three **materially distinct numbered artistic-rendering routes** from the current song, verified lyrics when present, music analysis, genre authority, and `MEDIA_CAPABILITY_MATRIX`.
- Where appropriate, the routes should explore different production forms rather than three cosmetic variants of one form.
- Present the routes in chat. Each route must include: route name, interpretation, rendering/media treatment, proposed `production_mode`, and a numbered mini-storyboard with at least three beats/frames.
- The user may select one option number, combine option numbers, or modify a route.
- Record every presented option and the explicit current-user selection in `MEDIA_PLAN.json`.
- Lock the selection before production media begins.
- Concept/storyboard previews made only to help the user choose are decision artifacts and are allowed before the gate locks; they are not automatically production assets.

## 2C — Lock the Director decision
Direction authority and production mode are separate decisions.

Direction authority:
- `reference_led`
- `music_led`
- `user_directed`

Production mode:
- `living_scene`
- `cinematic`
- `hybrid`

For Director Brain v2, record both in `OPERATING_ORDER.json` before `APPROACH_ESTABLISHED`. Also record the one-sentence mission, current-user direction, and exact next action.

## 3 — Establish visual/media approach
Create/lock the production's visual DNA and `MEDIA_PLAN.json`. Choose deliberately among source footage, extracted frames, generated stills/support imagery, living paintings, layered composites, depth/2.5D, reactive/atmospheric plates, loops, transitions, real radiance fields, real 3DGS when valid, and conventional video.

For a no-reference production, `APPROACH_ESTABLISHED` is valid only after the Visual Direction Selection Gate is locked. For Director Brain v2, it also requires a valid Operating Order.

## 4 — Lock storyboard and shot map
Only after visual-reference analysis, music analysis, lyrics status, genre authority, and director decision are complete. Map narrative and musical beats to specific source frame/ranges or to the established original-media plan.

When the user approves hero imagery, identities, picture language, shot architecture, or other foundational material, record that approval in `canon_lock` rather than treating approved material as disposable generation input.

## 4A — Lock the frame-followable video script
Create both:
- `SCRIPT.md` — readable director/editor script.
- `SCRIPT.json` — machine-readable full timeline.

`SCRIPT.json` must cover frame 0 through `total_frames - 1` without gaps and map each span to:
- shot ID;
- story/action function;
- visual media that must actually exist;
- animation behavior;
- music cues;
- lyric cue when applicable;
- transition.

For `living_scene`, entries also declare semantic `motion_regions` and `protected_regions`. For `hybrid`, each entry declares whether the shot uses `living_scene` or `cinematic` behavior; living-scene entries carry the same semantic region requirements.

If lyrics exist, the script basis includes lyrics + music analysis + storyboard unless lyrics were explicitly excluded. If no lyrics exist, the script basis includes music analysis + storyboard. Shot packages may not begin until the script is locked.

## 5 — Build real shot packages
For each selected shot use:
`source/ alpha/ layers/ depth/ generated/ fx_assets/ transition/ loop/ preview/ notes/`.

Each package also needs `package.json` with non-empty hashed `media_evidence` pointing to actual ingested/generated/derived visual media. A README + JSON-only package is invalid.

If `MEDIA_PLAN.json` selects generated stills/support imagery/living paintings, `ASSET_MANIFEST.json` must contain actual generated visual asset evidence. Do not substitute procedural rectangles/geometry for missing story media.

Director Brain v2 visual assets should carry lifecycle state: `exploratory`, `candidate`, `approved`, `canonical`, `derived`, `rejected`, or `retired`. Locked canonical assets are not casually regenerated.

A user's request to keep chat light or avoid previews is **not** permission to skip generation. If the runtime surfaces generated-image previews as part of producing assets, allow them and keep surrounding chatter minimal.

## 6 — Animate/composite and prove
Reuse neutral canonical capabilities before inventing substitutes. Make short finished shot proofs and inspect them visually.

Apply proof criteria by declared production mode:
- `living_scene`: internal motion visible; materials move independently; identity stable; camera restrained; loop/join clean.
- `cinematic`: action readable; coverage sufficient; continuity controlled; progression present; pacing follows the music.
- `hybrid`: run the correct proof checks for each section and verify one coherent world.

When direction authority is `reference_led`, also compare the proof's actual behavior against the authorized reference language.

## 7 — Music-directed behavior
Use the `MUSIC_ANALYSIS.json` section map and preferably one preserved, smoothed, frame-aligned song analysis bus (RMS/onset/low/mid/high) when several systems need the same signals. Musical cues are directing inputs, not optional decoration.

## 8 — Lock FX
Only accepted shot recipes enter the production FX manifest. Resolve callable effects from `fx_v2/registry.json`, declare real pixel-altering render inputs, run the fail-closed precompile gate, generate and verify `fx.lock.json` immediately before compile.

## 9 — Assemble
Only after enough finished shot packages/proofs exist and the scripted visual media is present. Never use infrastructure success as a substitute for creative completion.

## 10 — Render and QC
Inspect the actual full export for black/damaged frames, freezes, repetition, loop seams, ghosting, invisible/missing effects, flicker/boiling, identity drift, source leakage, continuity, framing/aspect, runtime, compression and audio sync.

Also compare the complete export against `SCRIPT.json`: every scripted section must materially appear. A technically clean export fails if the intended visual behavior is absent or replaced by placeholders.

Apply `MODE_AWARE_QC.md`. Director Brain v2 requires mode-aware proof acceptance and final QC state, not only technical pass flags.

## 10A — Accept, lock, and refine
When the current user explicitly accepts a full picture baseline:
- set `accepted_baseline.status=accepted`;
- record file/locator, SHA-256, and the user's acceptance statement;
- lock the approved picture language/canon;
- preserve the accepted master as recoverable production truth.

If the user then asks for changes, create an active `refinement_scope`:
- goal;
- allowed changes;
- forbidden changes;
- `restart_authorized`.

Default behavior is local repair and convergence, not restart:
`ACCEPT -> LOCK -> NAME DEFECTS -> REPAIR ONLY THOSE DEFECTS -> COMPARE -> PROMOTE IF BETTER`.

When `restart_authorized=false`, do not regenerate/reinterpret the accepted foundation.

## 10B — Delivery mastering
Preserve the artistic master separately from a platform/delivery master when intros, outros, titles, packaging, or platform-specific technical requirements differ. Platform packaging must not overwrite the accepted artistic master.

## 11 — Archive/promote
Preserve manifests, hashes, prompts/decisions, music analysis, script, Operating Order, proof/QC records, accepted-baseline identity, and storage pointers. Promote genuinely reusable methods to project-neutral `main/general/reusable/` only after proof/QC.

If intermediate media is lost but an accepted master exists, analyze the master as a recovery source before considering a restart.
