# Run evidence: OpenACM (paper 25) — 2026-11-05

Upstream: https://github.com/ShenShan123/OpenACM (HEAD 92813c9, Apache-2.0; not this repository's code, not redistributed here).
This folder records one real upstream run only. See paper 25 in `papers/25-202604-openacm/`.

## Command

```bash
# upstream cloned separately to ~/workspace/openacm-upstream/ (HEAD 92813c9, 744 MB)
# environment: system Python 3.12.3, standard library only
# the v2 requirements.txt is heavy (torch 2.8.0+cu128, torch-geometric, botorch,
# smac, openram, PySpice) but was NOT installed — both minimal generators import
# only stdlib modules (argparse, pathlib, re, math, datetime)
cd ~/workspace/openacm-upstream
python3 openacm/multiplier_compiler/multiplier_compiler.py --bit_width 8
python3 openacm/pe_compiler/SRAM.py --data_width 8 --addr_count 16 --rtl_dir ./DCIM/rtl
```

## Result

- Multiplier step, exit 0, instant: generated `DCIM/multiplier/Exact_8bit.v`,
  `Appro4_2_8bit.v` and `Log_our_8bit.v` (git status confirms only these three
  8-bit files changed; the 16/32-bit files were already in the clone).
- SRAM step (8-bit / 16-deep), exit 0, instant, but produced no observable
  change: the shipped `DCIM/rtl/sram.v` already is the 16x8 module (hardcoded
  `[7:0]` data / `[3:0]` address, no parameter lines for the script's regexes
  to replace), so the 8x16 example was already at the requested parameters.
- Full log: `openacm-forward.log` in this folder.

## Caveat

This proves only that the current v2 front end can generate 8-bit multiplier RTL here.
It does **not** reproduce any DATE 2026 paper numbers, and it is not a silicon
measurement. The PE and backend flow (OpenROAD / OpenSTA / FreePDK45 / OpenYield /
Xyce) were not attempted; the upstream README is now titled OpenACMv2 while the
repository description still calls it the DATE 2026 paper's initial version, so
v1/v2 drift remains.
