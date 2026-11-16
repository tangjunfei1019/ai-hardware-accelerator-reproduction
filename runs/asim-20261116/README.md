# Run evidence: ASiM (paper 44) — 2026-11-16

Upstream: https://github.com/Keio-CSG/ASiM (Apache-2.0; not this repository's code, not redistributed here).
This folder records one real upstream run only. See paper 44 in `papers/44-202510-asim/`.

## Command

```bash
# upstream cloned separately to ~/workspace/asim-upstream/ (HEAD 943eb5b)
# environment: a dedicated venv ~/workspace/asim-venv/, Python 3.12.3,
# torch 2.3.0+cpu, torchvision 0.18.0+cpu, numpy 1.26.4, pandas 2.2.2,
# matplotlib 3.8.0, easydict 1.13, pillow 13.0.0, gdown (for the downloads)
# (the shared aihwkit-venv could not be used: torchvision 0.29.2 does not
# import against torch 2.15.0+cpu; easydict and matplotlib are missing there)
# dataset: CIFAR-10 zip (184 MB) from the upstream README's Google Drive link,
# extracted to per-class PNG folders; weight resnet18_cifar10_w8a8_pact_trim_100.pkl
# (89.5 MB) from the upstream README's Google Drive link, both in ~/workspace/asim-data/
# config (main/config.py in the scratch clone): cfg.device = 'cpu',
# cfg.test_dir = <small subset>, cfg.pretrain_model_path = <downloaded .pkl>,
# cfg.test_bs = 1, cfg.test_workers = 0; W8A8 bit-serial, ADC 8-bit, nrow 255, no noise
# (main/src_simulation.py in the scratch clone was changed minimally so the model
# dictionary holds factory functions and only the selected model is built: as shipped
# it builds all 17 models eagerly, incl. ViT-H-14, which OOM-kills a small VM;
# the ResNet-18 computation itself is unchanged. The script must be run as a module,
# `python -m main.src_simulation`, because `python main/src_simulation.py` cannot
# resolve the `main` package.)
cd ~/workspace/asim-upstream
OMP_NUM_THREADS=2 ~/workspace/asim-venv/bin/python -u -m main.src_simulation
```

## Result

- 10-image subset (1 image per class): Test Acc **90.00%** in about 96 s, exit 0.
- 50-image subset (5 images per class): Test Acc **92.00%** (46/50) in about 7.5 min, exit 0.
  Misses: label 0 → 8, label 2 → 6, label 4 → 1, label 7 → 2.
- Full log of the 50-image run: `asim-forward.log` in this folder.

## Caveat

This proves the ASiM upstream builds, loads the pretrained W8A8 PACT weight, and produces
inference accuracy output on CPU here. It does **not** reproduce any TVLSI 2025 accuracy
table, and it is not a paper or silicon measurement; 92% is a simulator estimate on a
50-image subset, not a validation-set result.
