# Status

Machine stage: **SHOT_PROOFS_ACCEPTED**.

All 11 proof recipes are explicitly accepted. A complete 1920x1080 full-length master candidate has now been rendered and technically QC'd at the locked 2704-frame timeline.

Master candidate SHA-256: `2ea60fb7c1f99d528527be106a3c95df966ff45678c4a6f6962556fa4a9096eb`.

The production-approved runtime-native FX requirements are now recorded in `FX_REQUIREMENTS.json`. The machine stage intentionally remains SHOT_PROOFS_ACCEPTED until the canonical FX v2 precompile gate produces and verifies `fx.lock.json`.

Next: canonical FX lock, then promotion/rerender to ASSEMBLED.
