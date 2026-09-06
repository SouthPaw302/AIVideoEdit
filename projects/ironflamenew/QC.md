# IronFlameNew QC

## Source/reference
- Master WAV decode: PASS.
- Reference MP4 decode: PASS.
- Full extraction: PASS, 145/145 each, 435 total.
- Historical-source contamination: NONE AUTHORIZED.

## Shot media
- 10 widescreen shot packages: PASS.
- 30 corrected representative rendered frames (8/50/92% of each shot): PASS internal visual review.
- First delivery candidate was rejected before release for rectangular source-crop leakage in crystalline scenes and weak warm-presence geometry.
- Corrected crystalline/ribbon pixels were re-authored from REF-C geometry/motion language; warm presence was re-authored from REF-B head geometry.
- Medieval/warrior/wolf/sword/castle/portal/title contamination: NONE.

## Canonical FX
- Corrected manifests passed the FX v2 precompile gate.
- fx.lock.json verified against the corrected renderer/manifests.

## Final export
- File: IronFlameNew_FINAL_720p24.mp4
- SHA-256: `84344a93f7b5129845966655bdc28ef936447da8436d5637aadcce8448243509`
- Size: 90,061,352 bytes.
- Video: H.264, 1280x720, 24 fps, 5872 frames, 244.666667 s.
- Audio: AAC stereo, 48 kHz, 244.65 s.
- Full decode: 5872/5872 frames PASS.
- Black frames: 0.
- Exact duplicate adjacent pairs: 0.
- Long freezes: 0.
- Mean adjacent-frame delta: 0.411555.
- Boundary/contact-sheet review: PASS. Major visual-world changes are intentional hard editorial cuts at structural motif changes, not corruption.
- Final result: **PASS**.

## Repair policy learned in production
For a localized visual defect, do not regenerate the entire song. Render only the affected frame/shot range with the locked renderer and splice it into the accepted base master while preserving base audio. Full rerender is reserved for genuinely global changes (renderer/runtime, global color pipeline, frame rate/resolution, audio synchronization, or inputs affecting the whole film).
