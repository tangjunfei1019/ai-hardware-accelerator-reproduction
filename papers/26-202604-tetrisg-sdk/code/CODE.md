# Code sources and reproduction notes: TetrisG-SDK: Efficient Convolutional Layer Mapping with Adaptive Windows and Grouped Convolutions for Fast In-Memory Computing

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A**.

## Upstream repository (verified to exist)

- Link: https://github.com/SybilD/TetrisG-SDK
- Repository contents: TetrisG_SDK.py, Tetris_SDK.py, .ipynb demos, a NeuroSim directory, demo video and flow chart (note the repository root file is named readme.md)
- Hardware / software requirements: standard CPU, Python; the repository contains .py / .ipynb files and a NeuroSim directory — install dependencies per the repository readme.md
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/SybilD/TetrisG-SDK
2) Install dependencies per readme.md
3) First run TetrisG_SDK.py or an .ipynb small example to confirm window search and grouping logic
4) Then run CNN8 and other model configurations and compare against the paper's tables
Expected check: small examples should output window configurations and utilization; model configurations should output latency / energy estimate trends.

## What cannot be reproduced from the paper alone

- Skeleton utilization numbers must not be treated as NeuroSim simulation results; grouped convolution's accuracy constraints must not be ignored — the paper states near-lossless results, subject to the paper's experiments.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
