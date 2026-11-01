# LoCaLUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM

## Original paper information

- Original title: LoCaLUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM
- Authors: Junguk Hong, Changmin Shin, Sukjin Kim, Si Ung Noh, Taehee Kwon, Seongyeon Park, Hanjun Kim, Youngsok Kim, Jinho Lee (Seoul National University, and others)
- Year and venue: 2026, HPCA 2026; arXiv:2604.04523; HPCA 2026 Best Paper Candidate. Note: some sources abbreviate the title as LOCALUT; the paper title LoCaLUT is authoritative.

## Core method

- Lookup-table inference: multiple multiply-accumulate operations are packed into one table lookup (LUT lookup), trading compute for capacity by replacing multiplication with lookup.
- LUT canonicalization: removes duplicate table entries to compress lookup-table size; combined with reordered LUTs, it further reduces redundancy.
- LUT slice streaming: uses the DRAM cache hierarchy for slice streaming, matching the lookup dataflow to the DRAM-PIM memory structure.
- Real-system validation: evaluated on a real UPMEM-based system, not pure simulation.

## Core results

- As reported in the paper (see the original): about 1.82x geometric-mean speedup across different numerical precisions and DNN models.
- Significance: a key 2026 advance on the PIM route — it does not assume a future DRAM process, but confronts the "lookup saves compute yet costs capacity" trade-off head-on, and proves on real PIM hardware that this route works.

## Reproduction points

- Reproduction goal: simulate lookup packing — several small multiply-accumulates completed with one lookup — and count lookup-table size, entry counts before and after deduplication, and compute volume.
- Measure: the relationship between packing granularity and entry count, the canonicalization deduplication rate, and the lookup-to-multiplication count ratio.
- What will not match the original system: the real UPMEM programming model, the DRAM cache hierarchy, and lookup hardware; the skeleton only verifies lookup equivalence and deduplication logic.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not commercial DRAM RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
