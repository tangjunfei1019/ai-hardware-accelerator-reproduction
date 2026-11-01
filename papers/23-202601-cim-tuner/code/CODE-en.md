# Code sources and reproduction notes: CIM-Tuner: Balancing the Compute and Storage Capacity of SRAM-CIM Accelerator via Hardware-mapping Co-exploration

## Reproducibility grade: A

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **A**.

## Upstream repository (verified to exist)

- Link: https://github.com/champloo2878/CIM-Tuner
- Repository contents: Python tools, cim_config/, nn_config/, experiments/, evacim/, Result/, requirements.txt (note the repository root file is named Readme.md)
- Hardware / software requirements: standard CPU, Python, see the upstream requirements.txt
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/champloo2878/CIM-Tuner
2) pip install -r requirements.txt
3) Follow the repository Readme.md to run the example configurations under experiments/
4) Change the area budget or macro configuration and observe the energy-efficiency / throughput Pareto change
Expected check: examples should output configurations and energy-efficiency / throughput estimates; as the area constraint tightens, the feasible configuration set should shrink.

## What cannot be reproduced from the paper alone

- The paper's silicon-validated accuracy cannot be directly reproduced; tool estimates must not be treated as tape-out measurements; area and process assumptions follow the paper and repository configurations.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
