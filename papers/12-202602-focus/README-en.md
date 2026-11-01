# Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models

## Original paper information

- Original title: Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models
- Authors: Chiyue Wei, Cong Guo, Junyao Zhang, Haoxuan Shan, Yifan Xu, Ziyue Zhang, Yudong Liu, Qinsi Wang, Changchun Zhou, Hai Li, Yiran Chen
- Year and venue: 2026, HPCA 2026; arXiv:2512.14661, DOI: 10.1109/HPCA68181.2026.11408525; HPCA 2026 Best Paper Nominee / Candidate

## Core method

- Problem: vision-language models have large numbers of highly redundant visual tokens, and feeding all tokens into the large model wastes both compute and memory traffic.
- Multi-level streaming concentration: as a composable module in a systolic-array accelerator, it cuts redundancy in three stages — semantic-guided token pruning, spatiotemporal block-level concentration, and motion-aware matching-based vector-level redundancy removal.
- Streaming rather than offline: concentration is combined with the compute pipeline, avoiding the extra memory traffic of storing all tokens first and filtering afterwards.

## Core results

- As reported in the paper abstract (see the original): about 2.4x speedup and about 3.3x energy reduction; the conclusion's breakdown figures are up to about 2.35x speedup and about 3.29x energy-efficiency improvement, with about 2.7% area overhead.
- Significance: in 2026, the bottleneck of multimodal inference expanded from "the language model itself" to "the flood of visual tokens" — Focus puts token compression into the accelerator datapath instead of leaving it at the algorithm layer only.

## Reproduction points

- Reproduction goal: simulate the three-stage filtering — prune by semantic score, aggregate by block, deduplicate by similarity — and count the token reduction rate and the approximate amount of retained information.
- Measure: token counts after each stage, the relationship between pruning threshold and reduction rate, and the effect of deduplication on subsequent compute.
- What will not match the original chip: the true source of semantic scores (vision encoder outputs), the hardware implementation of motion-aware matching, and systolic-array timing and area/power; the skeleton only verifies the filtering logic and the reduction amounts.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
