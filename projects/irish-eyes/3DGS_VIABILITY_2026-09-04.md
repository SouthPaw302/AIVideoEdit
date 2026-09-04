# Irish Eyes — Literal 3D Gaussian Splatting Viability Test

Date: 2026-09-04

Purpose: determine whether `Brandi South Florida 2017.mp4` contains enough real viewpoint change / background parallax to justify an actual Structure-from-Motion + 3D Gaussian Splatting reconstruction.

This is a preflight only. No 3DGS reconstruction is claimed.

## Method

A quick background-only camera-motion test was run at 360x640 proof resolution using:

- ORB features;
- background masks intended to reduce Brandi's influence;
- pairwise matching across widely separated source frames;
- RANSAC planar homography fitting;
- residual error after the planar transform.

If stable background pairs are explained very well by one planar transform with very small residuals, that is evidence that the source mostly contains rotation/pan/distant-planar motion rather than the strong multi-view translation/parallax a robust splat reconstruction wants.

Raw metrics are preserved in the active runtime as:

`projects/irish-eyes/3DGS_VIABILITY_METRICS.json`

## Stable-pair findings

Examples:

- frames 40→160: 222/300 homography inliers, 74% inlier ratio, median residual ~1.00 px, p90 ~2.30 px;
- frames 160→300: 274/300 inliers, 91.3% inlier ratio, median residual ~0.89 px, p90 ~2.12 px;
- frames 600→760: median inlier residual ~0.67 px;
- frames 760→920: median inlier residual ~0.64 px, though the lower inlier ratio indicates substantial composition/foreground change.

Some very wide pairs produced unstable homographies / low inlier ratios and therefore are not valid evidence of useful parallax by themselves.

## Interpretation

Current evidence does **not** justify spending production time on a literal 3DGS train for this source clip.

The most reliable background windows are explained too well by a planar/global transform at this scale, and the waterfront is dominated by distant horizon, sky, and water. The visible motion in the clip is much more valuable as real subject motion than as a multi-view scene capture.

This is not a claim that 3DGS is impossible. It means the current clip is a weak capture for it, and we will not use the 3DGS label unless a real reconstruction is actually trained and inspected.

## Production decision

For Irish Eyes with this source:

- continue using retained real motion;
- source-derived 2.5D / soft depth;
- temporal source reconstruction;
- independent water / sky fields;
- reflection portals;
- camera/perception design;
- Gaussian-shaped volumetric light fields (named honestly as light fields, not 3DGS);
- hybrid NeRF only where an actual radiance-field component is trained/rendered.

Reserve literal 3DGS for future footage with deliberate camera translation around a mostly static scene, or for additional real captures that provide meaningful multi-view baseline.

## Capture lesson for future projects

If we want true walk-inside-the-photo splats from real footage, shoot a 5–20 second arc / lateral translation around the environment while keeping exposure and focus stable and minimizing moving foreground subjects. That footage can then be camera-solved, splat-trained, cleaned in SuperSplat, and rendered with a new virtual camera path.