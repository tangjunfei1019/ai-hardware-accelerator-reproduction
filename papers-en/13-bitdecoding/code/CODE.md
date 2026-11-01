## Code sources

- Status: **Official open-source GPU system code (CUDA / tensor-core implementation), not accelerator RTL**. Do not label it as RTL.
- Link given in paper v3: https://github.com/OpenBitSys/BitDecoding
- Note: an earlier version of the paper gave a different personal repository link from one of the authors; the latest v3 link above is authoritative — follow the repository README, and read its license. This directory does not copy any code from that repository.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, Python standard library only, demonstrating 4-bit KV quantization/dequantization and attention-score computation, and the effect of bit-width on cache byte counts.
