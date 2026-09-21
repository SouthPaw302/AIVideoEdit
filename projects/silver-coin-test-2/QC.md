# Final QC — Silver Coin Test 2

Result: PASS for the technical and director-mode review of this candidate master. This does not record user artistic acceptance; `OPERATING_ORDER.accepted_baseline.status` remains `none`.

- Master: `outputs/silver-coin-test-2/Silver_Coin_Test2_RepoCompliant_1280x720_24fps_fullframes.mp4` (branch repository output), SHA-256 `7d91825f59470c0997dcb144b219f2bd35c64f691c6f9a9a29354e20deb6b03eb`.
- Full decode PASS. H.264, 1280×720, 24 fps, 4,979 video frames / 207.458333 seconds; AAC stereo from the authorized 207.44-second WAV. Picture extends 18.3 ms beyond the audio tail, less than half a video frame.
- The initial `-shortest` mux trimmed one picture frame and was rejected; the corrected mux preserves all 4,979 frames.
- Five picture batches: 808 + 1,129 + 1,130 + 921 + 991 frames; every renderer exit code 0, stderr empty. The picture join is stream-copy, without a second visual encode.
- No black spans at 0.15-second / 5% pixel threshold. Audio integrated loudness -16.4 LUFS, LRA 5.0 LU, true peak -2.5 dBFS.
- Repository temporal scan: 623 samples; 29 risk spikes, all explained by the 29 planned hard cuts; zero unexplained risks. Median sampled frame difference 0.00351, median optical flow 0.03335.
- Generic freeze detection at -40 dB marks the deliberately restrained still-based motion as static. At -60 dB it flags one approximately one-second hold at 99.125–100.125 seconds in the merchant/coin beat; this is a real subtle-motion limitation, not a corrupt or duplicated segment. The contact sheet and proof show distinct scenes and stable protected identity. No claim of continuous character performance or fully animated footage is made.
- Representative contact sheet reviewed across intro, mill, tavern, merchant, bridge, final chorus, and dawn. Faces and hands remain legible; no prior Silver Coin render or reference appears.
- FX precompile lock verification PASS for the repository's byte-verified canonical living-scene FX set. The promoted FX proof in current main has a mismatched binary checksum, so those promoted IDs were not claimed in this lock. The project renderer uses its documented painterly-motion implementations and the proof and production use the same backend.

