# IronFlame — Audio Recovery

Canonical lossless source supplied for this production:

- filename: `Ironflame (Remastered).wav`
- PCM: 48 kHz, 16-bit, stereo
- duration: 244.680 seconds
- SHA-256: `76679c5e0d0c905635e80904ff67ba03b52c11893d3a71f09433e17feff0f962`

GitHub also contains a 320 kb/s MP3 working reference split into small binary parts so connector upload limits do not strand the production in one chat.

Reassemble from the repository root:

```bash
cat projects/ironflame/assets/audio/working-reference.parts/part-* > ironflame-remastered-working-reference.mp3
```

Expected reconstructed MP3 SHA-256:

`1a60e360c99e961792eee7d14c35ca3bfe8c80c156d08b05a76dc326ce248a2b`

Use the reconstructed MP3 for analysis, timing, previews, and assembly recovery. Use the canonical WAV for the final master mux whenever the lossless attachment is available.

