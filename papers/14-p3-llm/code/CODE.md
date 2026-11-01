## Code sources

- Status: **Official open-source quantization code, but the PIM hardware RTL is not open source**. Do not label the quantization code repository as PIM RTL.
- Quantization code link given in the paper: https://github.com/yc2367/P3-LLM
- Read the license and README shipped with the repository before use; this directory does not copy any code from that repository.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, Python standard library only, demonstrating per-operand bit-width allocation for hybrid-precision quantization and memory-traffic estimation for the prefill / decoding division of labor.
