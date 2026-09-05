# AIVideoEdit — Bible

This repository is the permanent operating system for creating dynamic long-form music films.

## 1. Branch law

- `main` contains only the production system, reusable cross-project technology, indexes, and templates.
- Every song/video production lives on its own branch: `song/<slug>`.
- Song-specific images, audio references, shot packages, storyboards, prompts, manifests, QC, renders, and decisions stay on that song branch.
- Generic reusable tools/effects developed during a song are promoted back to `main/general/reusable/`.
- Never put a complete song production back on `main`.

## 2. What we are making

The target is a directed long-form visual film for a song, not a slideshow, generic visualizer, or one source clip with weak effects.

A finished video should feel continuously authored through changing shots, depth, atmosphere, light, motion, environment, composition, transitions, and recurring visual motifs.

Silver Coin V8 is the current quality/motion benchmark for this production philosophy. Its art style is not mandatory for other songs.

## 3. Production order

1. Analyze the song and lyrics.
2. Define visual DNA and story.
3. Create/lock storyboard and shot map.
4. Build the asset/shot library before assembling the full movie.
5. Animate and composite selected shots.
6. Add music-directed behavior and transitions.
7. Assemble the timeline only when enough finished shot packages exist.
8. Render the complete movie.
9. Scan/QC the actual exported file.
10. Archive decisions, manifests, reusable methods, and final identity/checksums.

## 4. Storyboard rule

The storyboard is a production map, not merely a preview.

For each selected storyboard/source frame that becomes a scene, build a real shot package. Not every frame needs one; create enough strong packages to cover the full movie dynamically.

Recommended song-branch structure:

`projects/<slug>/shot_packages/<shot_id>/`

Possible contents:

- `source/` original frame/clip
- `alpha/` transparent subject/object plates
- `layers/` foreground / subject / midground / background / sky / water / props
- `depth/` depth maps, masks, mattes, holdouts, occlusion maps
- `generated/` real production support media
- `fx_assets/` fog, reflection, light, particles, prism, bloom, etc.
- `transition/` entry/exit assets
- `loop/` loop ingredients and approved loop render
- `preview/` short rendered proof of the intended shot
- `notes/` storyboard position, parameters, QC, approval state

Preview mode means create actual finished ingredients and short proof clips, **not** assemble the entire movie yet.

## 5. Reuse before invention

Before creating a new effect, loop, transition, spatial method, camera behavior, audio-reactive system, or QC utility, search:

- `general/reusable/CANONICAL_EFFECT_REGISTRY.md`
- `general/reusable/CANONICAL_EFFECT_REGISTRY.json`
- `general/reusable/PROJECT_TECHNIQUE_LINEAGE.md`

Then inspect the implementation under `general/reusable/`, especially `general/reusable/generative-engine/` before building a new song-level reactive analyzer or living-image runtime.

Do not recreate weaker substitutes for technology already built in another song.

A song may reuse another project's implementation without copying that project's art direction.

## 5A. Tool-first law

Before writing new code, first inspect the tools already available in the current environment and connected services.

The preflight should consider, when relevant:

- GitHub repository/search/branch/commit/tree/blob/Actions/artifact capabilities;
- existing AIVideoEdit reusable implementations;
- ChatGPT built-in tools and connected plugins;
- Cloudflare Wrangler CLI and the Cloudflare platform when available/authenticated;
- purpose-built media/storage services already connected.

Use existing proven capabilities before creating custom replacements.

### Cloudflare / Wrangler

Wrangler is a first-class infrastructure/storage tool for AIVideoEdit when it is available and authenticated.

Primary intended uses include:

- **R2** for large source media, frame archives, generated asset packs, proof renders, intermediate renders and final masters that do not belong in GitHub;
- **Workers** for lightweight asset/index APIs, signed-link helpers, render metadata services or production utilities when they materially help;
- **Pages/Workers delivery** for temporary review interfaces or browsable proof libraries when needed;
- **KV/D1/Queues or other Cloudflare services** only when a real production need justifies them.

Do not create Cloudflare infrastructure merely because it is available. Prefer the simplest path that improves persistence, recovery, transfer, review or automation.

Never store secrets in GitHub or manifests. Every large media object stored outside GitHub must retain a discoverable project manifest entry with filename/object key, size when known, checksum/hash when practical, role, and recovery location.

If Wrangler is not present or authenticated in the active runtime, record that limitation and continue using the strongest available local/connected alternative rather than pretending Cloudflare operations succeeded.

## 6. Canonical reusable technology

Current major trees:

- `general/reusable/generative-engine/`
- `general/reusable/silver-coin-tools/`
- `general/reusable/silver-coin-docs/`
- `general/reusable/depth-parallax-25d/`
- `general/reusable/irish-eyes-tools/`

The generative engine is the canonical shared timing/reactivity layer: analyze the song once, preserve a frame-aligned control bus, and let multiple visual systems consume the same smoothed RMS/onset/low/mid/high signals. Artistic parameter mappings remain song-specific and proof-gated.

