# Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks

## Original paper information

- Original title: Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks
- Authors: Yu-Hsin Chen, Tushar Krishna, Joel Emer, Vivienne Sze
- Year and venue: 2017, IEEE Journal of Solid-State Circuits (ISSCC special issue)

## Core method

- Spatial architecture: 168 PEs arranged in an array, each PE with its own register file, multiply-accumulate unit, and control; a global buffer (GLB) distributes data from the center, and off-chip DRAM sits at the outermost level, forming a four-level memory hierarchy.
- Row-stationary (RS) dataflow: one row of a convolution is kept in a PE register file for reuse, and weights, activations, and partial sums flow through the array by multicast, maximizing reuse of all three data types and reducing DRAM and GLB accesses.
- Reconfigurable multicast on-chip network (NoC): data distribution is reconfigured according to different convolutional layer shapes (filter size, channel count), avoiding low utilization when a fixed dataflow meets certain layers.
- Sparsity and gating: data gating and compression for zero activations further save power and bandwidth; the chip was integrated with the Caffe framework and can run real networks directly.

## Core results

- Chip measurement highlights reported in the paper (see the original paper for the exact figures): a 168-PE array, 65 nm process; about 35 fps and about 278 mW on AlexNet convolutional layers, reported by the authors as roughly 10x more energy-efficient than a contemporary mobile GPU.
- The RS dataflow's energy-efficiency advantage over other dataflows is on the order of 1.4x to 2.5x (varying with layer shape), which is the key number for understanding "dataflow is architecture".
- Eyeriss v2 (2019, follow-up work) further targets compact and sparse networks, introducing a hierarchical mesh NoC and RS+ dataflow, but this summary is based on the 2017 Eyeriss paper.

## Reproduction points

- Reproduction goal: for one convolutional layer, implement memory-access accounting under weight-stationary, output-stationary, and row-stationary dataflows, and verify row-stationary's advantage on most layers and its disadvantage on individual layers.
- Measure: DRAM/GLB/RF access volumes, PE utilization, and how the dataflow ranking changes with different filter sizes and channel counts.
- What will not match the original chip: real NoC congestion, clock, 65 nm power and area; the skeleton only makes relative comparisons at the dataflow level.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
