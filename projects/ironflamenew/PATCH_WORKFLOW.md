# IronFlameNew Frame-Range Patch Workflow

Localized QC defects must be repaired without a song-length visual rerender.

1. Preserve the accepted full base master and its SHA-256.
2. Identify the exact shot or frame range that is defective.
3. Correct only the affected source/layer/mask/recipe assets.
4. Regenerate/verify FX lock evidence if any locked pixel-changing input changed.
5. Render only the affected range using `render_patch.py`.
6. Validate patch frame count, dimensions and 24 fps against the declared range.
7. Use `splice_patch.py` to replace only that video range in the base. The base audio stream is copied unchanged.
8. Run the full export QC again on the patched master and record a new SHA-256.

A full visual rerender is allowed only when a change is genuinely global: renderer/runtime logic, global color pipeline, resolution/fps, audio synchronization, or an input affecting essentially the whole film.
