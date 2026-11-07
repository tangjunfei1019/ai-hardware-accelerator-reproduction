# Run evidence: TetrisG-SDK (paper 26) — 2026-11-04

Upstream: https://github.com/SybilD/TetrisG-SDK (HEAD 4c97363, last commit 2024-03-28;
no licence file found in the repository root — licence unverified; not this
repository's code, not redistributed here).
This folder records one real upstream run only. See paper 26 in `papers/26-202604-tetrisg-sdk/`.

## Command

```bash
# upstream cloned separately to ~/workspace/tetrisg-upstream/ (HEAD 4c97363)
# environment: system Python 3.12.3, standard library only (math, random)
# TetrisG_SDK.py is interactive: it asks for a network key and a group number,
# so both were fed on stdin (network cnn8-3, group 2)
printf 'cnn8-3\n2\n' | python3 TetrisG_SDK.py
```

## Result

- Config: array 512x512, image 18x18, kernel 3x3, channels 32x32.
- Im2col 256, SDK 64, SDK 16, **VW-SDK 48**; optimal PW shape **8x4x16x42**.
- Grouped path: No. of PW 16; 8 windows for 10x6 plus 8 marginal-optimized,
  total windows 16.0; grouped **Total CC 32.0**.
- Runtime: instant. Exit code 0. Full log: `tetrisg-sdk.log` in this folder.

## Caveat

This proves the TetrisG script runs one configuration here and outputs its own
window and cycle numbers. It does **not** reproduce any JETCAS 2026 paper speedups,
and it is not a silicon measurement. The NeuroSim C++ part of the repository was
not built or run. No licence file was found in the upstream repo root; check the
authors' licence terms before redistributing or building a product on it.
