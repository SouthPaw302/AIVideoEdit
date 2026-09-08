# The Door Between the Seconds — Render Repass / Gate Audit

Date: 2026-09-08
Render audited: `The_Door_Between_the_Seconds_RENDER_1080p.mp4`
SHA-256: `7fd4caf542a279f93a2b024fcc48b8508a896219f7d7b70eac120eee0d077cbb`
Branch: `song/the-door-between-the-seconds`

## Verdict

The working render is technically decodable and continuously changing, but it is **not ready to advance beyond STORYBOARD_LOCKED**. It fails the project-specific animation-density intent and lacks the repo-native evidence required by the later production gates.

The most important creative failure is that the render is still structurally a still-image montage with camera/atmosphere animation. The renderer applies per-frame push/pan/rotation, exposure/candle breathing, rain/embers and transient shifts, but it does not create the requested several authored key visual states per second, localized character animation, or short conventional-video inserts. The project contract specifically requires those things.

## Render technical inspection

- Container: MP4
- Video: H.264, yuv420p, 1920x1080, 30 fps
- Audio: AAC stereo, 48 kHz
- Container duration: 163.120 s
- Video stream duration: 163.100 s
- Audio duration: 163.120 s
- Decoded video frames: 4,893
- Script target frames: 4,894 (frames 0..4893)
- Result: **one scripted final frame is not present in the encoded video stream**
- Blackdetect: no >=0.5 s black segments
- Freezedetect: no >=1.0 s freeze segments
- Silencedetect: 0.000–1.0998 s silence at the opening; otherwise no >=1 s silence at -50 dB
- Source audio SHA-256 matches `ASSET_MANIFEST.json`
- Delivery is an upscale from the 960x540 native working render, not a native 1080p render

## Temporal-density inspection

- 27 editorial scenes across 163.12 s: mean scene span ~6.04 s
- 18 keyframe files feed those 27 scenes: ~0.11 keyframes/s
- Project-specific requirement: **several authored key visual states per second** in active passages
- The rendering code generates continuous pixel change primarily through global camera transforms, atmosphere, exposure and transient offsets
- No true localized protagonist animation pass is implemented for breath/eyes/hair/lace/velvet
- No conventional-video inserts are present in the working renderer
- Therefore: freeze detector PASS, but **meaningful authored-state density FAIL**

## Repo production gates, top to bottom

| Gate | Audit result | Evidence / blocker |
|---|---|---|
| INITIALIZED | PASS | Branch-local project files exist. |
| SOURCE_INGESTED | PASS | Current audio, lyrics and six current-chat stills are recorded; audio hash matches local master. |
| REFERENCES_ANALYZED | PASS | All six images are marked analyzed; music/lyrics/genre/rhythm/section analysis is complete. |
| APPROACH_ESTABLISHED | PASS with documentation correction | MEDIA_PLAN and REFERENCE_MANIFEST record current-user option 1 authorizing direct still reuse. Stale authority prose was corrected during this audit. |
| STORYBOARD_LOCKED | PASS | Locked frame-followable SCRIPT.json covers frames 0..4893 without script gaps; 27 lyric-bearing entries. Current GitHub production+narrative contract passed at this stage after metadata correction. |
| SHOT_PACKAGES_BUILT | FAIL | No repo-native `shot_packages/*/package.json` with hashed `media_evidence`; `media_evidence_verified=false`; ASSET_MANIFEST contains only the audio master and no generated visual asset evidence despite generated capabilities being selected. |
| SHOT_PROOFS_ACCEPTED | BLOCKED | Shot packages/proofs have not been registered or accepted. |
| FX_LOCKED | BLOCKED | `fx_lock_verified=false`; no verified project `fx.lock.json` for this production. |
| ASSEMBLED | BLOCKED | `assembly_complete=false`; scripted media has not been promoted through shot/proof/FX evidence gates. |
| FINAL_QC_PASSED | FAIL / NOT ELIGIBLE | Technical decode/black/freeze checks are good, but exact frame count is short by one frame and the export fails the requested animation-density/visual-state requirement. Creative acceptance is not recorded. |
| ARCHIVED | BLOCKED | `archive_complete=false`; final accepted media/storage evidence not registered. |

## Required repass before final promotion

1. Build real shot packages with hashed media evidence for the six supplied stills, generated continuation frames and every derived animation/video asset.
2. Register generated visuals in ASSET_MANIFEST.
3. Replace multi-second still-derived spans with dense authored state sequences: pose/face/hair/fabric/environment changes, not just camera motion.
4. Add actual short video inserts or materially animated shot sequences at high-energy/chorus transitions.
5. Produce and inspect shot proofs, then lock FX through the repo precompile gate.
6. Reassemble with exact SCRIPT frame coverage: 4,894 encoded video frames at 30 fps or revise the locked script/timeline coherently.
7. Render natively at delivery resolution if 1080p is the target rather than upscaling the 540p working master.
8. Re-run full export QC for repetition, identity continuity, loop seams, ghosting/flicker, framing, audio sync and narrative coverage before marking FINAL_QC_PASSED.

## Current disposition

**Keep stage at `STORYBOARD_LOCKED`. Do not promote this render to ASSEMBLED or FINAL_QC_PASSED.**
