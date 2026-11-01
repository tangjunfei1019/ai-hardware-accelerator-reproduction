# Code sources and reproduction notes: DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures

## Reproducibility grade: B

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **B**.

## Upstream repository (verified to exist)

- Link: https://github.com/SPIN-Research-Group/DCC
- Repository contents: C++ compiler source, setup.sh, run_experiments.sh, src/, with data layout and scheduling for multiple backends including UPMEM / HBM-PIM / AttAcc
- Hardware / software requirements: a standard CPU can run the compiler front end; fully reproducing the paper's numbers needs an AttAcc / HBM-PIM backend simulator — see the upstream setup.sh and README
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/SPIN-Research-Group/DCC
2) Install dependencies per the repository README / setup.sh and read the backend notes
3) First run the repository's built-in small example to confirm the compiler can generate target-backend code
4) Then run the paper experiment scripts via run_experiments.sh and compare against the baselines in the paper's tables
Expected check: the small example should generate code normally and output a performance prediction; full backend numbers are only comparable in the corresponding PIM backend simulation environment.

## What cannot be reproduced from the paper alone

- Absolute HBM-PIM / AttAcc speedups cannot be reproduced on an ordinary CPU alone; compiler run time on a CPU must not be mistaken for PIM execution time; the upstream repository's license is as shipped in the repository.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
