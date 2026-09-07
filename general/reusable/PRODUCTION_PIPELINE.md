# Production Pipeline

This ordered method applies to every `song/<slug>` branch and is enforced by `PRODUCTION_CONTRACT.json`, `production_guard.py`, and `narrative_guard.py`.

## 0 — Initialize authority/state
Create the branch-local template files. `SOURCE_AUTHORITY.json` allows current user inputs, current branch decisions, and current `main`; historical chats/unrelated branches are denied unless explicitly authorized.

## 1 — Ingest source material
Record hashes, roles, technical metadata, and recovery/storage pointers for supplied audio/video/images.

## 2 — Extract and analyze visual references
**Video present:**
- Short video (system default: <=30 s AND <=1800 frames): extract every frame.
- Larger video: meaningful sampling is allowed. Record sampling method, extracted count, frame/time ranges and scene/motion coverage.
- Analyze style, palette, motion language, composition, identity-bearing features, and useful frame/range mappings.

**Images present:** inspect/analyze all supplied images before deriving new media.

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

**Lyrics present:** preserve verified lyrics in `LYRICS.md`; lyrics + music analysis drive story/script.

**No lyrics:** music analysis becomes the primary story map. Instrumental music still requires narrative construction.

**Genre unclear:** do not guess. Ask the current user. Record their exact declaration in `MUSIC_ANALYSIS.json` with `genre.status=user_confirmed`, `genre.source=current_user_instruction`.

## 2B — No visual references: Visual Direction Selection Gate
- Do not silently choose the visual style and do not generate production media yet.
- Build at least three **materially distinct numbered artistic-rendering routes** from the current song, verified lyrics when present, music analysis, genre authority, and `MEDIA_CAPABILITY_MATRIX`.
- Present the routes in chat. Each route must include: a route name, story interpretation, rendering/media treatment, and a numbered mini-storyboard with at least three beats/frames.
- The user may select one option number, combine option numbers, or modify a route.
- Record every presented option and the explicit current-user selection in `MEDIA_PLAN.json`.
- Lock the selection before production media begins.
- Concept/storyboard previews made only to help the user choose are decision artifacts and are allowed before the gate locks; they are not automatically production assets.

## 3 — Establish visual/media approach
Create/lock the production's visual DNA and `MEDIA_PLAN.json`. Choose deliberately among source footage, extracted frames, generated stills/support imagery, living paintings, layered composites, depth/2.5D, reactive/atmospheric plates, loops, transitions, real radiance fields, real 3DGS when valid, and conventional video.

For a no-reference production, `APPROACH_ESTABLISHED` is valid only after the Visual Direction Selection Gate is locked.

## 4 — Lock storyboard and shot map
Only after visual-reference analysis, music analysis, lyrics status, genre authority, and approach are complete. Map narrative and musical beats to specific source frame/ranges or to the established original-media plan.

## 4A — Lock the frame-followable video script
Create both:
- `SCRIPT.md` — readable director/editor script.
- `SCRIPT.json` — machine-readable full timeline.

`SCRIPT.json` must cover frame 0 through `total_frames - 1` without gaps and map each span to:
- shot ID;
- story action;
- visual media that must actually exist;
- animation behavior;
- music cues;
- lyric cue when applicable;
- transition.

If lyrics exist, the script basis includes lyrics + music analysis + storyboard. If no lyrics exist, the script basis includes music analysis + storyboard. Shot packages may not begin until the script is locked.

## 5 — Build real shot packages
For each selected shot use:
`source/ alpha/ layers/ depth/ generated/ fx_assets/ transition/ loop/ preview/ notes/`.

Each package also needs `package.json` with non-empty hashed `media_evidence` pointing to actual ingested/generated/derived visual media. A README + JSON-only package is invalid.

If `MEDIA_PLAN.json` selects generated stills/support imagery/living paintings, `ASSET_MANIFEST.json` must contain actual generated visual asset evidence. Do not substitute procedural rectangles/geometry for missing story media.

A user's request to keep chat light or avoid previews is **not** permission to skip generation. If the runtime surfaces generated-image previews as part of producing assets, allow them and keep surrounding chatter minimal.

## 6 — Animate/composite and prove
Reuse neutral canonical capabilities before inventing substitutes. Make short finished shot proofs. Inspect them visually. Protect identity. Internal motion first, camera second. Reference-video animation language, when supplied, is authoritative within the selected visual direction.

## 7 — Music-directed behavior
Use the `MUSIC_ANALYSIS.json` section map and preferably one preserved, smoothed, frame-aligned song analysis bus (RMS/onset/low/mid/high) when several systems need the same signals. Musical cues are directing inputs, not optional decoration.

## 8 — Lock FX
Only accepted shot recipes enter the production FX manifest. Resolve callable effects from `fx_v2/registry.json`, declare real pixel-altering render inputs, run the fail-closed precompile gate, generate and verify `fx.lock.json` immediately before compile.

## 9 — Assemble
Only after enough finished shot packages/proofs exist and the scripted visual media is present. Never use infrastructure success as a substitute for creative completion.

## 10 — Render and QC
Inspect the actual full export for black/damaged frames, freezes, repetition, loop seams, ghosting, invisible/missing effects, flicker/boiling, identity drift, source leakage, continuity, framing/aspect, runtime, compression and audio sync.

Also compare the complete export against `SCRIPT.json`: every scripted story section must materially appear. A technically clean export fails if the narrative media is absent or replaced by placeholders.

## 11 — Archive/promote
Preserve manifests, hashes, prompts/decisions, music analysis, script, proof/QC records and storage pointers. Promote genuinely reusable methods to project-neutral `main/general/reusable/` only after proof/QC.
