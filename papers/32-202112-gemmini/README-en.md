# Gemmini: An Agile Systolic Array Generator

## Original paper information

- Original title: Gemmini: An Agile Systolic Array Generator Enabling Systematic Evaluations of Deep-Learning Architectures
- Authors: Hasan Genc, Ameer Haj-Ali, Vighnesh Iyer, Alon Amid, Howard Mao, John Wright, Colin Schmidt, Jerry Zhao, Albert Ou, Max Banister, Yakun Sophia Shao, Borivoje Nikolic, Ion Stoica, Krste Asanovic (UC Berkeley)
- Year and venue: arXiv:1911.09925 (2019, revised 2021); full system version at DAC 2021
- Upstream repository: https://github.com/ucb-bar/gemmini

## Core method

- Chisel generator: generates a systolic-array accelerator (matrix multiplication, plus activation, pooling, im2col and other deep-learning inference helpers), integrated with the Rocket Chip SoC generator; the host can be a Rocket in-order core or a BOOM out-of-order core.
- Supports output-stationary and weight-stationary dataflows, multiple data types, and a complete software stack (`libgemmini`), so the same design can be evaluated at system level rather than as an isolated array.
- The paper's evaluation uses FireSim (FPGA-accelerated cycle-accurate simulation) for design-space exploration; the selected design points achieve two to three orders of magnitude of speedup over a host processor on edge deep-learning inference (the paper's reported range; exact design points are as in the original paper).

## Core results

- Impact: Gemmini turned deep-learning accelerator design from one-off RTL engineering into a parameterised generator — systolic-array size, dataflow, data types and memory hierarchy can all be changed in configuration — and it became the standard open baseline in the RISC-V Chipyard ecosystem, including fabricated test chips in TSMC 16nm and Intel 22FFL.
- The 100–1000x range is not quoted here as a single "result", because the result depends on the chosen configuration; exact numbers are in the paper's design-space exploration cases.

## Reproduction points

- Reproduction goal: simulate systolic-array matrix multiplication with tiling, to understand how weights, inputs and partial sums flow through the array under an output-stationary dataflow.
- What to measure: effective multiplication counts and data-reuse trends at different tile sizes.
- What will not match the original tool: real Chisel generation, Verilator cycle simulation, FireSim FPGA simulation, and synthesis area and power; the skeleton only demonstrates the idea of tiled matrix multiplication.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas and cannot directly reproduce the paper's area, power or clock numbers.

## Verification notes for this entry

- The upstream repository was verified to exist via `git ls-remote`; it contains a Chisel RTL generator (`src/`, 61 Scala files counted), a software stack, a modelling directory and tests.
- The upstream build was not attempted end-to-end here, because a from-scratch Chipyard/Spike/Verilator build is a multi-hour toolchain job; the repository structure, README quick start, software tests and Chisel sources were verified to exist.
