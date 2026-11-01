## Code sources

- Status: **Official open-source code (link given in the paper), but whether it contains synthesizable RTL was not verified item by item in this check — judge by the repository contents, and do not assume it is RTL**.
- Link given in the paper: https://github.com/dbw6/Eva.git
- Read the license and README shipped with the repository before use; this directory does not copy any code from that repository.

## Skeleton in this directory

- `reproduce.py`: original reproduction skeleton, Python standard library only, demonstrating input x codebook dot products followed by index-based summation, equivalent to dequantize-then-multiply-accumulate.
