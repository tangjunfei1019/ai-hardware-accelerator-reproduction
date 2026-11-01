# MTIA 300: Meta's First Training Chip Featuring Built-in NICs and Collective Offloading Engines

## Original paper information

- Original title: MTIA 300: Meta's First Training Chip Featuring Built-in NICs and Collective Offloading Engines
- Authors: MTIA Team (Meta Platforms)
- Year and venue: 2026, ISCA 2026; a Meta engineering blog post also accompanies it (August 2026)

## Core method

- Networking inside the package: two network chiplets, each with 6 custom 800 Gbps RDMA NICs, for 12 NICs total and about 1.2 TB/s of aggregate I/O, removing the PCIe bottleneck.
- Communication offloading: 16 dedicated message engines execute collective communication without occupying the compute grid; communication changes from "handled on the side by general compute cores" to "a first-class citizen".
- Designed for recommendation training: the chip is built for ranking / recommendation training, with 72 processing units and 216 GB of HBM3E; the compute die is 3 nm and the I/O die is 5 nm.
- Hardware-software co-design: co-designed from scratch with the in-house communication library HCCL, so the same NICs can be flexibly partitioned between scale-up (within a rack) and scale-out (across racks) use.

## Core results

- As reported in the paper and Meta materials (see the original): on a 40-accelerator, 150-billion-parameter production recommendation model, total communication time is about 3.9x faster than a comparable GPU cluster; when collective communication runs in parallel with large matrix multiplication, compute performance drops by less than 0.5%.
- Significance: one of the 2026 dividing lines for industry accelerators — the bottleneck shifts from single-card compute to cluster communication, and MTIA 300 writes "communication architecture" into the chip definition itself.

## Reproduction points

- Reproduction goal: simulate the two modes — "compute cores also doing communication" versus "dedicated message engines offloading communication" — and compare total time and compute slowdown when communication overlaps compute.
- Measure: communication time share, overlap rate, and compute throughput drop before and after offloading.
- What will not match the original chip: real chiplet interconnect, the RDMA protocol, HCCL collective algorithms, and production cluster scale; the skeleton only verifies the offloading-and-overlap gain model.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
