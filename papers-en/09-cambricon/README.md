# Cambricon: An Instruction Set Architecture for Neural Networks

## Original paper information

- Original title: Cambricon: An Instruction Set Architecture for Neural Networks
- Authors: Shaoli Liu, Zidong Du, Jinhua Tao, et al.
- Year and venue: 2016, ISCA 2016

## Core method

- Problem framing: general-purpose ISAs (x86, MIPS, GPGPU) pay too much flexibility overhead for neural networks, while fixed-function accelerators can only cover a few networks; Cambricon seeks a domain-specific middle ground between the two.
- Instruction set design: a load-store architecture integrating scalar, vector, matrix, logic, data-movement, and control instructions; based on a commonality analysis of many neural network algorithms, it extracts shared compute primitives, rather than building hardware for each network separately.
- Coverage is the core evaluation criterion: the same instruction set must express convolution, pooling, fully-connected, normalization, and other operators, with higher code density than general-purpose ISAs, while keeping hardware overhead controllable relative to a specialized accelerator.
- Later work such as Cambricon-X (sparse) and Cambricon-S (software/hardware co-design for irregular sparsity) extends this ISA idea, but this summary is based on the 2016 ISA paper.

## Core results

- Results reported in the paper (see the original paper for the exact figures): on 10 representative and distinct neural network algorithms, Cambricon shows strong expressiveness, with higher code density than general-purpose ISAs such as x86, MIPS, and GPGPU.
- Compared with the then state-of-the-art DaDianNao (which could only cover 3 neural network algorithms), a Cambricon-based prototype in TSMC 65 nm incurred only negligible latency/power/area overhead, while expanding coverage to 10 benchmarks.
- The key conclusion is not a single speed number, but the "generality + efficiency" trade-off: a domain-specific ISA can significantly expand an accelerator's applicability without sacrificing much efficiency.

## Reproduction points

- Reproduction goal: design a tiny domain-specific instruction interpreter supporting vector/matrix primitives, and verify that the same instruction set can express convolution, fully-connected, pooling, and other operators.
- Measure: the number of instructions needed to express different operators (code-density comparison), the kinds of operators covered by the instructions, and the MAC count executed by the interpreter.
- What will not match the original chip: real instruction encodings, pipelines, hardware area and power; the skeleton only verifies expressiveness at the ISA level.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code, and not chip RTL. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
