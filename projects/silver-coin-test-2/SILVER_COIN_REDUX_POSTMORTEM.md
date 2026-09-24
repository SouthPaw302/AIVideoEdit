# Silver Coin Redux — Agentic Production Postmortem

Status: production-learning record
Branch: `song/silver-coin-test-2`
Project: Silver Coin Test 2 / Silver Coin Redux
Comparison reference: `El_Viento_Route4_1080p_CREATIVE_LOCK_v5_review.mp4`

## Purpose

Record what succeeded, what failed, and what should become reusable AIVideoEdit production policy after comparing:

1. the agent-directed Silver Coin Redux production in Codex; and
2. the more automated El Viento sandbox/DeepSeek-harness production.

This record separates final creative quality from production efficiency. Silver Coin produced the stronger finished film, but its route to completion was too slow, token-intensive, and dependent on repeated user correction.

## Outcome

Silver Coin Redux succeeded because it developed cinematic and lyrical continuity: the heroine, workers, merchant, tavern, fire, coin, bridge, final chorus, dawn, and Mountain Noir bookends form a readable progression. The final export corrected the reversed-hand problem, used thirty new finished stills, preserved the remastered WAV, strengthened fire and architectural movement, and passed actual-export visual and technical QC.

The process was not efficient. It took multiple days, repeated rerenders, several incorrect assumptions, excessive status narration, and late discovery of problems that bounded proofs should have caught.

## What the agent did well

- Recovered from an initially incorrect repository path and ultimately booted the canonical AIVideoEdit runtime from current `main`.
- Read the project directives and preserved the song, lyrics, source media, and branch scope once the production was correctly grounded.
- Built thirty independent finished hero stills rather than reusing the rejected old-video reference set.
- Corrected the visibly reversed coin hand before final delivery.
- Preserved the strongest existing edit timing while replacing the visual source library.
- Improved lyric-to-image storytelling and maintained a recognizable heroine and tavern world.
- Escalated visual energy through chorus, bridge, rafters, fire, and dawn rather than applying one uniform effect everywhere.
- Used protected-person masks so faces, anatomy, the coin, and instruments were more stable than the animated surroundings.
- Added correct Mountain Noir intro/outro branding and a readable channel identity.
- Reviewed frames from the exported master, not only source stills or timeline assumptions.
- Verified duration, frame count, codecs, audio stream, decode integrity, black/freeze behavior, and file hashes.
- Delivered the final MP4 locally, in Downloads, on the Git branch, and in a structured Google Drive backup with a hash index.

## What the agent did poorly

- Initially followed or discussed the wrong repository and made claims before producing verifiable artifacts.
- Did not begin with a single authoritative boot, scope lock, and production-state readback.
- Allowed old visual references into an early attempt despite the explicit requirement for a totally new video.
- Generated storyboard-like material after the user had requested finished stills only.
- Underused the production-stage tooling already present in `main`, including analysis, shot packages, proof acceptance, FX locking, assembly, final QC, and archive operations.
- Treated stronger FX as a late finishing layer rather than defining a coherent recurring motion language before assembly.
- Ran expensive full renders before proving the entire pipeline from first frame through the final frame.
- Discovered a one-frame manifest/encoded-picture mismatch only after the FX pass reached the end.
- Relied on too many hard scene changes. Silver Coin has stronger narrative continuity than El Viento, but El Viento maintains substantially more continuous within-shot motion and smoother handoffs.
- Softened image detail through repeated processing. The measured median spatial sharpness of El Viento was about `1999`, versus about `1005` for Silver Coin V5.
- Used excessive commentary while waiting for renders, consuming attention and tokens without changing production state.
- Deferred organized backup and archival work until after the creative master was complete.

## Agentic Codex versus sandbox/harness findings

### Silver Coin Redux — agentic Codex strengths

- Stronger story and lyric interpretation.
- Better scene progression and emotional escalation.
- Better correction of anatomy and continuity faults.
- More deliberate character, prop, and environment choices.
- Correct Mountain Noir branding.
- Higher-quality H.264 profile and higher audio bitrate in the delivered master.
- Better final-film judgment.

### Silver Coin Redux — agentic Codex weaknesses

