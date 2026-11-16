# Code sources and reproduction notes: MICSim: A Modular Simulator for Mixed-signal Compute-in-Memory based AI Accelerator

## Reproducibility grade: B

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **B** (conda environment plus a pybind11 build of the NeuroSim v1.3 backend, Python 3.8).

## Upstream repository (verified to exist)

- Link: https://github.com/MICSim-official/MICSim_V1.0
- Verified HEAD (2026-11-16): 3395bb6
- Repository contents: accuracy evaluation (`Accuracy/`, quantized layers, configs), hardware performance evaluation (`Performance/`, NeuroSim v1.3 backend), example scripts (`script_example/accuracy`, `script_example/performance`), saved pretrained models
- Hardware / software requirements: Linux Ubuntu 20.04; conda environment from `environment.yml` (`conda env create -f environment.yml && conda activate MICSim`); compile the NeuroSim v1.3 backend with pybind11 (`cd ./Performance/NeuroSim && python3.8 setup.py build`, then add the built library directory to `PYTHONPATH`)
- License: no LICENSE file was found in the repository root — licence unverified; read the repository's own files before use.

## Reproduction steps

1) git clone https://github.com/MICSim-official/MICSim_V1.0
2) conda env create -f environment.yml && conda activate MICSim
3) Compile the NeuroSim v1.3 backend: `cd ./Performance/NeuroSim && python3.8 setup.py build` (adjust `include_dirs` in `setup.py` to the local pybind11 path), then add the built `lib.linux-x86_64-cpython-38` directory to `PYTHONPATH`
4) Test software performance: `python script_example/accuracy/main-cnn.py`
5) Test hardware performance: `python script_example/performance/main_cnn.py` (set the network structure in `Performance/src/Configuration.py` first)
Expected check: the accuracy script should report quantized-model accuracy and dump per-layer statistics (e.g. `avg_data.csv`); the performance script should report hardware overhead estimates. These are simulator estimates, not silicon measurements.

## What cannot be reproduced from the paper alone

- Simulator estimates must not be equated directly with real mixed-signal CIM chip measurements; quantization settings (e.g. LSQ, 8-bit weights/inputs in the example config), circuit architecture choices, and device parameters drive the results and must not be ignored.
- The skeleton in this directory does not run the NeuroSim backend and does not reproduce the paper's accuracy or hardware numbers.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
