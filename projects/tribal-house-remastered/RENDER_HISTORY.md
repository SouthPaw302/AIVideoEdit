# Render History — Tribal House Remastered

## Preserved production history

### Early batch motion proofs
- Batches 01-09 produced standalone still + motion/FX packages.
- Purpose: establish continuity, picture quality, and representative local motion.
- Status: preserved inputs, not final FX treatment.

### Early 305-second assembly proof
- Duration: 305.000 seconds
- Cadence: 24 fps
- Resolution: 1280x720 review proof
- User review: continuity acceptable; picture quality acceptable; FX explicitly very early/provisional.
- Decision: preserve base imagery/continuity and expand FX rather than restart.

### Full FX expansion / prelock proof
- Canonical audio map and 24fps reactive-control bus created.
- Three full FX packs archived.
- Nine music-synced section proofs passed.
- Eight authored transitions integrated.
- Heavy-FX prelock assembly passed exported-film technical QC at 305.000 seconds / 7,320 frames / 24 fps.
- Status: prelock diagnostic proof; not final master.

### Formal FX lock
- Workflow: Tribal House Project FX Lock
- GitHub Actions run: 36043449083
- Result: PASS
- Lock: `projects/tribal-house-remastered/fx.lock.json`
- Schema: aivideoedit-fx-precompile-v2
- Evidence fingerprint: `3d5dc69ca4a9018a6aeb54b1c5a9db03dbdc48e11a671108770d283fe380822e`
- Branch commit containing lock: `f0702ef386a988527f55591a442a4fc55b01c60b`

## Next render
Rebuild the full 305-second assembly from the formally locked FX package, preserving global song time and accepted base continuity. Then run actual-export mode-aware QC before any final-master/archive claim.
