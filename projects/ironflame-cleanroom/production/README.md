# Molten Cartography Production Source

`index.html` is the deterministic browser composition. `build_control_map.py` compiles the canonical `analysis/audiomap.json` into a compact browser control map immediately before QC/render. The canonical WAV is reconstructed only in the render environment into `production/assets/ironflame.wav`; the full master is not duplicated in Git.

Composition source SHA-256: `ec193a26dc82d6bc92b8d22e93e806b1f0684669159933ff82d81fe563ebdf51`
Control-map builder SHA-256: `2b2a8704bbe68bd233b98df85ac1a85c4858a7d5086610c433681e3bf1773733`
Timeline SHA-256: `03157ed1b7dace602bd2e4d688216261591b163d7dcc7d4cb11866b8988448e3`

No wall-clock time, random number generator, asynchronous timeline construction or historical IronFlame visual asset is used by the composition.
