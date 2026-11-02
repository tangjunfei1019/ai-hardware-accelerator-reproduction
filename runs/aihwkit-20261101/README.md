# Run evidence: AIHWKit (paper 31) — 2026-11-01

Upstream: https://github.com/IBM/aihwkit (not Junfei's code, not redistributed here).
This folder records one real upstream run only. See paper 31 in `papers/31-202106-aihwkit/`.

## Command

```bash
# upstream cloned separately to ~/workspace/aihwkit-upstream/ (HEAD 14d47831)
# environment: ~/workspace/aihwkit-venv/, Python 3.12.3, torch 2.15.0+cpu, aihwkit 1.2.0
~/workspace/aihwkit-venv/bin/python examples/01_simple_layer.py
```

## Result

- Single `AnalogLinear(4, 2)` layer with `ConstantStepDevice`, AnalogSGD (lr 0.1), 100 epochs, trained to sum its inputs, on CPU.
- Loss fell from 0.379 (epoch 1) to 0.0093 (epoch 100), with small analog fluctuations.
- Runtime: ~10 s. Full log: `aihwkit-example01.log` in this folder.

## Caveat

This proves the AIHWKit toolchain installs and runs end-to-end on CPU here. It does **not**
reproduce any specific AICAS 2021 paper accuracy table. Installed aihwkit 1.2.0 is the
current PyPI release, not a frozen 2021 version.
