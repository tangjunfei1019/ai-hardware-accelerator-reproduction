# Code sources and reproduction notes: ColumnQuant / RUnQuant

- Link: https://github.com/jiyoonkm/ColumnQuant
- Nature: official open-source framework, not a third-party implementation.
- Licence: no licence file was found in the repository root; check the authors' / paper's licence terms before redistributing or building a product on it.

## Completeness checklist

- [x] Real code, not just a PDF: `SplitConv4Pim_group.py` (CIM convolution framework), `LSQ.py` (learned step-size quantization), `any_quant.py`, plus the `legacy/` directory
- [x] Additional entry files in the full clone (listed by filename only; contents not checked item by item here, so check them before an end-to-end reproduction): `main.py`, `resnet_quan.py`, `utils.py`
- [x] Checkpoint: the ResNet-20 CIFAR-100 W3A3P3 checkpoint in `legacy/` (`ResNet20_Cifar100_W3A3P3_ckpt.pth`)
- [x] Installation/run instructions: the README gives the API, parameters and usage examples; but there is no separate `requirements.txt` or install script in the root, so dependencies (PyTorch etc.) must be configured by the user
- [x] Examples: the README usage example is the entry example; there is no separate `examples/` directory
- [ ] Licence: no licence file found in the root
- [x] Hardware requirements: the framework itself runs on a standard CPU + PyTorch; GPU is recommended for training larger models; running the quantization framework needs no CIM hardware (it models CIM constraints in software)

## Minimal upstream reproduction steps (README example)

```bash
git clone https://github.com/jiyoonkm/ColumnQuant
cd ColumnQuant
python3 - << 'EOF'
import torch
from SplitConv4Pim_group import SplitConv4Pim_group

conv = SplitConv4Pim_group(
    w_bit=3, split_bit=1, w_mode='Array',
    ps_bit=3, num_sigma=6, psum_mode='Array',
    in_planes=64, planes=64, kernel_size=3,
    N=256, stride=1, padding=1,
)
x = torch.randn(1, 64, 32, 32)
y = conv(x)
print(y.shape)
EOF
```

Expected check: the module builds without error and the forward pass returns the expected output shape for a 64-channel, 3x3 convolution on a 32x32 input (the exact output shape depends on the framework's splitting, so check it against the README's parameter documentation on a first run).

## Parts that cannot be reproduced from this entry alone

- The full PyTorch training flow and the paper's accuracy tables require a machine with PyTorch installed plus the checkpoint/training scripts; the skeleton only demonstrates column-granularity quantization.
- The reason the upstream code was not run end-to-end here: this VM has no PyTorch and the CPU PyTorch download timed out repeatedly; syntax checks passed (`SplitConv4Pim_group.py`, `LSQ.py` and `any_quant.py` all passed `python3 -m py_compile`).

## Skeleton in this directory

`reproduce.py` is an original standard-library skeleton demonstrating column-granularity quantization and dequantization, unrelated to the upstream code.

## Run evidence (real upstream run, 2026-11-02)

- Evidence folder: [runs/columnquant-20261102/](../../runs/columnquant-20261102/) — command, log and result for the `SplitConv4Pim_group` forward pass (input (1, 64, 32, 32) → output (1, 64, 32, 32), ~1.3 s, CPU).
- Caveat: this proves the module builds and runs; it does not reproduce any DATE 2025 accuracy table. No licence file was found in the upstream repo root.
