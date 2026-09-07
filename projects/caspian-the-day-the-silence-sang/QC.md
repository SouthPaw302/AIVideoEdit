# QC — Music-only abstract hybrid

## Reference verification
- supplied reference `None.mp4`: 6.041667 s, 560×560, 24 fps, 145 frames
- short-reference rule applied: **all 145 frames extracted and inspected**
- selected production anchors: frames 0, 36, 72, 96, 120, 144

## Media proof
Initial 18-second hybrid proof used direct material masks between alternating supplied/generated portraits. Review of sampled proof frames showed a double-face/ghosting risk when source compositions differed. That transition design was rejected.

Accepted revision: every state change collapses through the reference's resolved dark-material frame before the next image emerges. This preserves the supplied clip's material-takeover grammar and prevents direct portrait-to-portrait ghost blends.

Accepted proof: `hybrid_motion_proof.mp4`, SHA-256 `8badc28f7669180789f3411db0cace6762215fa39aaec24e0149d60aa526f119`.

## Final export
Accepted master: `A_Thousand_Doors_HYBRID_v3_720p.mp4`
- container duration: **180.640000 s**
- video: H.264, 1280×720, 24 fps, 4335 frames, 180.625 s video stream
- audio: AAC, 48 kHz stereo, 180.640 s
- SHA-256: `2957c2290ac48a56c9503afe40c086aaca2ea1fd7c246405fd1cca40620f0b38`

Actual-export QC:
- full video decode errors: **0**
- blackdetect events (d=0.3, pic_th=0.98, pix_th=0.05): **0**
- freezedetect events >2.5 s at -45 dB: **0**
- timeline script coverage: frames 0–4334 with no gaps
- hybrid-media requirement: PASS — 6 supplied-frame anchors + 8 generated companion stills
- lyric exclusion: PASS — no lyric cue or lyric-derived scene is present in the locked script
- reference-style requirement: PASS — near-locked compositions, internal flow, dark material midpoint and sparse warm fissures are present throughout

Durable binary archival remains pending; do not mark `ARCHIVED` yet.
