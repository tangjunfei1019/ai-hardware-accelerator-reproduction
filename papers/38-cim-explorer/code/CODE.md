# Code notes: CIM-Explorer (CIM-E): Optimizing Binary and Ternary Neural Network Inference on RRAM Crossbars

- **Upstream repository:** https://github.com/rpelke/CIM-E
- **Licence:** Apache
- **Hardware/software requirements:** Standard Linux CPU + Docker (or Podman, rootless supported); simulator build needs Python 3.10/3.11 with python3-dev; no RRAM hardware, GPU, or FPGA needed

## Completeness checklist

- Completeness: Apache licence; `src/` (compiler, experiment, model parser, ADC calibration, plotting), analog-cim-sim submodule, `models/`, `scripts/` (benchmark.bash, build_simulator.bash, build_tvm.bash), `docker/`, `util/`; CI checks for the simulator build and the Docker image.
- Upstream HEADs verified via `git ls-remote`: CIM-E f1bb4eac, analog-cim-sim fce1f36e.
- What cannot be reproduced on this machine: the Docker image build and full benchmark flow, which need a machine with Docker; running `main.py` bare is not the documented route.

## Minimal reproduction commands

See the "Reproduction points" section of this paper's README; commands and expected checks follow the upstream README.

## Skeleton note

- `reproduce.py` is an original skeleton using only the Python standard library, not upstream code; it demonstrates the core idea and does not reproduce the original paper's performance numbers.
- Reproducing the original numbers needs the upstream code, the corresponding hardware/toolchain, and the original data/configuration; the skeleton can only verify correctness and relative trends at the algorithm and dataflow level.

