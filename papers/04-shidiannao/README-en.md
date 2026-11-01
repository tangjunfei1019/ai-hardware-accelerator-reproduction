# ShiDianNao: Shifting Vision Processing Closer to the Sensor

## Original paper information

- Original title: ShiDianNao: Shifting Vision Processing Closer to the Sensor
- Authors: Zidong Du, Robert Fasthuber, Tianshi Chen, et al.
- Year and venue: 2015, ISCA 2015

## Core method

- Core idea: do not first move the whole image to memory and then compute; instead connect the accelerator directly beside the vision sensor, so data enters the compute pipeline as soon as it leaves the sensor, bypassing off-chip memory.
- It fits small-model vision tasks: when the whole CNN's parameters fit in on-chip SRAM, off-chip DRAM accesses can be greatly reduced; for such tasks, the sensor-direct benefit is largest.
- Architecturally it still follows the DianNao family's NFU and buffer ideas, but the data path's starting point changes from "memory" to "sensor", and the memory hierarchy is simplified accordingly.
- Design trade-off: sacrifice generality in exchange for extremely low power and small area for embedded vision.

## Core results

- As relayed in survey literature: ShiDianNao's energy-efficiency improvement over DianNao can reach on the order of 60x (for specific vision tasks and comparison conditions; see the original paper for the exact basis).
- The applicability boundary is critical: when the model grows and no longer fits in on-chip storage, the sensor-direct benefit drops rapidly; this paper's conclusion cannot be generalized directly to large models.
- On area, a public survey table gives on the order of 4.86 mm² (65 nm); see the original paper for the exact figure.

## Reproduction points

- Reproduction goal: compare two data paths — "sensor → DRAM → accelerator" versus "sensor → accelerator directly" — for memory accesses and latency on small models.
- Measure: DRAM access volume, end-to-end latency, and on-chip SRAM capacity required as model size varies.
- What will not match the original chip: real sensor-interface timing, analog/digital-boundary power, and chip area.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
