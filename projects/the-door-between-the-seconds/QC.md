# QC — Pandora current gate status

## Current authority
- Subject: Pandora the Vampire
- Timeline: 34 scripted shots, 30 fps
- Cold open: 6.0 seconds of intended silence before music
- Current formal project state: not final; `final_qc_passed` remains false

## Gate rebuild after current-main QC update
The current-main acceptance rule invalidated the earlier "render looks good" acceptance path. The production was rebuilt through the current contracts:
- narrative contract: repaired and passed
- production contract: repaired and passed
- FX V2 precompile/lock: regenerated and verified
- canonical reusable FX runtime: enforced by renderer before frame emission
- project capability proofs: built for reflection/perspective/transition behavior
- 34 shot packages and shot proof records: created for the gate-compliant v2 path

## User-driven framing/motion revision
After that gate rebuild, the user identified additional framing and camera-energy issues. The renderer was changed again:
- portrait/tall stills now preserve subject height and use a widescreen extension background instead of aggressive center-crop;
- selected architecture shots use wider bounded crops;
- selected impact/departure shots use bounded transient-driven impact sway inspired by the accepted kinetic language from Leave It by the Door;
- random/global shake is still not used as the default motion source.

Because renderer inputs changed, the complete proof chain must be rerun before final acceptance.

## Latest patched export-variety checks
Patched full-length picture candidate:
`production/final_pandora_v2_gate/pandora_picture_960x540_v3patch.mp4`

Patched muxed candidate:
`production/final_pandora_v2_gate/The_Door_Between_the_Seconds_PANDORA_FINAL_540p_v3patch_mux.mp4`

- 3-second export-variety QC: PASS; no similar runs
- 5-second export-variety QC: PASS; no similar runs

The two earlier strict-review runs at 51–57 s and 138–144 s were locally repaired.

## Final acceptance
**PENDING.** Do not set `FINAL_QC_PASSED` until the current renderer/framing revision has gone back through all shot proofs and final decode/black/freeze/audio-sync/variety/manual-cinematic checks.
