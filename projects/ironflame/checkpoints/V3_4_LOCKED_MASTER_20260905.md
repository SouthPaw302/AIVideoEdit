# IronFlame V3.4 — Locked Master Recovery Checkpoint

**Branch:** `song/ironflame-20260905-0216`

## Master
- Sandbox master: `/mnt/data/ironflame_work/assembly_v34_locked/IRONFLAME_V3_4_LOCKED_MASTER_1080P24.mp4`
- Resolution: 1920x1080
- Frame rate: 24 fps
- Video frames: 5,872
- Container duration: 244.680 s
- SHA-256: `393abdfb536fe3c0ee61a3f092e83017483fd168271c5ef6b4a62e3d9479e867`

## Canonical runtime / lock
- Runtime SHA-256 used in locked shot compile: `2dc55b4c052fa01e732dbef4d20f718f40f2036af97708716b23af98ef1bafa3`
- GitHub Action: `IronFlame FX V2 Lock Gate`
- Run ID: `34005496884`
- Job `ironflame-lock-gate`: SUCCESS
- Hard gate and immediate immutable lock verification both passed.
- Lock artifact: `ironflame-fx-lock`, artifact ID `9980789945`, artifact digest `sha256:2e9720045f440ada82d52198ababc4338d4c9a11934c6f8b3657ba3dce6b913a`

## Production grammar
Frame effects executed through canonical FX2 runtime:
- `FX2-MOTION-002`
- `FX2-LIGHT-001`
- `FX2-LIGHT-002`
- `FX2-SURFACE-001`

Selected transitions executed through canonical runtime methods:
- `FX2-TRANS-001` pigment gate — short 6-frame handoffs on transformation boundaries
- `FX2-TRANS-003` light peak handoff — 12-frame handoffs where light/orb is the narrative object

Selective authored-depth spatial shots use conditional `FX2-SPATIAL-004` preflight input on shots 01, 06, 09, and 12. This remains honestly labeled 2.5D living parallax, not NeRF or 3DGS.

Long-held scenes 03, 08, 10, and 11 use sparse editorial reframing/camera cuts on top of already locked FX renders to reduce slideshow feel without inventing new effect IDs.

## Export QC
Full exported master was decoded frame-by-frame and also scanned with FFmpeg `blackdetect` + `freezedetect`.

Results:
- 5,872 / 5,872 video frames decoded
- zero black frames detected
- zero freeze runs >= 1.5 s detected
- FFmpeg blackdetect: no events
- FFmpeg freezedetect: no events
- mean adjacent low-res delta: `0.5063419341`
- p05 adjacent delta: `0.0534722222`

## Recovery rule
If a later agent damages the project, restore to this branch checkpoint and recover the binary from the sandbox/workspace archive if still available. Do not resume from the old V2/V3 alpha assemblies.
