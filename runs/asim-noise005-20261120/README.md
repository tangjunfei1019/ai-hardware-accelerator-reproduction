# Run evidence: ASiM (paper 44), noise 0.05 — 2026-11-20

Upstream: https://github.com/Keio-CSG/ASiM (Apache-2.0; not this repository's code, not redistributed here).
This folder records one real upstream run only: the second ASiM run, with analog noise
turned on. The no-noise baseline (92.00% on the same 50-image subset) is in
`runs/asim-20261116/`. See paper 44 in `papers/44-202510-asim/`.

## Command

```bash
# same scratch clone ~/workspace/asim-upstream/ (HEAD 943eb5b) and the same dedicated
# venv ~/workspace/asim-venv/ (Python 3.12.3, torch 2.3.0+cpu, torchvision 0.18.0+cpu,
# numpy 1.26.4, pandas 2.2.2, matplotlib 3.8.0, easydict 1.13, pillow 13.0.0) as the
# baseline run; same 50-image CIFAR-10 subset and same pretrained weight
# resnet18_cifar10_w8a8_pact_trim_100.pkl in ~/workspace/asim-data/; no new downloads
# only change in main/config.py: conv and linear rand_noise_sigma and non_linear_sigma
# from 0.0 to 0.05 (the upstream README's simulation example value; the config unit is
# %, so 0.05 means 0.05% standard deviation). Everything else unchanged: cfg.device =
# 'cpu', cfg.test_bs = 1, cfg.test_workers = 0; W8A8 bit-serial, ADC 8-bit, nrow 255.
# (the lazy-model fix in main/src_simulation.py from the baseline run is still in
# place: only the selected model is built.)
cd ~/workspace/asim-upstream
OMP_NUM_THREADS=2 ~/workspace/asim-venv/bin/python -u -m main.src_simulation
```

## Result

- 50-image subset (5 images per class): Test Acc **92.00%** (46/50) in about 6.7 min,
  exit 0 — identical to the no-noise baseline.
  Misses, unchanged: label 0 → 8, label 2 → 6, label 4 → 1, label 7 → 2.
- Full log: `asim-forward-noise005.log` in this folder.

## Caveat

This proves the ASiM upstream runs with the 0.05 noise setting and produces inference
accuracy output on CPU here. It does **not** reproduce any TVLSI 2025 accuracy table,
and it is not a paper or silicon measurement; 92% is a simulator estimate on a 50-image
subset, not a validation-set result. It is a single run's result, and the simulation
does not seed its random number generator (`setup_seed` exists in `tools/common_tools.py`
but is only called in that file's own testbench), so the noise draw is random per run.
At this 0.05% noise level, no prediction on this subset changed.
