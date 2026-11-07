# XBTorch: A Unified Framework for Modeling and Co-Design of Crossbar-Based Deep Learning Accelerators

## Original paper information

- Original title: XBTorch: A Unified Framework for Modeling and Co-Design of Crossbar-Based Deep Learning Accelerators
- Authors: Osama Yousuf, Andreu L. Glasmann, Martin Lueker-Boden, Sina Najmaei, Gina C. Adam
- Year and venue: APL Machine Learning, 2026
- arXiv / DOI: arXiv:2601.07086

## Core method

- On top of PyTorch, uniformly models crossbar arrays: weights mapped to conductances, device variation and noise injection, quantization and gradient decomposition; a stateful mode does layer-wise mapping and inference, while a stateless mode streams LLM parameters, avoiding persistent crossbar instances for all parameters.

## Core results

- As reported in the paper (see the original): the framework is comparable with existing tools in device modeling, hardware-aware training, and inference fault tolerance, and can handle large models in stateless LLM evaluation; specific accuracy and speedup numbers follow the paper's tables, and this directory does not treat skeleton output as paper numbers.

## Reproduction points

- Reproduction goal: first run the upstream repository's minimal example to confirm the core mechanism works; then run the paper configuration and compare against the paper's baselines and method description.
- Measure: correctness (round-trip / accuracy / output trends) and trends under key configuration changes, not a single speedup number.
- What will not match the original: process, device parameters, simulator versions, and baseline configurations all change absolute numbers; the skeleton only demonstrates the idea.

## Run evidence

- The upstream minimal example was actually run (2026-11-04): the README's two-layer perceptron `SimpleMLP(10, 5, 2)`, patched with `xbtorch_model`, completed one forward pass in ~12 s, input (4, 10) → output (4, 2). Evidence: [runs/xbtorch-20261104/](../../runs/xbtorch-20261104/). This proves only that the upstream module builds, patches a model and runs one forward pass, not any APL Machine Learning 2026 accuracy table.

## Code sources

See [`code/CODE.md`](code/CODE.md), and the reproduction skeleton in this directory, [`code/reproduce.py`](code/reproduce.py).

> Note: the `reproduce.py` in this directory is an original reproduction skeleton, not the original authors' code. It is only for understanding the core ideas, and cannot directly reproduce the original area, power, or clock numbers.
