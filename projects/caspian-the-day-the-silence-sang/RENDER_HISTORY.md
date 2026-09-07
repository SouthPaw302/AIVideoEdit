# Render History — Music-only abstract hybrid

1. Current reference video re-extracted under the short-reference rule: all 145 frames preserved for analysis/control.
2. Six reference frames selected as exact production still anchors: 0, 36, 72, 96, 120, 144.
3. Eight generated companion stills accepted after user approved the reference-matched abstract look.
4. Built `RFMT-001 Reference-Flow Material Takeover`: Farneback optical-flow control from all 145 frames, reference-luma takeover masks, smoothed audio-RMS deformation control.
5. Rendered 18 s proof. Direct portrait-to-portrait material blend showed ghost/double-face risk in sampled transition frames; rejected that transition mode.
6. Revised transitions to A → resolved dark reference material → B. Proof logic accepted.
7. Full working picture rendered in twelve contiguous ~15 s 640×360 / 24 fps chunks to stay within sandbox execution limits; reference flow remained a lower-resolution control field.
8. Chunks concatenated to a 180.625 s / 4335-frame silent working master.
9. Delivery encode V1 used a padded 4336th video frame; rejected for frame-count mismatch.
10. V2 restored 4335 video frames but AAC timing ended at 180.608 s; rejected as audio timing mismatch.
11. V3 remuxed the 4335-frame video with a fresh AAC encode from the original WAV and a controlled audio pad to exact 180.640 s container/audio duration.
12. V3 passed decode, black-frame, freeze and creative hybrid/reference-style QC.

Accepted master SHA-256: `2957c2290ac48a56c9503afe40c086aaca2ea1fd7c246405fd1cca40620f0b38`.
