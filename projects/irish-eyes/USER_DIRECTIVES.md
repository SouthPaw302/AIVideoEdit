# Irish Eyes — User Directives

These directives override presentation habits and production defaults.

1. **Do not create additional storyboards.** The project already has sufficient storyboard/concept material.
2. **Do not use generative AI video or image-to-video as the production method.** Irish Eyes is source-derived cinema. Do not use text-to-video, image-to-video, synthetic character generation, AI lookalikes, or generated replacement footage unless the user explicitly changes this directive.
3. **Real footage and real extracted frames are the visual truth.** `Brandi South Florida 2017.mp4` and its frame set are the primary visual material.
4. **Make existing material come alive instead of replacing it.** Approved approaches include real-motion retiming and looping, optical flow/interpolation, masking/rotoscoping, alpha plates, compositing, 2.5D depth separation, Structure-from-Motion, photogrammetry, 3D Gaussian Splatting, source-trained reconstruction, conventional/procedural VFX, particles, water/reflection systems, refraction, halation, bloom, volumetrics, camera moves, zoom/perception effects, color grading and editorial finishing.
5. **3D Gaussian Splatting is specifically encouraged when the source provides enough real viewpoint/parallax coverage.** Reconstruct the real waterfront/environment from real source frames, then navigate/render it with a real-time splat renderer such as PlayCanvas/SuperSplat. Do not reconstruct Brandi as a synthetic identity-bearing splat; protect/mask the moving human subject and composite her separately where required.
6. **If the source does not contain enough viewpoint information for convincing 3D reconstruction, do not hallucinate missing geometry.** Fall back to strong source-derived 2.5D, neighboring-frame reconstruction, clone/paint from actual source material, optical compositing, or clean original footage.
7. **Machine-learning tools may be used as analysis/reconstruction aids only when they do not replace the source visually.** For example, camera solving, segmentation or depth metadata may assist the edit; they must not silently invent a new person, environment or shot.
8. **Procedural effects are allowed and encouraged.** Shader-driven fog, rain, mist, light shafts, reflection distortion, particles, lens effects, chromatic/prism behavior and similar VFX are treatments of the real material, not substitute AI-generated scenes.
9. **Prioritize rendered moving footage.** Work should advance through enhanced real footage, source-derived loops, 2.5D shots, real 3D reconstruction, PlayCanvas/SuperSplat camera moves, optical transitions, compositing, scene assembly and final video renders.
10. **No concept art for its own sake and no generated support footage.** If an asset is created, it should be derived from or directly support the real source: mask, matte, depth map, reflection plate, optical layer, procedural VFX element, reconstruction file, transition element, grade reference, or render output.
11. Keep work in the current chat/project workflow. Do not move production to ChatGPT Work unless the user explicitly requests it.
12. Ask for more real user footage only when a specific missing real-world shot or additional parallax coverage would materially improve the finished film.
13. **Do not preview internal frame/contact-sheet assets in chat unless the user explicitly asks.** Internal QC is fine.

## Governing visual philosophy

The goal is not to create an AI-generated video. The goal is to take real captured imagery and use modern computational cinematography, spatial reconstruction, VFX and professional editing to reveal movement, depth and perception that were latent in the source.

The picture should feel as if the real photograph or footage opened into a navigable world — while remaining recognizably the same real captured moment.
