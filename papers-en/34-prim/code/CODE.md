# Code sources and reproduction notes: PrIM

- Link: https://github.com/CMU-SAFARI/prim-benchmarks
- Nature: official open-source benchmark suite, not a third-party implementation.
- Licence: MIT (`LICENSE`, SAFARI Research Group, ETH Zürich, 2021).

## Completeness checklist

- [x] Real code, not just a PDF: 16 benchmark directories (BFS, BS, GEMV, HST-L, HST-S, MLP, NW, RED, SCAN-RSS, SCAN-SSA, SEL, SpMV, TRNS, TS, UNI, VA) + `Microbenchmarks/`, each benchmark with host + DPU + support code
- [x] Installation/run instructions: README (citation, benchmark list) + each benchmark's Makefile and README
- [x] Examples: each benchmark is itself a runnable example; the `run_*.py` scripts run the scalability studies
- [x] Tests/baselines: each benchmark's `baselines/cpu` and `baselines/gpu`
- [ ] Hardware requirements for full results: UPMEM PIM DIMMs + UPMEM SDK (the DPU Makefile needs `dpu-pkg-config` and `dpu-upmem-dpurte-clang`). The CPU baseline needs only GCC + OpenMP.

## Minimal upstream reproduction steps (CPU baseline, actually run)

```bash
git clone https://github.com/CMU-SAFARI/prim-benchmarks
cd prim-benchmarks/VA/baselines/cpu
make
./va -t 8 -w 1 -e 3 -i 16777216
```

Actual output here (standard CPU, no UPMEM):

```
nr_elements	16777216	Kernel Time (ms): 59.957000
```

This is the vector-addition (VA) benchmark's CPU baseline, not a DPU result.

## Full DPU reproduction (requires UPMEM hardware)

```bash
# For example, in VA/, with the UPMEM SDK installed:
make NR_DPUS=1 NR_TASKLETS=16 BL=10 TYPE=INT32
./bin/host_code
```

Expected check: the host code loads the DPU binary, runs the workload on the DPUs and reports kernel time. Not run here — this VM has no UPMEM hardware or SDK.

## Skeleton in this directory

`reproduce.py` is an original standard-library skeleton demonstrating partitioning a vector across DPUs, unrelated to the upstream code.
