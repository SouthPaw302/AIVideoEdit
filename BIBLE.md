# AIVideoEdit — Bible

Permanent operating system for authored music visuals.

`PRIME_DIRECTIVE.md` is the short directing law. This Bible expands the production doctrine without overriding it.

## Branch and authority law
`main` is system-only. Every production lives on `song/<slug>`. A new audio master starts a fresh song branch from current `main` unless the user explicitly names an existing branch. Production authority is current user instruction -> active song-branch state/Operating Order -> current main. Historical projects/chats are opt-in only.

## Target
Make the visual form that best serves the song. Do not default every project to the same kind of film.

A production may be:
- `living_scene` — strong stable compositions animated internally like living paintings;
- `cinematic` — evolving conventional film coverage, action, locations, and progression;
- `hybrid` — a deliberate combination of both.

Direction authority is separate: `reference_led`, `music_led`, or `user_directed`.

The result must be authored and intentional, not a slideshow, generic visualizer, geometric placeholder reel, or one weak repeated clip.

## Hard production order
Initialize -> ingest sources -> extract/analyze visual references -> analyze music -> resolve lyrics status -> resolve genre authority -> choose direction authority + production mode -> establish visual/media approach -> lock storyboard/shot map -> lock frame-followable script -> build real shot media/packages -> animate/composite -> accept short mode-aware proofs -> lock FX -> assemble -> render -> inspect actual export with mode-aware QC -> accept/lock/refine when applicable -> archive.

`general/reusable/tools/production_guard.py` and `general/reusable/tools/narrative_guard.py` are fail-closed authorities.

## Director Brain law
New projects use Director Brain v2 and `OPERATING_ORDER.json`.

The Operating Order records:
- one-sentence mission;
- direction authority;
- production mode;
- canon lock;
- accepted baseline;
- current refinement scope;
- current user direction;
- exact next action.

Approval creates canon. If the user accepts a baseline and then names defects, preserve the accepted foundation and repair only the authorized scope unless the user explicitly authorizes restart/reinterpretation.

## Music, lyrics and genre law
- Lyrics status must be explicitly resolved.
- If verified lyrics exist, lyrics + musical analysis are directing inputs unless the current user explicitly excludes lyrics.
- If there are no lyrics, the music itself becomes primary directing authority unless the current user supplies a stronger current direction: tempo/pulse, groove, phrasing, section changes, energy curve, instrument entrances/exits, drops/builds, tension/release and recurring motifs shape visual timing and development.
- If the agent cannot confidently identify the song type/genre, it must ask the current user before direction lock. The user's genre declaration becomes source authority.
- Absence of lyrics never permits an unconsidered default. It does **not** require a cinematic narrative; the production mode is chosen deliberately.

## Reference law
- Short reference video: extract every frame.
- Long/large reference video: meaningful sampling is allowed, but policy, sample count, frame ranges/scene coverage, and analysis must be recorded.
- Supplied images: inspect/analyze them before deriving new media.
- Analyze references for composition, motion language, camera behavior, internal motion, lighting, pacing, scene-change frequency, and loop behavior.
- A reference video does not automatically mean cinematic production. It may teach living-scene, cinematic, hybrid, or other visual behavior.
- Reference content is not final-picture material unless the current user explicitly authorizes content reuse.
- No visual references: enter the Visual Direction Selection Gate. Before production media, present at least three materially distinct numbered artistic-rendering routes. Each route includes a named interpretation, rendering/media treatment, proposed production mode, and numbered mini-storyboard. The user selects, combines, or modifies; record and lock the decision before production proceeds.

## Script law
After storyboard lock and before shot-package construction, create `SCRIPT.md` plus machine-readable `SCRIPT.json`. The script covers the complete target frame range and maps each frame span to function/action, visual media, animation behavior, music cues, lyrics when applicable, and transition.

For Director Brain v2 `living_scene`, script entries also name semantic `motion_regions` and `protected_regions`. For `hybrid`, each shot declares whether it uses living-scene or cinematic behavior.

## Living-scene law
A strong still is a scene plate, not a finished shot. Preserve the authored composition while selected elements live independently. Internal scene motion comes before camera motion. Fire, smoke, rain, water, reflections, light, atmosphere, hair, cloth, particles, and articulated subject motion should behave according to their material/semantic role. Protect faces, hands, anatomy, and canonical artwork. Do not substitute global shake, endless zoom, generic wobble, or low-frame-rate duplication for animation.

## Cinematic law
Cinematic work requires deliberate coverage, readable action, continuity, shot progression, and pacing that follows the song. Beautiful unrelated shots are not a finished film.

## Hybrid law
Hybrid work uses living-scene and cinematic methods deliberately by section/shot. Each section must pass the appropriate mode-specific proof rules while remaining inside one coherent visual world.

## Shot-package law
Every selected scene becomes a genuine branch-local shot package with source, masks/alpha, layers, depth where needed, generated support, FX assets, transitions/loops, proof preview, notes, QC, and actual hashed media evidence. Metadata-only packages are forbidden. Preview means a short finished proof, not premature assembly.

Director Brain v2 visual assets should carry lifecycle status: `exploratory`, `candidate`, `approved`, `canonical`, `derived`, `rejected`, or `retired`. Locked canonical assets may not be silently regenerated.

## Real-media law
Before inventing technology, inspect `SYSTEM_INDEX.md`, `MEDIA_CAPABILITY_MATRIX.json`, `fx_v2/registry.json`, the generative engine, and relevant neutral capability folders. The production media plan deliberately selects suitable media forms rather than defaulting to stills + zoom or procedural geometry.

If generated media capabilities are selected, generated visual assets must actually exist and be recorded in `ASSET_MANIFEST.json`. A request to keep chat light or suppress previews never authorizes replacing required production media with geometric/procedural placeholders.

## Technical truthfulness
2.5D means depth/layer image-space motion. NeRF means an actual trained radiance field. 3DGS means actual Gaussian-splat scene primitives. A Gaussian light/noise field is not 3DGS. A custom reactive field is not projectM/MilkDrop unless that engine is actually used.

## Proof/QC law
Code existence is not proof. Preserve implementation/backend, parameters, proof render, QC, and keep/revise/reject decision. Effects must be visible in proof and survive export. Callable FX must pass the canonical gate/lock. Final acceptance requires inspection of the actual complete export.

Apply `MODE_AWARE_QC.md` according to the declared production mode. Technical export checks cannot compensate for the wrong visual behavior.

## Convergence law
When the current user accepts a full baseline, record its locator, SHA-256, and acceptance statement; lock the approved canon. If changes are requested, create a refinement scope with goal, allowed changes, forbidden changes, and restart authorization.

Default behavior after acceptance is local repair and comparison, not restart. The accepted master is itself a recoverable source of truth if intermediate material is lost.

## Delivery law
Keep the artistic master separate from a platform/delivery master when titles, intros, outros, packaging, or platform requirements differ. Do not overwrite an accepted artistic master merely to satisfy delivery packaging.

## Persistence
GitHub is the persistent brain; large binaries may live externally if branch manifests preserve identity/hash/role/recovery location.

## Final principle
The goal is not “AI pictures behind a song.” The goal is: **the song found its right visual form, and the system preserved what worked until it was finished.**
