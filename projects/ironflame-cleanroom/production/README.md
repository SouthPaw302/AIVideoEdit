# IronFlame Reference-Driven Production

The active assembly is reference-driven. The earlier `Molten Cartography` browser composition is retained only as historical proof and is not the final visual authority.

Final assembly uses:
- canonical IronFlame WAV reconstructed from `assets/audio/canonical-wav.parts/` and verified against SHA-256 `76679c5e0d0c905635e80904ff67ba03b52c11893d3a71f09433e17feff0f962`;
- `assets/visual/reference_movement_pack.zip`, containing 12 authorized 1280x720 movement variants spanning the entire 244.68-second reference sequence;
- deterministic bounded pan/zoom and short crossfades only, with harder cuts near the source-reference boundaries around 210s and 233s;
- project-local renderer `render_reference_cut.py` at native 24 fps.

The branch-only GitHub Action renders the final MP4, runs duration/resolution/fps/audio QC, builds a contact sheet and checksums, and publishes the final + QC bundle to the song's GitHub Release. Main is not modified by this production workflow.
