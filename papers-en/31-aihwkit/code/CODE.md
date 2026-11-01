# Code sources and reproduction notes: AIHWKit

- Link: https://github.com/IBM/aihwkit
- Nature: official open-source toolkit, not a third-party implementation.
- Licence: MIT (`LICENSE.txt`); before use, follow the licence shipped with the repository.

## Completeness checklist

- [x] Real code, not just a PDF: Python + C++/CUDA simulator (`src/`), PyTorch integration
- [x] Installation/run instructions: README + documentation at https://aihwkit.readthedocs.io
- [x] Examples: `examples/` (30 numbered examples, such as `01_simple_layer.py`, LeNet-5, ResNet, BERT examples) and `notebooks/` tutorials
- [x] Tests: `tests/` (30 test files counted in the clone)
- [x] Hardware requirements: standard CPU works; GPU/CUDA optional, used only when available

## Minimal upstream reproduction steps

```bash
pip install aihwkit
git clone https://github.com/IBM/aihwkit
cd aihwkit
python examples/01_simple_layer.py
```

Expected check: the script builds a one-layer analog network (`AnalogLinear(4, 2)`, constant-step device), trains it to sum its inputs, and prints the training process. No GPU is needed.

## Parts that cannot be reproduced from this entry alone

- The full PCM device statistical model calibration, GPU-accelerated simulator performance, and the paper's per-experiment accuracy tables require running the full examples on a machine with PyTorch, following the paper and upstream documentation.
- The reason the upstream example was not run end-to-end here: this VM has no PyTorch, and the CPU PyTorch download timed out repeatedly; this is an environment limitation, not a repository defect.

## Skeleton in this directory

`reproduce.py` is an original standard-library skeleton demonstrating matrix-vector multiplication on an analog tile + noise + ADC quantization, unrelated to the upstream code.
