# Beat This ONNX provider for Runtime V2

Runtime V2 uses Beat This only as an optional evidence provider for
`music_and_beat_analysis`. It never becomes production authority.

Pinned provider:

- conversion repository: `mosynthkey/beat_this_cpp`
- commit: `07ab790a9ec2eda8093d52d249e3ec4f0510ee72`
- model path: `onnx/beat_this.onnx`
- Git blob: `e2363cec9872bacf8867945b71ddaed879089995`
- expected bytes: `83077778`
- original model project: `CPJKU/beat_this`
- license: MIT

The model is deliberately not stored in AIVideoEdit git history.

## Provision

```bash
export AIVIDEOEDIT_REPO_ROOT="$(pwd)"
python -m pip install -r runtime_v2/requirements-onnx.txt
python -m runtime_v2.models.provision music.beat.beat-this-onnx.v1
```

Provisioning downloads the exact commit-pinned model into
`.aivideoedit/models/beat_this/beat_this.onnx` and verifies both its byte size
and Git blob identity before promotion from a temporary file.

## Preprocessing contract

The adapter reproduces the provider's documented C++ contract:

- mono 22,050 Hz audio
- 1024-point periodic Hann STFT
- hop length 441 (50 frames/second)
- 128 Slaney mel bands
- 30–11,000 Hz range
- amplitude spectrum divided by sqrt(1024)
- `log1p(1000 * max(mel_energy, 1e-10))`
- ONNX input `input_spectrogram`: `[1,time,128]`
- outputs: `beat`, `downbeat`
- 1500-frame chunks with six-frame borders
- local-max peak extraction and downbeat-to-nearest-beat snapping

If ONNX Runtime or the pinned model is absent, Runtime V2 falls back to the
existing AIVideoEdit `audio_map.py` analyzer when its dependencies are
available, then to the built-in CPU micro-DSP fixture analyzer.

The fallback is intentional: embedded inference adds evidence; it does not block
or redefine the production contract.
