# NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing

## Original paper information

- **Authors:** Cheng Zou, Shuo Yang, Chen Nie, et al. (Shanghai Jiao Tong University, Shanghai AI Laboratory, Lenovo Research, and collaborators)
- **Venue:** ISCA 2026; arXiv:2605.21952
- **Upstream repository:** https://github.com/Intelligent-Computing-Research-Group/NasZip
- **Licence:** MuLan PSL 2.0 (badge in README; check the repo's licence file before redistribution)
- **Hardware/software requirements:** Pre-built-index route: x86 server with 16+ CPU cores and 256+ GB DRAM; build-from-scratch route needs a large-VRAM GPU and much more time

## Core method

- Feature-level early exiting (FEE): instead of waiting for partial distances to converge, estimate and correct the full-dimensional distance from statistics-based PCA, so exiting happens earlier without losing accuracy.
- Bit-level NDP-aware dynamic-float: a data format that cuts memory traffic for vector data on NDP hardware.
- Data-aware neighbor-list mapping to cut neighbor-retrieval latency and inter-channel communication, plus a dedicated cache exploiting data locality and prefetch.
- System structure: a host CPU connects to DIMM-based DRAM modules over memory channels, each rank embedding near-memory hardware.

## Core results

- Reported in the paper/README: up to 8.4x over the state-of-the-art CPU implementation (SCANN) and 1.4x over the state-of-the-art GPU implementation at equal accuracy; up to 1.69x over the state-of-the-art NDP ANNS accelerator ANSMET. In the reported configuration, recall@1 and recall@10 are at least 90%.
- These numbers are quoted from the paper/README and were not re-measured here; per-dataset recall/throughput tables are authoritative in the original paper.
- The significance is at the application level: it extends NDP/CIM thinking from matrix multiplication to retrieval (a key RAG step), not just a faster distance kernel.

## Reproduction points

- Minimal reproduction (pre-built-index route, as documented): `git clone https://github.com/Intelligent-Computing-Research-Group/NasZip.git`, `conda create -n naszip python=3.12`, `bash init_env.sh`, `pip install torch torchvision huggingface_hub matplotlib pandas seaborn numba`, then `python download_full_dataset.py SIFT GIST GloVe Wiki --output-dir Datasets`, `python download_query_groundtruth.py`, `python download_anns_idx_cache.py`, followed by `bash fee_dim_freq.sh`, `bash get_var.sh`, CSV sync in `result/`, and figure plotting in `Plot/` for Fig. 8.
- Expected check: on a qualifying server, the Fig. 8 pipeline completes in about 10 minutes and updates the CSVs and figure; Figs. 15/18 take about 1 hour each, Fig. 16 about 2.5 hours.
- Honest note: not run end to end here — only `python download_anns_idx_cache.py --help` was run (it printed the Hugging Face index-cache options). The reason is purely hardware: this VM has 4 vCPUs and 7.7 GB RAM, far below the README's 16-core / 256 GB minimum, and the dataset/index downloads are large. This is not a repo defect.

## Code sources

- Upstream code is at the repository link above; `code/CODE.md` in this folder gives the completeness checklist and minimal reproduction commands.
- **`code/reproduce.py` in this folder is an original reproduction skeleton using only the Python standard library, for understanding the core idea. It is not upstream code, and it is not the original hardware/simulator, and it cannot directly reproduce the original paper's numbers.**

