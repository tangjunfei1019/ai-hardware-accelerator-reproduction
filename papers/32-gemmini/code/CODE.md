# Code sources and reproduction notes: Gemmini

- Link: https://github.com/ucb-bar/gemmini
- Nature: official open-source generator, Chisel RTL.
- Licence: UC Regents licence (`LICENSE`, redistribution is conditional — read that file before redistributing).

## Completeness checklist

- [x] Real code, not just a PDF: Chisel RTL generator (`src/`, 61 Scala files), software stack (`software/libgemmini`, `software/gemmini-rocc-tests`), modelling (`modeling/`)
- [x] Installation/run instructions: README "Quick Start" (Chipyard + Spike configuration, software build, Verilator simulator build)
- [x] Examples: `software/gemmini-rocc-tests` (from matrix-multiplication tests to ResNet-50-level programs), JSON test configurations (`gemmini-tests.json`, `gemmini-smoke.json`)
- [x] Tests: `src/test/` Scala tests
- [x] Hardware requirements: a standard Linux machine suffices for the generator and Spike/Verilator simulation; FPGA (FireSim) is optional, for fast cycle-accurate simulation; no custom silicon is needed to run the generator

## Minimal upstream reproduction steps (documented path)

```bash
git clone https://github.com/ucb-bar/chipyard.git
cd chipyard
./build-setup.sh
source env.sh
cd generators/gemmini
make -C software/libgemmini install
cd chipyard/generators/gemmini/software/gemmini-rocc-tests
./build.sh
# Build the cycle-accurate simulator under chipyard/sims/verilator:
make CONFIG=GemminiRocketConfig
```

Expected check: RISC-V binaries (bare-metal, Linux and proxy-kernel versions) appear under `build/`, and the `GemminiRocketConfig` Verilator simulator builds successfully. This is a heavy build (Chipyard + RISC-V toolchain + Verilator); budget hours, not minutes, for a first run.

## Parts that cannot be reproduced from this entry alone

- Real RTL synthesis area, power, clock frequency and FireSim cycle-accurate performance require the full toolchain and the chosen configuration; the skeleton only demonstrates tiled matrix multiplication.
- The reason the upstream build was not attempted end-to-end here: the multi-hour toolchain build was not attempted.

## Skeleton in this directory

`reproduce.py` is an original standard-library skeleton demonstrating tiled matrix multiplication and the output-stationary idea, unrelated to the upstream code.