The registry preserves implemented and recovered methods from Silver Coin, Irish Eyes, IronFlame, Leave It by the Door, Sigh No More, and broader production-system work.

Important classes already available include:

- 2.5D/depth parallax
- compact NeRF / hybrid radiance-field rendering
- 3D Gaussian Splatting as a distinct system option when actual splat data exists
- mesh/micro-motion and living-image motion
- atmosphere, fog, smoke, rain, embers, heat haze
- water/wet-road reflections
- halation/bloom/light shafts/glints
- transient/performance warps
- audio edit maps and audio-reactive controls
- shared frame-aligned reactive control bus
- organic generative visual plates for compositing
- pigment/object/recursive transitions
- integrated visualizer language
- temporal QC

## 7. Technical naming must stay honest

- **2.5D** = depth/layer-aware image-space motion.
- **NeRF** = an actual trained neural radiance field is rendered.
- **Hybrid NeRF** = a trained radiance-field component is composited with image/depth layers.
- **3DGS** = actual Gaussian-splat scene data/primitives are rendered.
- A Gaussian-shaped light field is not the same thing as 3D Gaussian Splatting.
- A custom music-reactive field is not projectM/MilkDrop unless that actual engine is used.

Never claim a technique merely because the result resembles it.

## 8. Effect proof rule

An effect does not count because code exists.

For meaningful effects preserve:

- source input
- method/backend
- parameters/preset
- proof render
- QC result
- keep/revise/reject decision

The effect must be visibly present in the rendered proof and must survive final assembly/export. Subtle is fine; invisible is not.

## 9. Loop rule

A reusable loop must record:

- source/range
- FPS/dimensions
- duration
- real / synthesized / generated / hybrid motion type
- entry/exit behavior
- seam method and crossblend duration if used
- return-to-start behavior
- seam QC
- freeze/duplicate/ghosting QC
- intended musical role

Mathematical endpoint similarity alone is not acceptance.

Avoid long crossfades that create double-image ghosting, especially with people.

## 10. Identity and source rule

Use real source media aggressively where it provides identity, motion, place, or continuity.

Generated media is encouraged where the story needs scenes or support footage that do not exist, but generated content must have a concrete production purpose.

For identity-bearing real people, protect facial/body identity and reject morphing, hallucinated anatomy, waxy restoration, obvious matte edges, and prolonged double exposure.

## 11. Music-directed rule

The song can drive:

- shot timing
- cut/transient accents
- motion density
- atmosphere
- reflection strength
- light/glint behavior
- camera amplitude
- transition timing

Prefer measured/smoothed controls over generic random movement or strobing. When several systems react to the same song, prefer one preserved generative-engine control bus over independent effect-specific re-analysis unless there is a documented reason to diverge.

## 12. QC law

A successful render command is not a finished video.

Before delivery, scan the actual exported movie for:

- black/damaged frames
- freezes or accidental still stretches
- repeated sections
- bad loop seams
- transition ghosting
- invisible/missing effects
- temporal flicker/texture boiling
- identity drift
- incorrect source leakage
- continuity errors
- aspect/framing issues
- full runtime and audio sync

Never hand off a final movie without inspecting the final file itself.

## 13. Persistence law

GitHub is the persistent brain, not necessarily the large-media bucket.

Store on the song branch:

- project rules and status
- storyboard/shot map
- manifests and hashes
- prompts and approved/rejected decisions
- practical-size source/reference assets
- masks, depth maps, previews, scripts, QC
- exact storage references for large binaries

Large masters/source libraries may remain in workspace/File Library/object storage such as Cloudflare R2 when necessary, but their identity and recovery location must be recorded.

## 14. Reusable-effect promotion law

If a useful method survives a real production test:

1. give it a stable name/ID;
2. preserve generic implementation/recipe;
3. record source project and validation status;
4. preserve proof/QC and failure modes;
5. add/update the canonical effect registry;
6. promote generic code/docs to `main/general/reusable/`.

A useful technique is not allowed to die inside a chat, temporary folder, branch note, or final MP4.

## 15. New-song rule

Create `song/<slug>` from `main`.

Minimum project package on that branch:

- `projects/<slug>/PROJECT.md`
- `projects/<slug>/STATUS.md`
- `projects/<slug>/LYRICS.md` when applicable
- `projects/<slug>/VISUAL_DNA.md`
- `projects/<slug>/EFFECTS_PLAN.md`
- `projects/<slug>/ASSET_MANIFEST.json`

Use `projects/PROJECT_TEMPLATE.md` as the starting structure.

## 16. Recovery rule

A new agent should read, in order:

1. `BIBLE.md`
2. `PROJECT_INDEX.md`
3. the canonical reusable-effect registry
4. `general/reusable/generative-engine/README.md` when the active work uses music-directed motion, living images or generated visual fields
5. the complete active song project's own branch and handoff/status files

Do not rebuild settled decisions from memory when the branch already records them.

## Final principle

The goal is not “AI pictures behind a song.”

The goal is: **the song became a visual world.**
