# CIM-Explorer (CIM-E): Optimizing Binary and Ternary Neural Network Inference on RRAM Crossbars

## Original paper

- **Authors:** Rebecca Pelke, José Cubero-Cascante, Nils Bosbach, et al. (RWTH Aachen University)
- **Venue:** SAMOS 2025; arXiv:2505.14303
- **Upstream repository:** https://github.com/rpelke/CIM-E
- **Licence:** Apache
- **Hardware/software requirements:** Standard Linux CPU + Docker (or Podman, rootless supported); simulator build needs Python 3.10/3.11 with python3-dev; no RRAM hardware, GPU, or FPGA needed

## Core method

- At compile time, a TVM-based compiler stack (with a Larq frontend) optimises a binary/ternary network for execution on a crossbar, with multi-batch support and crossbar-specific optimisations such as maximising weight reuse; arbitrary crossbar sizes are supported.
- At runtime, weights are prepared according to the compute mode; several backends can execute, including different simulators.
- A design-space exploration (DSE) tool automates finding optimal crossbar parameters and mappings, so accuracy can be estimated early for a given crossbar before committing to a chip design.
- Key distinction: most RRAM-CIM tools cover only compilation, simulation, or DSE, and usually assume 8-bit quantization; this tool ties all three together for binary/ternary networks.

## Core effect

- The contribution is the toolkit and its DSE flow, not one accelerator's speedup; per-model, per-mapping accuracy results are authoritative in the original paper, and no single headline number is quoted here.
- For low-precision analog CIM researchers, this is the most complete open starting point found in this search: compilation, simulation, and DSE close the loop in one repository.
- Note on the repository name: the correct link is `rpelke/CIM-E`; `rpelke/CIM-Explorer` was verified not to resolve and must not be used.

## Reproduction points

- Minimal reproduction (Docker route, as documented): `git clone --recursive https://github.com/rpelke/CIM-E.git` (including the analog-cim-sim submodule), `./models/download_models.bash` to download pre-compiled binary/ternary models, `docker build -f docker/build_simulator.dockerfile -t cim-e .` (or `docker pull docker.io/pelke/cim-e:latest`), then run the benchmarks per `scripts/benchmark.bash` and the README's "Run Simulations" section.
- Expected check: the Docker image builds (the repo has CI checks for the simulator build and the Docker image), and the benchmark scripts run binary/ternary inference through the crossbar simulator.
- Honest note: not run end to end here. `src/main.py --help` fails immediately here with `ModuleNotFoundError: No module named 'tvm'`, because the documented route is Docker, not a bare `python src/main.py`, and Docker is not installed in this VM. The simulator build was not attempted outside Docker, to stay on the documented route. On a machine with Docker, the README's build-then-benchmark flow is the reproducible path.

## Code source

- Upstream code is at the repository link above; `code/CODE.md` in this folder gives the completeness checklist and minimal reproduction commands.
- **`code/reproduce.py` in this folder is an original reproduction skeleton using only the Python standard library, for understanding the core idea. It is not upstream code, and it is not the original hardware/simulator, and it cannot directly reproduce the original paper's numbers.**

