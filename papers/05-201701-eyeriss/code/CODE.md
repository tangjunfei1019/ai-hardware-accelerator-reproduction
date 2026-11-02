## Code sources

- Status: **Third-party RTL, verified to exist, but not an MIT official release**. Do not label it as the original authors' official code.
- Third-party repositories verified to exist (verified by reading GitHub content):
  - https://github.com/abdelrahmanmedhatt/Eyeriss (contains GLB/HMNOC/PE Verilog files)
  - https://github.com/arasi15/CNN-Accelerator-Implementation-based-on-Eyerissv2 (contains an RTL directory and README)
- Before use, read each repository's own license and README; third-party implementations may differ from the original chip in functionality, timing, and precision, so reproduction conclusions should be based on your own tests.
- Additional modeling route: Timeloop/Accelergy (see the links in the Sze section) can be used for dataflow-level modeling and comparison.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, using only the Python standard library, demonstrating row-stationary dataflow's row-level reuse accounting. It is not the original paper code, and not a copy of the third-party code above.

## Unified run evidence

- Unified run evidence: [unified/](../../unified/) — SCALE-Sim v3 Run B (Eyeriss-like 12x14, weight-stationary): total 249,102 cycles, overall utilisation 40.15%, mapping efficiency 97.96%. Framework estimate only, not the Eyeriss paper result and not silicon measurement.
