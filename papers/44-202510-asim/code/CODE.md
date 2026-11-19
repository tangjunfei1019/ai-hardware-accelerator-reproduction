# Code sources and reproduction notes: ASiM: Modeling and Analyzing Inference Accuracy of SRAM-Based Analog CiM Circuits

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A** (Python + torch; ResNet-18 / CIFAR-10 can run on CPU, on a small subset for a light test).

## Upstream repository (verified to exist)

- Link: https://github.com/Keio-CSG/ASiM
- Verified HEAD (2026-11-16): 943eb5b
- Repository contents: ASiM simulation modules (`module/`), DNN models (`model/`), datasets (`dataset/`), main simulation and training scripts (`main/src_simulation.py`, `main/src_train.py`), example configs (`examples/`), extensions (RRAM, full weight bit-parallel, current domain)
- Hardware / software requirements: Python 3.11.7, torch 2.3.0, numpy 1.24.3, matplotlib 3.8.0, easydict 1.13. ResNet-18 / CIFAR-10 can run on CPU; ViT on ImageNet is recommended on a GPU server. Pretrained weights are provided through Google Drive links in the upstream README.
- License: Apache-2.0.

## Reproduction steps

1) git clone https://github.com/Keio-CSG/ASiM
2) Install the environment (Python 3.11.7, torch 2.3.0, numpy 1.24.3, matplotlib 3.8.0, easydict 1.13)
3) Download a pretrained model weight (Google Drive links in the upstream README, e.g. `resnet18_cifar10_w8a8_pact_trim_100.pkl`) and the CIFAR-10 dataset
4) Set the dataset path (`cfg.test_dir`) and pretrained weight (`cfg.pretrain_model_path`) in `./examples/resnet18_cifar10/config.py`, using a small subset for a light test
5) Run `./main/src_simulation.py`
Expected check: the simulation should report inference accuracy under the configured ADC precision, bit-parallel encoding, and analog-noise settings; the upstream README's timing table says the full ResNet-18 / CIFAR-10 validation set takes about 6000 s on an i9 CPU, so a light test must use a small subset. Results are simulator estimates, not silicon measurements.

## What cannot be reproduced from the paper alone

- Simulator estimates must not be equated directly with real SRAM ACiM chip measurements; ADC quantization, bit-parallel encoding, and analog-noise parameters are models of circuit behaviour, and their values must come from silicon measurement or the paper's settings, not from the skeleton.
- The skeleton in this directory does not run the ASiM modules and does not reproduce the paper's accuracy numbers.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.

## Run evidence

- Evidence folder: [runs/asim-20261116/](../../runs/asim-20261116/)
- Evidence folder: [runs/asim-noise005-20261120/](../../runs/asim-noise005-20261120/) (noise 0.05 run, 2026-11-20)
