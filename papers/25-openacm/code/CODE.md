# Code sources and reproduction notes: OpenACM: An Open-Source SRAM-Based Approximate CiM Compiler

## Reproducibility grade: B

- A = upstream code runs on a standard machine / simulator.
- B = upstream code runs, but needs special hardware or a specific toolchain.
- This paper's grade: **B**.

## Upstream repository (verified to exist)

- Link: https://github.com/ShenShan123/OpenACM
- Repository contents: Python compiler front end, multiplier / SRAM / PE generators, RTL templates, OpenROAD flow scripts, docs/, examples/ (note: the repository has since evolved into OpenACMv2 — for reproducing v1, check the repository history and documentation)
- Hardware / software requirements: a standard CPU can run the front end; the full physical design flow needs OpenROAD and FreePDK45, see the upstream documentation
- License: follow the license file shipped with the repository; read it before use.

## Reproduction steps

1) git clone https://github.com/ShenShan123/OpenACM
2) Install Python dependencies per the repository documentation, then run a front-end example first to confirm it generates architectures and multiplier configurations
3) Then run the OpenROAD + FreePDK45 flow per the documentation (install that toolchain first)
4) Compare against the paper: exact versus approximate configurations under the same accuracy constraint, in terms of energy
Expected check: front-end examples should output configurations and estimates; the full flow should output post-layout area / power estimates.

## What cannot be reproduced from the paper alone

- Post-layout power cannot be reproduced from front-end output alone; the current v2 repository state must not be equated directly with all of the v1 paper's experiments; process libraries and OpenROAD versions affect results.

## Skeleton in this directory

- `reproduce.py` is an original Python standard-library skeleton demonstrating the core idea, not upstream code, and not RTL / chip measurements.
- The skeleton alone does not satisfy this paper's reproducibility requirement; reproducibility is provided by the upstream steps above.
