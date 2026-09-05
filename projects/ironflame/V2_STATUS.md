# IronFlame V2 — Active Status

**Branch:** `song/ironflame-20260905-0216`  
**Started:** 2026-09-05  
**Canonical runtime source:** `main@e6ba077cabeed8e799090d3d505d82bc96d2fd02`

## Current state

Production is actively using the new generative-engine roadmap and FX V2 system.

Completed:

- three supplied reference videos fully decomposed to native frames (145 each / 435 total);
- 12-frame contact-sheet extraction for each reference;
- hard visual-style lock written in `V2_REFERENCE_STYLE_LOCK.md`;
- 12-shot lyric/hero structure written in `V2_HERO_SHOT_MAP.md`;
- full song analyzed at native production 24 fps using the canonical reactive-control algorithm;
- 5,873 frame-aligned control records generated;
- generated support media constrained to the REF-A / REF-B / REF-C language;
- V2.0 rough cut assembled and final-file QC performed;
- V2.1 targeted REF-B revision built after dead-zone detection;
- V2.2 rebuilt all 12 scenes with shorter hero holds, stronger restrained source-preserving push/drift, and substantially more of the actual supplied reference-video motion;
- V2.2 final exported movie scanned at reduced QC resolution with `blackdetect` and `freezedetect`;
- V2.2 produced zero black events and zero >=2-second freeze events at the selected QC threshold.

## V2.2 review render

- duration: 244.666667 s picture / 244.680 s canonical audio target
- resolution: 1280x720
- frame rate: 24 fps
- video: H.264
- audio: AAC from `Ironflame (Remastered).wav`
- SHA-256: `80f165f947fc1a3db41f32f8a52b160adcdb17af63a304a066a76b054dd403db`
- Library: `/AIVideoEdit/IronFlame_V2_20260905/IRONFLAME_V2_2_REVIEW_720p24.mp4`
- Library ID: `libfile_33fe581a1b8081919e94c4125c277638`

Compact review:

- `/AIVideoEdit/IronFlame_V2_20260905/IRONFLAME_V2_2_COMPACT_540p24.mp4`
- Library ID: `libfile_a7a6a263b5dc8191b08a55895758007b`
- SHA-256: `615044c88f31e9faaeffb5a6b21984fb637edda8e3e01807ef7f60bf54222de1`

QC log:

- `/AIVideoEdit/IronFlame_V2_20260905/V2_2_QC.log`
- Library ID: `libfile_fe125238e4388191ba8117546d4121b2`

## V2.2 edit rule

This revision does **not** introduce a new visual-effects family. Every scene alternates between generated hero/support plates and the matching supplied REF-A / REF-B / REF-C source motion. The supplied examples remain the style and motion veto.

The new generative-engine control bus remains the shared audio-analysis source. It informs motion strength and scene energy; it does not authorize unrelated visualizer effects.

## Next production actions

1. Review V2.2 picture for artistic pacing and lyric/emotional correspondence, not just technical motion survival.
2. Refine any shot whose generated support media drifts from the supplied reference language.
3. If the picture is approved, produce a higher-quality master encode and final contact-sheet/QC evidence.
4. Preserve all accepted/rejected decisions and exact hashes before promotion.