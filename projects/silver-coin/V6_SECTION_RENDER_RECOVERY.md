# V6 Section Render Recovery

Silver Coin V6 is rendered as six global-time chunks at 960x540/12fps, concatenated losslessly at the intermediate MPEG-4 stage, then upscaled once to 1280x720 and muxed with the canonical WAV.

Why: the CPU environment can render each section reliably even when one monolithic encode exceeds the execution window. Each frame uses the original global song timestamp, so camera motion, audio envelopes and transition halves remain continuous across chunk boundaries.

Chunk global frame ranges at 12fps:

1. 0-471 (0:00-0:39.333)
2. 472-991 (0:39.333-1:22.667)
3. 992-1243 (1:22.667-1:43.667)
4. 1244-1657 (1:43.667-2:18.167)
5. 1658-2117 (2:18.167-2:56.500)
6. 2118-2488 (2:56.500-3:27.417)

The renderer intentionally favors strong source paintings over scene count. Reuse is achieved with new crops, angle paths, scale paths, palette response and effect intensity driven by the music.

This sectioned method is now preferred for long CPU renders because a failed section can be regenerated without rerendering the whole film.