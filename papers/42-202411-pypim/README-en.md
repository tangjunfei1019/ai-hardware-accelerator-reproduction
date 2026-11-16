# PyPIM: Integrating Digital Processing-in-Memory from Microarchitectural Design to Python Tensors

## Original paper information

- Original title: PyPIM: Integrating Digital Processing-in-Memory from Microarchitectural Design to Python Tensors
- Authors: Orian Leitersdorf, Ronny Ronen, Shahar Kvatinsky
- Year and venue: MICRO 2024 (2024-11-02)
- arXiv / DOI: arXiv:2308.14007; DOI 10.1109/MICRO61859.2024.00119

## Core method

- An end-to-end integration of digital memristive processing-in-memory (PIM), from a high-level Python tensor library down to the microarchitectural design: a microarchitecture and instruction set architecture (ISA) bridge the gap between the low-level control periphery and an abstraction of PIM parallelism; a development library converts high-level Python to ISA instructions; and a driver translates ISA instructions into PIM micro-operations.
- The microarchitecture supports parallel bitwise operations inside the memory array, including the partitions and operations across both directions of the array that are specific to memristive PIM.
- The Python library offers tensor operations similar to NumPy / PyTorch, so users can write tensor programs directly or assemble new PIM routines from existing arithmetic functions; the repository has four parts: a GPU-accelerated simulator, the microarchitectural driver, the development library, and test scripts that serve as benchmarks.
- Evaluation uses a cycle-accurate simulator on a wide variety of benchmarks, checking the versatility of the Python library and performance against theoretical PIM bounds.

## Core results

- As reported in the paper (see the original): PyPIM drastically simplifies the development of PIM applications and lets existing tensor-oriented Python programs convert to PIM with ease; specific benchmark numbers follow the paper's tables, and this directory does not treat skeleton operation counts as paper results.
- The upstream minimal example: after `pip install -e .`, running `python main.py` should output `32.0`.
- Peak performance: no comparable peak number is given (evaluation against theoretical PIM bounds is not a peak).

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (tensor operation results match expectations) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers. PyPIM itself is a simulation tool, and its outputs are simulator estimates, not silicon measurements; the full simulation backend needs CUDA 12.0 and a GPU with at least 8 GB of VRAM, so it cannot run a full simulation on this CPU-only machine; and no LICENSE file was found in the upstream repository root, so check the repository's own files before use.
