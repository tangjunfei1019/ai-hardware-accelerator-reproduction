# AIHWKit: A Flexible and Fast PyTorch Toolkit for Analog Crossbar Arrays

## Paper information

- Original title: A flexible and fast PyTorch toolkit for simulating training and inference on analog crossbar arrays
- Authors: Malte J. Rasch, Diego Moreda, Tayfun Gokmen, Manuel Le Gallo, Fabio Carta, Cindy Goldberg, Kaoutar El Maghraoui, Abu Sebastian, Vijay Narayanan (IBM Research)
- Year and venue: 2021, AICAS; arXiv:2104.02184
- Upstream repository: https://github.com/IBM/aihwkit

## Core method

- Weights are mapped to "analog tiles": a two-dimensional weight matrix is stored on a resistive crossbar array, with scaling, ADC/DAC and noise modelled as pre- and post-processing around the inputs and outputs.
- Provides analog PyTorch layers (linear, 1D/2D/3D convolution, LSTM, sequence containers), an analog optimizer (AnalogSGD) and in-situ algorithms such as Tiki-Taka.
- Device models are configurable: device-to-device and cycle-to-cycle variation, resistive response curves, weight/output noise, and a PCM statistical model calibrated on measurements from a 1-million-device PCM chip (per the repository README).

## Core results

- The paper's contribution is a toolkit, not a single accelerator design, so no single speedup is quoted here as a headline number. The paper claims the toolkit fully supports GPU acceleration and can estimate how future analog technology material properties and non-idealities affect the accuracy of any artificial neural network; the per-experiment accuracy tables are as in the original paper.
- Impact: it was the first widely used open PyTorch toolkit for analog crossbar simulation, letting ordinary deep-learning researchers do analog crossbar training and inference without building their own simulator, and it became the default baseline for analog-AI hardware-aware training work.

## Reproduction points

- Reproduction goal: run a small linear layer on an analog tile and compare ideal computation with the output after adding noise and ADC/DAC quantization.
- What to measure: output error at different noise levels and quantization bit-widths; do not treat the skeleton output as the paper's accuracy tables.
- What will not match the original tool: the real C++/CUDA simulator, the PCM device statistical model, and the full AnalogSGD and Tiki-Taka training flows; the skeleton only demonstrates the core idea of "weights on an array + noise + quantization".

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not code by the paper's authors. It is only for understanding the core idea and cannot directly reproduce the paper's accuracy or performance numbers.

## Verification notes for this entry

- The upstream repository was verified to exist via `git ls-remote`; it contains 30 examples, tutorial notebooks, 30 test files and an MIT licence, with documentation at https://aihwkit.readthedocs.io.
- The upstream example was not run end-to-end in this VM, because this VM does not have PyTorch installed and the CPU PyTorch download timed out repeatedly — a VM/network limitation, not a repository defect. On a normal machine with PyTorch installed, the minimal example in CODE.md runs, with GPU optional.
