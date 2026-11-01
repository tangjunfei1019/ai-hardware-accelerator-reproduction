# Efficient Processing of Deep Neural Networks: A Tutorial and Survey

## Original paper information

- Original title: Efficient Processing of Deep Neural Networks: A Tutorial and Survey
- Authors: Vivienne Sze, Yu-Hsin Chen, Tien-Ju Yang, Joel Emer
- Year and venue: 2017, Proceedings of the IEEE

## Core method

- Core argument: the first bottleneck in accelerating deep neural networks is not compute power, but data movement. Moving weights, activations, and partial sums between off-chip DRAM, on-chip global buffers, and PE-local register files accounts for most of the system's energy.
- The method framework has three layers: (1) network level: pruning, quantization, low-rank methods, and compact network structures; (2) hardware level: spatial architectures, specialized dataflows, and on-chip memory hierarchies; (3) algorithm-hardware co-design: approximation and sparsity only where the accuracy loss is controllable.
- Dataflow is the key design variable: weight-stationary, output-stationary, row-stationary, and other dataflows determine how many times the same layer is reused and how many memory accesses it makes on the same PE array. Evaluation must consider throughput, energy efficiency, area, and accuracy together, not TOPS/W alone.
- It proposes an evaluation discipline: distinguish peak compute from actual utilization, distinguish training from inference, and distinguish results under different processes, voltages, and sparsity levels; otherwise cross-paper comparisons are meaningless.

## Core results

- This paper is a tutorial and survey, so it does not present a single chip and therefore has no single "chip metric of this paper". Its value is a unified analysis framework and comparison method.
- Representative examples cited in the paper include the Eyeriss chip: about 34.7 fps and about 278 mW on AlexNet convolutional layers, reported by its authors as roughly an order of magnitude more energy-efficient than a contemporary mobile GPU (see the Eyeriss paper itself for the exact figures).
- When reproducing, do not take numbers cited in the survey as this paper's own measured results; check each original paper's experimental conditions one by one.

## Reproduction points

- Reproduction goal: for a given convolutional layer, estimate memory accesses and energy under weight-stationary, output-stationary, and row-stationary dataflows, and verify the core conclusion that "changing the dataflow changes energy".
- Measure: DRAM accesses, global-buffer accesses, PE-local accesses, and MAC utilization under each dataflow.
- What will not match the original chips: without process libraries and real chip area and power models, this skeleton can only make relative comparisons, not reproduce absolute power numbers.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
