# PrIM: The First Benchmark Suite for a Real Processing-in-Memory System

## Original paper information

- Original title: Benchmarking a New Paradigm: Experimental Analysis and Characterization of a Real Processing-in-Memory System
- Authors: Juan Gómez-Luna, Izzat El Hajj, Ivan Fernandez, Christina Giannoula, Geraldo F. Oliveira, Onur Mutlu
- Year and venue: 2022, IEEE Access (DOI: 10.1109/ACCESS.2022.3174101); arXiv:2105.03814
- Upstream repository: https://github.com/CMU-SAFARI/prim-benchmarks

## Core method

- First characterise the UPMEM system with microbenchmarks (a general-purpose in-order core, called a DPU, beside each DRAM bank) for compute throughput and memory bandwidth, then run PrIM's 16 workloads on real UPMEM systems (640 and 2556 DPUs in the paper) and compare against CPU/GPU baselines.
- Each benchmark contains host code, DPU code (`dpu/task.c`), support code and CPU/GPU baselines, and the repository root also has the `run_strong_full.py`, `run_strong_rank.py` and `run_weak.py` scaling scripts.
- The paper's conclusions are programming recommendations (which workloads suit PIM, how to partition across DPUs), rather than a single accelerator design.

## Core results

- Impact: PrIM was the first benchmark suite for the first publicly available real PIM hardware (UPMEM), and became the yardstick later PIM papers compare against — 16 workloads covering linear algebra, databases, graph processing, neural networks, bioinformatics and image processing, plus architectural-limit microbenchmarks.
- The paper's results are per-workload scalability and performance/energy comparison tables on two real UPMEM systems, in the IEEE Access paper; no single speedup is quoted here as a headline, because PrIM is a benchmark suite, not a single kernel.

## Reproduction points

- Reproduction goal: first run the CPU baseline to understand the benchmark, then understand DPU partitioning: split a vector by the number of DPUs, compute one slice per DPU, and reduce at the end.
- What to measure: baseline time trends at different element counts and partition counts.
- What will not match the original tool: real DPU kernel times and energy, and scalability curves; the skeleton only demonstrates the partitioning idea, and the CPU baseline result is in CODE.md.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas and cannot directly reproduce the paper's DPU performance numbers.

## Verification notes for this entry

- The upstream repository was verified to exist via `git ls-remote`; it contains 16 benchmark directories and microbenchmarks, each benchmark with host + DPU + support code.
- The CPU baseline was actually run: `VA/baselines/cpu` was compiled with `gcc -fopenmp` and run, outputting `nr_elements 16777216, Kernel Time (ms): 59.957000`. This is a CPU baseline, not a DPU result.
- Full DPU results were not run, because this VM has no UPMEM hardware or SDK.
