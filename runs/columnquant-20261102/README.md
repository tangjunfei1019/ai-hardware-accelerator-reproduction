# Run evidence: ColumnQuant (paper 35) — 2026-11-02

Upstream: https://github.com/jiyoonkm/ColumnQuant (not Junfei's code, not redistributed here).
This folder records one minimal upstream run only. See paper 35 in `papers/35-202503-columnquant/`.

## Command

```bash
# upstream cloned separately to ~/workspace/columnquant-upstream/ (HEAD 6f9784e)
# environment: ~/workspace/aihwkit-venv/, torch 2.15.0+cpu
~/workspace/aihwkit-venv/bin/python - << 'EOF'
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

## Result

- Module built in 0.12 s.
- Input `(1, 64, 32, 32)` → output `(1, 64, 32, 32)`, total ~1.3 s, exit 0.
- Full log: `columnquant-forward.log` in this folder.

## Caveat

This proves the upstream `SplitConv4Pim_group` module builds and runs a forward pass here.
It does **not** reproduce any DATE 2025 accuracy table — that would need the full training
flow and checkpoints. No licence file was found in the upstream repo root; check the
authors' licence terms before redistributing or building a product on it.
