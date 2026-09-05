# Leave It by the Door — Full V2 Native-24 Render Plan

## Goal
Replace V1.1, which was visually under-sampled, with a true native 24 fps living-image production derived from the user-provided motion references.

## Delivery target
- 1280x720
- true 24 fps, every frame rendered natively
- H.264 CRF 16 shot masters
- AAC 320 kbps / 48 kHz final audio
- no 10→24 frame-rate conversion
- 25 resumable shot files
- final concatenation uses stream copy to avoid a second video generation

## Motion language
- camera movement is secondary
- internal scene motion is primary
- separate exterior weather, people/fabric/instrument, firelight, atmosphere, reflection, and particle layers
- reference clips are measured with optical flow and luminance changes; their motion signatures drive irregular movement rather than generic constant loops
- identity-safe masks damp motion around faces

## Effects in V2
- storm/cloud/ocean drift
- wave/foam bands
- rain and sea spray
- wet reflection shimmer
- smoke/fog advection
- warm/cool light migration
- fire/candle breath
- volumetric warm shaft breathing
- embers
- burden/ash motif
- lightning flash/reflection accents
- dawn birds and storm→gold progression
- pigment/fog travel transitions
- scene-fixed canvas grain

## Resumability
The local renderer accepts `SHOT_IDS` ranges. Production is split across independent workers, e.g. `SHOT_IDS=4-10`, `SHOT_IDS=11-18`, and `SHOT_IDS=19-25`. A completed H.264 shot is validated by expected native frame count and skipped on rerun.

## Current production checkpoint
Shots 1-3 were already completed at 1280x720/24 before parallel workers were launched. Remaining ranges are being produced independently. The final video is assembled only after all 25 shot files validate.

## Source of truth
Branch: `song/leave-it-by-the-door`
Renderer: `projects/leave-it-by-the-door/scripts/render_full_native24_v2.py`
Reference target notes: `projects/leave-it-by-the-door/REFERENCE_MOTION_TARGETS.md`
