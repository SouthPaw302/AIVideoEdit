# IronFlameNew Handoff

## Authority
Current user instruction -> this branch guarded state/manifests -> current main. No historical production context authorized.

## Current state
`FINAL_QC_PASSED`.

## Completed
- 435/435 reference frames extracted/analyzed.
- Current WAV analyzed to 24 fps controls.
- Clean visual DNA/storyboard locked from the three supplied references.
- 10 widescreen shot packages built.
- First delivery candidate rejected internally for visible source-crop leakage and weak presence geometry.
- Corrected assets re-authored and 30 representative frames passed visual QC.
- Corrected FX lock regenerated and verified.
- Accepted base master completed and passed full 5872-frame export QC.
- Accepted master SHA-256: `84344a93f7b5129845966655bdc28ef936447da8436d5637aadcce8448243509`.

## Repair rule
Do not rerender the full song for localized defects. Use `render_patch.py` for the exact shot/frame range, then `splice_patch.py` to replace that range while preserving the accepted master audio. Full rerender is only for global changes.

## Remaining
Archive/publish the accepted master if required. Do not alter the accepted base without creating recorded patch/QC evidence.
