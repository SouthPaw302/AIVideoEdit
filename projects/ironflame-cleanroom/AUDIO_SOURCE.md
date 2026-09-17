# Canonical Audio Source

Recovered audio only from historical IronFlame archive.

- Reconstructed filename: `Ironflame (Remastered).wav`
- PCM: 48 kHz, 16-bit, stereo
- Duration: 244.680 seconds
- Expected SHA-256: `76679c5e0d0c905635e80904ff67ba03b52c11893d3a71f09433e17feff0f962`
- Parts: `assets/audio/canonical-wav.parts/part-*`

Reconstruct:

```bash
cat projects/ironflame-cleanroom/assets/audio/canonical-wav.parts/part-* > 'Ironflame (Remastered).wav'
sha256sum 'Ironflame (Remastered).wav'
```

The SHA-256 must match exactly before the audio is accepted as ingested.
