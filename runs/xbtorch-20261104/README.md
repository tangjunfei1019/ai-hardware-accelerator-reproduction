# Run evidence: XBTorch (paper 22) — 2026-11-04

Upstream: https://github.com/ADAM-Lab-GW/xbtorch (BSD-3-Clause; not this repository's code, not redistributed here).
This folder records one real upstream run only. See paper 22 in `papers/22-202610-xbtorch/`.

## Command

```bash
# upstream cloned separately to ~/workspace/xbtorch-upstream/ (HEAD 57b119d)
# environment: ~/workspace/aihwkit-venv/, Python 3.12.3, torch 2.15.0+cpu, xbtorch 1.0.0
# install (README's `pip install -e xbtorch` does not match the repo layout;
# the working install was `pip install -e . --no-deps` from the repo root,
# plus qtorch 0.3.0, ninja 1.13.2 (must be on PATH), transformers 5.22.1;
# lm_eval, smt and matplotlib were not installed and were not needed here)
PATH=~/workspace/aihwkit-venv/bin:$PATH ~/workspace/aihwkit-venv/bin/python xbtorch-tiny-mlp.py
```

The script `xbtorch-tiny-mlp.py` in this folder follows the upstream README Getting Started
example: a 2-layer perceptron `SimpleMLP(10, 5, 2)` patched with `xbtorch_model`, with
`xbtorch.optim.SGD`, run for one forward pass on a small random input.

## Result

- `xbtorch.initialize()` succeeded; `xbtorch_model` patch succeeded; `xbtorch.optim.SGD` created.
- Input `torch.randn(4, 10)` returned output shape `(4, 2)`, as expected for 10 inputs and 2 outputs.
- Runtime: ~12 s. Exit code 0. Full log: `xbtorch-forward.log` in this folder.

## Caveat

This proves the XBTorch module builds, patches a model and runs one forward pass on CPU here.
It does **not** reproduce any APL Machine Learning 2026 accuracy table, and it is not a
paper or silicon measurement.
