# AGENT HANDOFF — AIVideoEdit / The Door Between the Seconds / Pandora the Vampire

## Project authority
- Repository: `SouthPaw302/AIVideoEdit`
- Active branch: `song/the-door-between-the-seconds`
- Current main authority at handoff time: `0fada7f78453339acea864dfbd1edfe73fb9ddec`
- Branch already contains the merge of that main QC update.
- Local project root used by the current ChatGPT production session: `/mnt/data/AIVideoEdit_local/projects/the-door-between-the-seconds`

## Locked user canon
- Lead subject: **Pandora the Vampire**.
- The lyrics are the narrative spine.
- A **6-second silent cold open** introduces Pandora before the music starts.
- Do **not** scrap the existing media. Reuse useful recovered material inside the lyric-driven story.
- The recurring candle/window/chamber imagery is Pandora's **memory-home motif**, not the entire film.
- The user explicitly authorized creating more media and using the supplied videos.
- The user wants the more kinetic camera-angle/motion energy previously achieved on **Leave It by the Door**, including impact sway and camera attitude changes, while avoiding generic uncontrolled whole-frame shake.
- Some prior still/animation framing was out of frame. Future passes must preserve Pandora's head/body and important architecture rather than blindly center-cropping portrait assets into 16:9.

## Story structure
1. Silent Pandora cold open.
2. House beneath rain / threshold.
3. Dust, iron and memory responding to her.
4. Walls and reflections recognizing her.
5. Sleeping distance opens into cathedral-scale space.
6. Quiet thunder / gravity instability.
7. Endless hallway.
8. Almost-touch / temporal contact.
9. Second chorus expands the world.
10. Crypt, underground sanctuary and dawn.

## Current canonical documents
- `LYRICS.md`
- `STORYBOARD.md`
- `SCRIPT.md`
- `SCRIPT.json`
- `SHOT_LIST.md`
- `MEDIA_PLAN.json`
- `VISUAL_DNA.md`
- `PROJECT_STATE.json`
- `FX_REQUIREMENTS.fx.json`
- `fx.lock.json`

## Current production code
- `production/build_pandora_final.py`
- `production/build_shot_packages_from_v2.py`

The current renderer verifies `fx.lock.json` before emitting production frames and routes the reusable motion/atmosphere/light layer through approved FX V2 IDs.

## Current framing repair
`build_pandora_final.py` was patched after user review:
- Tall portrait stills now use a **subject-preserving full-frame extension** instead of aggressive 16:9 center cropping.
- Portraits keep more of Pandora in frame while an extended/blurred background fills the widescreen canvas.
- Wide/environment shots use bounded crops that favor architecture.
- Camera motion was reduced from blanket zoom behavior and augmented with **bounded transient-driven impact sway** on selected high-energy shots.

## Current localized cinematic patches
The strict 3-second export-variety scan previously returned REVIEW at:
- 51–57 s
- 138–144 s

Those runs were repaired locally:
- `S11–S12`: Pandora/cathedral beat now transitions toward architectural takeover and deeper cathedral space instead of holding one repeated composition.
- `S29–S30`: dawn passage now hands off into crypt/descent imagery rather than holding the same bridge/portrait composition.

## Latest QC result for the patched assembly
Patched picture candidate:
`production/final_pandora_v2_gate/pandora_picture_960x540_v3patch.mp4`

Patched muxed candidate:
`production/final_pandora_v2_gate/The_Door_Between_the_Seconds_PANDORA_FINAL_540p_v3patch_mux.mp4`

Latest export-variety checks on the patched candidate:
- 3-second QC: **PASS**
- 5-second QC: **PASS**

Records:
- `production/final_pandora_v2_gate/FINAL_VARIETY_3S_v3patch_mux.json`
- `production/final_pandora_v2_gate/FINAL_VARIETY_5S_v3patch_mux.json`

## Important gate history
After main changed, the previous render could no longer be considered accepted. The updated gate exposed and repaired:
- invalid project stage advancement;
- noncanonical SCRIPT.json shape;
- missing local LYRICS.md during continuation reconstruction;
- renderer/media-plan capability mismatch;
- rejected endless-hallway proof;
- later 3-second final-export variety failures.

The narrative and production contracts were repaired. A current FX lock was regenerated and verified. Shot packages/proofs were built for the gate-compliant v2 path. The user then requested further framing and camera-motion revisions, which created the current v3 patch path.

## Current project-state truth
Do **not** claim `FINAL_QC_PASSED` yet.

The patched v3 candidate clears the specific 3-second and 5-second variety failures, but the complete proof/QC chain must be rerun after the latest renderer/framing changes before final acceptance. `PROJECT_STATE.json` therefore remains `final_qc_passed: false`.

## Existing media that must remain available
Created stills:
`resume_payload/created_images_jpg/`

Reference stills:
`resume_payload/reference_images_jpg/`

Video assets:
`resume_payload/video/`

Important video assets:
- `gothic_window_8s_fullscreen_720p.mp4`
- `The_Door_Between_the_Seconds_REPASS_FAST_540p.mp4`

The first is an accepted motion/cold-open benchmark. The second contains usable supplied/recovered video material and audio source material.

## Proof/QC locations
`proofs/current_gate/`

Important records include:
- `CAPABILITY_PROOF.json`
- `SHOT_PROOF_QC.json`
- revised hallway/perspective/rain proof media and contact sheets

## Final production/QC directory
`production/final_pandora_v2_gate/`

Important records include:
- `RENDER_METADATA.json`
- original v2 3s/5s variety reports
- patched v3 3s/5s variety reports
- patched contact sheets
- patched picture and muxed candidate video

## Next-agent priorities
1. Rescan current `main` before work; merge newer system law if main advanced.
2. Boot against current main/branch authority.
3. Preserve the patched framing behavior.
4. Use the supplied video and create genuinely new media when it improves story progression; do not solve every beat by reframing the same portrait.
5. Continue the more cinematic **Leave It by the Door**-style camera energy where musically motivated, but keep internal scene motion primary.
6. Rebuild any shot packages invalidated by the latest renderer changes.
7. Rerun the complete current proof/QC chain: guards, FX lock, shot proofs, decode, black/freeze, cold-open silence, 3s and 5s variety, and manual cinematic scan.
8. Only then set `final_qc_passed: true` and archive/promote the final output.

## Resume in one sentence
Resume from the **Pandora v3 framing/motion patch**, keep all useful recovered media, add new media where the story needs it, rerun the complete current gate, and do not declare final until every current proof/QC check passes.
