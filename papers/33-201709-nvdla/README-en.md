# NVDLA: NVIDIA Deep Learning Accelerator (Open Architecture)

## Original paper information

- Original title: NVDLA Primer (NVIDIA official architecture document); system: NVIDIA Deep Learning Accelerator, open-sourced in 2017
- Authors/source: NVIDIA; originally designed for the Xavier SoC, later open-sourced as a parameterised architecture
- Year and venue: open-source release 2017–2018
- Upstream repository: https://github.com/nvdla/hw

> Note first: this is an open-system entry, not a conventional conference paper, and it is labelled as such so it is not mistaken for an ordinary conference paper.

## Core method

- Modular inference pipeline: convolution core (CDMA streams data into the convolution buffer, CSC sequencer, CMAC multiply-accumulate array, CACC partial-sum accumulation), followed by SDP (activation/bias/batch-normalization/element-wise operations), PDP (pooling), CDP (channel normalization), plus BDMA and RUBIK for data movement and rearrangement.
- Two programming modes: independent mode (each block configured separately) and fused mode (blocks pipelined through small FIFOs, saving one memory round trip).
- The `nvdlav1` branch in the repository is a non-configurable "full-precision" version, fixed at 2048 8-bit MACs or 1024 16-bit MACs; the master branch is the configurable version.

## Core results

- Impact: NVDLA was the first industry-grade, openly released deep-learning inference accelerator architecture — a complete, modular, extensible design that other companies and open SoC projects (including RISC-V SoC platforms) could actually integrate, rather than only a paper design.
- No single speedup is quoted here, because performance depends on the chosen configuration (small/large, 8-bit/16-bit); the authoritative sources are the Primer and the performance-estimation spreadsheet in the repository's `perf/`.

## Reproduction points

- Reproduction goal: simulate one inference pass through the pipeline — convolution → activation → pooling — and understand how the blocks chain together.
- What to measure: output sizes and value changes at each stage; do not treat the skeleton output as the paper's performance numbers.
- What will not match the original tool: the real Verilog RTL, SystemC C model, trace-replay tests, and synthesis area and power; the skeleton only demonstrates the pipeline idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas and cannot directly reproduce the paper's area, power or clock numbers.

## Verification notes for this entry

- The upstream repository was verified to exist via `git ls-remote`; it contains Verilog RTL (406 `.v` files counted under `vmod/`), a SystemC C model, a trace-replay testbench, synthesis scripts and performance estimates.
- The upstream build was not run end-to-end here, because `tmake` requires a complete Verilog simulation/synthesis toolchain configuration, which this VM does not have installed; the build was not attempted.
