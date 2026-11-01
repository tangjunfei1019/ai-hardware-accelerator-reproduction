# AHASD: Asynchronous Heterogeneous Architecture for LLM Adaptive Drafting Speculative Decoding on Mobile Devices

## Original paper information

- Original title: AHASD: Asynchronous Heterogeneous Architecture for LLM Adaptive Drafting Speculative Decoding on Mobile Devices
- Authors: Ma Zirui, Fan Zhihua, Li Wenxing, Wu Haibin, Zhang Fulin, Ye Xiaochun, Li Wenming
- Year and venue: arXiv 2026
- arXiv / DOI: arXiv:2604.25326

## Core method

- Splits speculative decoding into task-level asynchronous execution: a small draft model drafts on PIM, a large target model batch-verifies on a single NPU; entropy-history-aware draft control and time-aware pre-verification control suppress low-confidence invalid drafts; LPDDR5-PIM includes in-memory attention algorithm units and gated task scheduling units, enabling attention localization and sub-microsecond task switching.

## Core results

- As reported in the paper (see the original): versus a GPU baseline, up to about 4.2x throughput and about 5.6x energy efficiency; versus a GPU+PIM baseline, about 1.5x throughput and about 1.24x energy efficiency; hardware overhead below 3% of DRAM area.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
