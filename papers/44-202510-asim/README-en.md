# ASiM: Modeling and Analyzing Inference Accuracy of SRAM-Based Analog CiM Circuits

## Original paper information

- Original title: ASiM: Modeling and Analyzing Inference Accuracy of SRAM-Based Analog CiM Circuits
- Authors: Wenlun Zhang, Shimpei Ando, Yung-Chin Chen, Kentaro Yoshioka
- Year and venue: IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2025 (vol. 33, no. 10, pp. 2838–2851)
- arXiv / DOI: arXiv:2411.11022; DOI 10.1109/TVLSI.2025.3605286

## Core method

- A simulation framework for evaluating inference accuracy in SRAM-based analog compute-in-memory (ACiM) systems: existing simulation tools rarely target SRAM-based ACiM and give inconsistent accuracy predictions, so ASiM provides a standardized, circuit-aware evaluation methodology.
- High-fidelity modeling of the critical effects in charge-domain architectures: ADC quantization, bit-parallel encoding, and analog noise; supports CNNs and Transformer models such as ViT, scaling to ImageNet-scale classification.
- Users can drop ASiM modules into their own DNN models, with all configurable arguments in `config.py`; two modes — Train (training / fine-tuning) and Simulation (bit-wise simulation) — plus noise-aware training (`trim_noise`) for more robust models.
- Explores hybrid analog-digital execution and majority voting as robustness schemes; extension examples cover RRAM crossbars, full weight bit-parallel operation, and current-domain SRAM ACiM.

## Core results

- As reported in the paper (see the original): bit-parallel encoding can improve energy efficiency with only modest accuracy degradation; however, even 1 LSB of analog noise can significantly impair inference performance, particularly in complex tasks such as ImageNet; hybrid analog-digital execution and majority voting enhance robustness without negating energy savings.
- Simulation times from the upstream README (full validation set): ResNet-18 / CIFAR-10 (W4A4) takes about 6000 s on an i9-13980HX and about 230 s on a laptop RTX 4080; ViT-B-32 / ImageNet (W8A8) takes about 19841 s on an A6000.
- Peak performance: no comparable peak number is given (this tool is accuracy-oriented).

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (how inference accuracy changes with noise and encoding choices) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Run evidence

- Upstream run on 2026-11-16: ResNet-18 / CIFAR-10 small subset (5 images per class, 50 total), W8A8 bit-serial, ADC 8-bit, nrow 255, no noise, about 7.5 min on CPU, Test Acc 92.00% (46/50). See [runs/asim-20261116/](../../runs/asim-20261116/). This proves only that the upstream runs and produces accuracy output here; it does not reproduce any TVLSI 2025 accuracy table and is not a silicon measurement.
- Upstream run on 2026-11-20 (noise 0.05): same 50-image subset and weight; conv and linear rand_noise_sigma and non_linear_sigma changed from 0.0 to 0.05 (the upstream README example value), everything else (W8A8, ADC 8-bit, nrow 255) unchanged; about 6.7 min on CPU, Test Acc 92.00% (46/50), identical to the no-noise baseline, with the same 4 images misclassified. See [runs/asim-noise005-20261120/](../../runs/asim-noise005-20261120/). This is a single run's result; it does not reproduce any TVLSI 2025 accuracy table and is not a silicon measurement.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers. ASiM itself is a simulation tool, and its outputs are simulator estimates, not silicon measurements; ResNet-18 / CIFAR-10 can run on CPU, but the full validation set takes about 6000 s on an i9, so a light test can only use a small subset, and ImageNet / ViT runs are recommended on GPU; pretrained weights are provided through Google Drive links in the upstream README.
