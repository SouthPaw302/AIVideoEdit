# Scene 03 QC Record

## Completed pre-media checks

- **Audio duration:** source is 98.04 seconds; editorial range locked to exactly 98.00 seconds.
- **Frame calculation:** 98.00 × 24 fps = 2,352 frames.
- **Script coverage:** entries begin at frame 0 and end at frame 2351.
- **Continuity:** no gaps or overlaps between the eight script entries.
- **Score identity:** SHA-256 recorded in source authority, asset manifest, score analysis and script.
- **Stem package:** 12 stems verified at matching duration; vocal stems contain no meaningful vocal performance.
- **Dialogue:** no new dialogue or captions falsely claimed.
- **Picture status:** no Scene 03 images or video have been generated, reviewed or accepted.
- **Branch status:** active production remains `project/american-empire-act1/scene-03`.

## Not yet testable

The following remain **NOT RUN / NOT PASSED** because picture media does not exist:

- identity and anatomy continuity
- apartment/hallway/elevator/lobby/street topology
- generated-continuation temporal stability
- living-scene visible motion
- 2.5D depth and crop safety
- weather and source-light coupling
- caption placement
- audio/picture sync
- shot proofs
- FX lock
- assembly QC
- final artistic acceptance

## Runtime gate

The repository's current generic production guard still requires a narrow compatibility update for the explicitly declared `project/<slug>/scene-XX` hierarchy. Do not mark runtime bootstrap PASS until that change is merged to repository `main`, synchronized into the project branches and verified by the existing production-contract workflow.