- Slower and more token-intensive.
- Too much manual orchestration and repeated rediscovery.
- Quieter median within-shot motion (`0.059` sampled flow versus El Viento's `0.289`).
- More visible hard cuts; automated scene detection found twenty-two high-confidence hard scene events.
- Less unified FX grammar across the whole film.

### El Viento — sandbox/harness strengths

- More continuous motion and smoother visual handoffs.
- Strong recurring red/gold-thread, portal, map, and ancestry motifs.
- Tighter visual-world continuity around one couple and one coastal-fantasy setting.
- Higher measured spatial edge detail.
- More repeatable automated production path.
- Lower expected agent-token cost for mechanical operations.

### El Viento — sandbox/harness weaknesses

- The file named `1080p` is actually encoded at `1280x720`.
- The branding reads `@MontañaNegra`, not the canonical Mountain Noir handle.
- Several long dissolves produce visible ghosting and muddy intermediate compositions.
- The edit is more visually continuous but less specific as lyric-driven storytelling.
- Lower audio bitrate and H.264 Constrained Baseline profile.
- Automated fluency did not prevent factual delivery and branding errors.

## Central lesson

The harness should own deterministic mechanics. The agent should own directorial judgment.

The production failed when agentic work replaced the harness. It succeeded when agentic judgment was applied to story, shot choice, continuity, visual repair, escalation, and final review. The best future workflow combines Silver Coin's creative direction with El Viento's continuous-motion discipline and the current-main production toolchain.

## Proposed production structure for future AIVideoEdit work

1. **Canonical boot**
   - Fetch and boot exact current `main`.
   - Record commit, project branch, production mode, and next canonical stage.

2. **Production contract lock**
   - Record source media, song, lyrics, forbidden references, platform, resolution, branch, accepted baseline, and deliverables.
   - Do not infer authorization to reuse rejected media.

3. **Evidence-producing analysis**
   - Hash and inspect source assets.
   - Map music structure and lyrics.
   - Record technical metadata and accepted media roles.

4. **Script and shot lock**
   - Create one authoritative script/shot manifest.
   - Every shot receives timing, story purpose, assigned media, provenance, and acceptance state.

5. **Finished-media generation**
   - A request for stills returns separate finished stills, not a storyboard or contact sheet.
   - Generate in bounded batches and register every accepted asset by hash.

6. **Proof ladder**
   - Single-shot motion proof.
   - Transition proof.
   - Section proof including first and final boundaries.
   - Full picture assembly only after those pass.

7. **FX design and lock**
   - Define one recurring project FX language before full assembly.
   - Select only registered canonical effects or explicitly bounded project-local effects.
   - Run precompile/runtime verification and write an immutable FX lock.

8. **Assembly ladder**
   - Picture master.
   - FX master.
   - Titles/audio delivery encode.
   - A full rerender requires a written change list and bounded affected sections whenever possible.

9. **Actual-export review**
   - Review every scripted section from the encoded export.
   - Check continuity, anatomy, identity, typography, branding, transitions, motion, color, and emotional ending.

10. **Technical QC**
    - Verify actual resolution rather than trusting filenames.
    - Verify codec/profile, frame rate, duration, frame count, audio channels/rate/bitrate, loudness, peaks, decode integrity, black/freeze behavior, and hash.

11. **Delivery and archive**
    - Copy the watchable file locally.
    - Commit the production record to its working branch.
    - Back up source media, accepted assets, docs/config, QC evidence, and master to Drive.
    - Verify the remote backup by metadata readback and hashes.

## Rules proposed for promotion to `main`

1. Boot before interpretation.
2. Lock scope and forbidden references before generation.
3. Never claim completion without a real artifact and verification evidence.
4. Maintain one authoritative shot/media/FX manifest.
5. Use a proof ladder before any full render.
6. Judge continuity before effect count.
7. Establish one recurring FX language per production.
8. Use the harness for mechanics and the agent for creative judgment.
9. Treat generated batches as finished independent media when requested.
10. Require a documented change list before rerendering.
11. Verify encoded properties rather than trusting filenames or labels.
12. Report only meaningful milestones during long jobs.
13. Automatically deliver, hash, back up, and verify accepted masters.
14. Promote only reusable project-neutral effects to `main`; keep song-specific assets and timing on the production branch.

## Efficiency policy

- Do not repeatedly poll or narrate unchanged render state.
- Do not rescan unchanged media or reread unchanged documents.
- Do not browse unrelated repositories or tools after the authoritative repo is known.
- Prefer bounded proofs and section rerenders over full rerenders.
- Reuse accepted timing, manifests, masks, and media when the requested change does not invalidate them.
- Record decisions once in the project so another agent can resume without reconstructing history from chat.

## Recommendation

Use Silver Coin Redux as the positive creative case and the negative efficiency case. Use El Viento as the positive automation/motion case and the negative delivery-validation case. Future AIVideoEdit work should require both standards: harness-grade reproducibility and agent-grade cinematic judgment.
