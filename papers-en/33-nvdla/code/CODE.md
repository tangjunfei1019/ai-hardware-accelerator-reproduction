# Code sources and reproduction notes: NVDLA

- Link: https://github.com/nvdla/hw
- Nature: official open-source RTL, not a third-party implementation.
- Licence: NVIDIA Open NVDLA License and Agreement v1.0 (`LICENSE` — read it before commercial use; it is not an ordinary MIT/BSD licence).

## Completeness checklist

- [x] Real code, not just a PDF: Verilog RTL (`vmod/nvdla`, `vmod/vlibs`, `vmod/rams`, 406 `.v` files under `vmod/`), SystemC C model (`cmod/`), trace-replay testbench (`verif/`, with example traces), synthesis scripts (`syn/`), performance estimates (`perf/`)
- [x] Installation/run instructions: README (basic build + sanity simulation) and the integration manual at nvdla.org
- [x] Examples: example traces for various networks in `verif/traces/`; `tools/bin/` contains `tmake`, `run_sanity`, `vcp`, `defgen`
- [x] Hardware requirements: a standard Linux machine suffices for RTL simulation/synthesis; FPGA/ASIC flows are optional, for implementation; simulating the RTL does not need an NVIDIA GPU

## Minimal upstream reproduction steps (documented path)

```bash
git clone https://github.com/nvdla/hw
cd hw
bin/tmake
```

Expected check (per the repository README): `tmake` compiles the design and runs a short sanity simulation. Full integration needs the integration manual (nvdla.org/integration_guide.html) and a Verilog simulation/synthesis toolchain.

## Parts that cannot be reproduced from this entry alone

- Real RTL area, power, clock and trace-replay performance require a Verilog toolchain and the chosen configuration; the skeleton only demonstrates the pipeline stages.
- The reason the upstream build was not run end-to-end here: this VM does not have a complete Verilog simulation/synthesis toolchain installed.

## Skeleton in this directory

`reproduce.py` is an original standard-library skeleton demonstrating the convolution → activation → pooling pipeline, unrelated to the upstream code.
