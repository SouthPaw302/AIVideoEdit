# Reference Analysis

- Source: `1000100358.mp4`
- SHA-256: `a5acc4d880f9e4e4a46ffa4ae53aff8d96b60ce900edbbc377ece1c8737e9ded`
- Duration: 25.52 s container / 25.255 s picture stream
- Total picture frames: 631
- Repo short-reference rule: **all frames**
- Extracted/analyzed: **631 / 631**
- Format: vertical 720×1600 phone screen recording.

The embedded visual clip supplies the actual production language: paired pale-haired futuristic figures in matte-black suits, a sleek craft, barren pale terrain, warm sunset sky, restrained portrait staging, and subtle internal motion. Most of the surrounding phone/social UI is not part of the intended picture world.

A source-derived crop used only for analysis (`x=104, y=728, w=486, h=742`) hashes to `9fd5d2cead30df994ae6266609860a197340f13f9e62717262adbca3fd890b35`.

MainV2 `hero_library_extract.py` evidence:
- full screen: 1 selected useful frame, duplicate-heavy;
- cropped picture region: 101 dense candidates → 10 selected candidates, 91 near-duplicate rejections.

Conclusion: reference language is clear; coverage quantity is not. The production must create additional consistent source-faithful media rather than loop one weak clip.
