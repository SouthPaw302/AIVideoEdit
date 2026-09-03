# Silver Coin — Decision Log

## SC-001 — Dedicated production branch

**Decision:** Silver Coin work lives on `song/silver-coin`.  
**Reason:** Every song receives its own recoverable branch and production chat/context.

## SC-002 — Style lock

**Decision:** Use **Living Pre-Raphaelite Folk Romanticism** as the primary visual language.  
**Source:** User supplied `imagine-d04b484c.mp4` and `imagine-5558fc80.mp4` and explicitly selected their visual style.

## SC-003 — Style versus subject

**Decision:** The clips define surface, palette, lighting, and motion quality. They do not require the same blonde woman, flower crown, woodland plot, or square framing.

## SC-004 — Existing Silver Coin narrative retained

**Decision:** Preserve the recovered village/road/wagon, firelit tavern, musicians/fiddler, dancing crowd, merchant/barmaid, and silver-coin motif, subject to precise mapping after lyrics are verified.

## SC-005 — Motion requirement

**Decision:** More animation per image is required. Slow zooms alone are insufficient. Use character performance, environmental motion, and reusable seamless loops.

## SC-006 — Effects discipline

**Decision:** Choose and document effects from `docs/VISUAL_STYLE_CATALOG.md`; do not add unrelated visual tricks.

## SC-007 — Persistence

**Decision:** Update GitHub after every meaningful phase and before chat/agent handoff. Small reference previews are committed to GitHub; larger originals remain in Library/workspace/object storage and are fingerprinted in the manifest.

## SC-008 — Neural Radiance Fields selected

**Decision:** The user explicitly selected Neural Radiance Fields and ordered production to proceed.

**Implementation:** This runtime lacks GPU, PyTorch, Nerfstudio, COLMAP, and a packaged NeRF stack. Silver Coin will use a compact CPU-trained NeRF MLP mapping 3D position plus view direction to volumetric density and color, combined with painted multi-plane scene geometry.

**Integrity:** Describe the result as hybrid neural-radiance-field spatial rendering. Do not falsely claim full photogrammetric reconstruction or Instant-NGP.

## SC-009 — Recovered song canon

**Decision:** Preserve the rustic early-1700s Central European tavern-folk world, lively 6/8 feel near 104 BPM, laborers ending the day in revelry, communal defiance, merchant betrayal, village characters, fiddler, mugs/stamping/dancing, tomorrow's debts/work, and the theme “poor in coin, rich in song.”

**Visual implication:** Keep the Living Pre-Raphaelite painted style but ground costumes, woodwork, tools, instruments, wagons, tavern behavior, and lighting in this folk world. Avoid modern drums, synth imagery, piano, orchestra, folk-rock staging, or polished contemporary performance language.
