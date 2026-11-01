# AI Hardware Accelerator Paper Reproduction

> This is the English index of a bilingual repository: English analysis is in `papers-en/`, Chinese analysis is in `papers/`. The Chinese index is in [README.md](README.md). Every new paper must be added in both languages.
>
> How to use: read the English summary in each paper folder alongside the code sources and reproduction skeleton in that folder's `code/` directory.

## Important note: where the code comes from

- **Most original hardware RTL is not open source.** This repository does not claim to own the original chip code, and it does not label third-party code as the original authors' code.
- Each paper's `code/CODE.md` states clearly whether the code is: official / third-party / simulation tool / skeleton only / not found, and gives verified links plus a reminder to read the license before use.
- Each paper's `code/reproduce.py` is an **original reproduction skeleton**, using only the Python standard library, runnable as-is, for understanding the core ideas (tiling, dataflow, sparsity, systolic arrays, compute-in-memory, domain-specific instructions, and so on). It is **not the original paper code, and it is not RTL**, and it cannot directly reproduce the original area, power, or clock numbers.
- Reproducing the original chip numbers requires the original PDFs, process libraries, synthesis flows, and real simulators; the skeletons in this repository can only verify correctness and relative trends at the algorithm and dataflow level.

## Paper index

| No. | Paper (English title) | Authors and year | Code status |
|---|---|---|---|
| 1 | [Efficient Processing of Deep Neural Networks: A Tutorial and Survey](papers-en/01-sze-survey/README.md) | Vivienne Sze, Yu-Hsin Chen, Tien-Ju Yang, Joel Emer, 2017 | Simulation tool |
| 2 | [DianNao: A Small-Footprint High-Throughput Accelerator for Ubiquitous Machine-Learning](papers-en/02-diannao/README.md) | Tianshi Chen, Zidong Du, Ninghui Sun, et al., 2014 | Skeleton only (no official open-source code found) |
| 3 | [DaDianNao: A Machine-Learning Supercomputer](papers-en/03-dadiannao/README.md) | Yunji Chen, Tao Luo, Shaoli Liu, et al., 2014 | Skeleton only (no official open-source code found) |
| 4 | [ShiDianNao: Shifting Vision Processing Closer to the Sensor](papers-en/04-shidiannao/README.md) | Zidong Du, Robert Fasthuber, Tianshi Chen, et al., 2015 | Skeleton only (no official open-source code found) |
| 5 | [Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks](papers-en/05-eyeriss/README.md) | Yu-Hsin Chen, Tushar Krishna, Joel Emer, Vivienne Sze, 2017 | Third-party RTL (verified to exist, not official) |
| 6 | [In-Datacenter Performance Analysis of a Tensor Processing Unit](papers-en/06-tpu/README.md) | Norman P. Jouppi, Cliff Young, Nishant Patil, David Patterson, et al., 2017 | Simulation tool (Google hardware is not open source) |
| 7 | [EIE: Efficient Inference Engine on Compressed Deep Neural Network](papers-en/07-eie/README.md) | Song Han, Xingyu Liu, Huizi Mao, et al., 2016 | Skeleton only (no official open-source code found for the hardware RTL) |
| 8 | [ISAAC: A Convolutional Neural Network Accelerator with In-Situ Analog Arithmetic in Crossbars](papers-en/08-isaac/README.md) | Ali Shafiee, Anirban Nag, Naveen Muralimanohar, et al., 2016 | Simulation tool (no official ISAAC code) |
| 9 | [Cambricon: An Instruction Set Architecture for Neural Networks](papers-en/09-cambricon/README.md) | Shaoli Liu, Zidong Du, Jinhua Tao, et al., 2016 | Skeleton only (no official open-source code found) |
| 10 | [SCNN: An Accelerator for Compressed-Sparse Convolutional Neural Networks](papers-en/10-scnn/README.md) | Angshuman Parashar, Minsoo Rhu, Anurag Mukkara, et al., 2017 | Simulation tool (original simulator not released) |
| 11 | [EVA: Accelerating LLM Decoding via an Efficient Vector Quantization Architecture](papers-en/11-eva/README.md) | Bowen Duan, Cong Guo, Chiyue Wei, et al., ISCA 2026 | Official code (whether it contains synthesizable RTL not verified) |
| 12 | [Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models](papers-en/12-focus/README.md) | Chiyue Wei, Cong Guo, et al., HPCA 2026 (Best Paper Nominee) | Official implementation (not an RTL claim) |
| 13 | [BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache](papers-en/13-bitdecoding/README.md) | Dayou Du, Shijie Cao, et al., HPCA 2026 | Official GPU system code (not RTL) |
| 14 | [P3-LLM: An Integrated NPU-PIM Accelerator for Edge LLM Inference Using Hybrid Numerical Formats](papers-en/14-p3-llm/README.md) | Yuzong Chen, Chao Fang, et al., ISCA 2026 | Official quantization code; PIM hardware RTL not open source |
| 15 | [MTIA 300: Meta's First Training Chip Featuring Built-in NICs and Collective Offloading Engines](papers-en/15-mtia300/README.md) | MTIA Team (Meta), ISCA 2026 | No official open-source code found; proprietary, RTL not open source |
| 16 | [Early Silicon of Raptor: The First 3D-DRAM Accelerator for Generative Inference](papers-en/16-raptor/README.md) | d-Matrix and University of British Columbia, ISCA 2026 | No official open-source code found; proprietary, RTL not open source |
| 17 | [OSCAR: An Open-Source Flexible and Hierarchical AI Accelerator Generator with Accurate Power Model](papers-en/17-oscar/README.md) | Jay Zhe-An Mok, Qijun Zhang, et al., TODAES 2026 | Official open-source generator, including Chisel and synthesizable RTL |
| 18 | [FSGen: Agile Fused and Sparse Accelerator Generator with Accurate Power Model for LLM Applications](papers-en/18-fsgen/README.md) | Jay Zhe-An Mok, Qijun Zhang, Zhiyao Xie, DAC 2026 | Official open-source generator, including Chisel RTL |
| 19 | [LoCaLUT: Harnessing Capacity-Computation Tradeoffs for LUT-Based Inference in DRAM-PIM](papers-en/19-localut/README.md) | AISys Lab, et al., HPCA 2026 (Best Paper Nominee) | Official PIM implementation (UPMEM, not commercial DRAM RTL) |
| 20 | [Combating the Memory Walls: Optimization Pathways for Long-Context Agentic LLM Inference (PLENA)](papers-en/20-memory-walls/README.md) | Haoran Wu, et al., ISCA 2026 | No official open-source code found; paper says it will be open sourced, link not yet verified |
| 21 | [DCC: Data-Centric Compilation of Machine Learning Kernels for Processing-In-Memory Architectures](papers-en/21-dcc/README.md) | Peiming Yang, et al., ISCA 2026 | Reproducible B: official open source, full numbers need a PIM backend simulator |
| 22 | [XBTorch: A Unified Framework for Modeling and Co-Design of Crossbar-Based Deep Learning Accelerators](papers-en/22-xbtorch/README.md) | Osama Yousuf, et al., APL Machine Learning 2026 | Reproducible A: official open source, standard CPU + PyTorch |
| 23 | [CIM-Tuner: Balancing the Compute and Storage Capacity of SRAM-CIM Accelerator via Hardware-mapping Co-exploration](papers-en/23-cim-tuner/README.md) | Jinwu Chen, et al., arXiv 2026 | Reproducible A: official open source, standard CPU + Python |
| 24 | [A gem5-based Simulation Framework for Computing-in-DRAM (gem5-CIMD)](papers-en/24-gem5-cimd/README.md) | Alexander Kusnezoff, et al., arXiv 2026 | Reproducible A: official open source, standard Linux + gem5 build environment |
| 25 | [OpenACM: An Open-Source SRAM-Based Approximate CiM Compiler](papers-en/25-openacm/README.md) | Yiqi Zhou, et al., DATE 2026 | Reproducible B: official open source, full physical flow needs OpenROAD + FreePDK45 |
| 26 | [TetrisG-SDK: Efficient Convolutional Layer Mapping with Adaptive Windows and Grouped Convolutions for Fast In-Memory Computing](papers-en/26-tetrisg-sdk/README.md) | Ke Dong, et al., IEEE JETCAS 2026 | Reproducible A: official open source, standard CPU + Python |
| 27 | [NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities](papers-en/27-neurosim-v15/README.md) | James Read, et al., IEEE TCAD 2026 | Reproducible A: official open source, standard CPU + C++ (non-commercial license) |
| 28 | [DRAMatic Speedup: Accelerating HE Operations on a Processing-in-Memory System](papers-en/28-dramatic/README.md) | Niklas Klinger, et al., arXiv 2026 | Reproducible B: official open source, full speed reproduction needs UPMEM hardware + SDK |
| 29 | [AHASD: Asynchronous Heterogeneous Architecture for LLM Adaptive Drafting Speculative Decoding on Mobile Devices](papers-en/29-ahasd/README.md) | Ma Zirui, et al., arXiv 2026 | Reproducible A: official open source, standard machine + PIM simulator toolchain |
| 30 | [Characterizing Digital DRAM PIM through Modeling and Benchmarking (PIMeval-PIMbench extension, TACO 2026)](papers-en/30-pimeval-2026/README.md) | Follow the paper's author list, ACM TACO 2026 | Reproducible A: official open source, standard Linux + C++, no UPMEM hardware needed |
| 31 | [AIHWKit: A Flexible and Fast PyTorch Toolkit for Analog Crossbar Arrays](papers-en/31-aihwkit/README.md) | Malte J. Rasch et al. (IBM Research), AICAS 2021 | Fully open source: MIT, 30 examples, standard CPU, GPU optional |
| 32 | [Gemmini: An Agile Systolic Array Generator](papers-en/32-gemmini/README.md) | UC Berkeley, DAC 2021 | Fully open source: Chisel RTL, Linux + Chipyard/Verilator, FPGA optional |
| 33 | [NVDLA: NVIDIA Deep Learning Accelerator (Open Architecture)](papers-en/33-nvdla/README.md) | NVIDIA, open-source release 2017–2018 (not a conventional conference paper, labelled as such) | Fully open source: 406 Verilog files, Linux + Verilog toolchain |
| 34 | [PrIM: The First Benchmark Suite for a Real Processing-in-Memory System](papers-en/34-prim/README.md) | Juan Gómez-Luna et al., IEEE Access 2022 | Fully open source: MIT, 16 benchmarks; CPU baseline needs only GCC, full DPU results need UPMEM hardware + SDK |
| 35 | [ColumnQuant / RUnQuant: Column-Granularity Quantization for Compute-in-Memory Accelerators](papers-en/35-columnquant/README.md) | DATE 2025 / Journal of Systems Architecture 2026 | Full framework code; standard CPU + PyTorch, no licence or requirements file found in the repository root |

## Directory structure

```
papers/
  01-sze-survey/README.md        # Survey: data movement and the dataflow framework
  02-diannao/README.md
  03-dadiannao/README.md
  04-shidiannao/README.md
  05-eyeriss/README.md
  06-tpu/README.md
  07-eie/README.md
  08-isaac/README.md
  09-cambricon/README.md
  10-scnn/README.md
  11-eva/README.md … 20-memory-walls/README.md   # 2026 supplement: ISCA / HPCA / DAC / TODAES 2026
  21-dcc/README.md … 30-pimeval-2026/README.md   # 2026 CIM supplement: reproducibility-screened, A = runnable on a standard machine, B = needs special hardware/toolchain
  31-aihwkit/README.md … 35-columnquant/README.md   # Influential CIM supplement: fully open-source code; skeletons are not upstream code, upstream steps govern reproduction
  <each paper>/code/CODE.md        # Code sources, nature, and run steps
  <each paper>/code/reproduce.py   # Original reproduction skeleton (standard library only)
```

Each paper folder contains: original paper information, core method, core results, reproduction points, and code sources.

## Quick start

```bash
# Pick any paper, read its summary first, then run its skeleton
python3 papers/05-eyeriss/code/reproduce.py
python3 papers/06-tpu/code/reproduce.py
python3 papers/07-eie/code/reproduce.py
```

## License note

- The original content of this repository (the English summaries and the `reproduce.py` reproduction skeletons) is provided as reproduction study examples.
- Upstream code is not copied into this repository; before using any upstream repository, follow the license shipped with that repository, and do not apply an upstream license to this repository's skeletons.
