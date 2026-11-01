# NasZip：面向 DIMM 近数据处理的近似最近邻搜索软硬件协同设计

## 原文信息

- **英文原题：** NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing
- **作者：** Cheng Zou、Shuo Yang、Chen Nie 等（上海交通大学、上海人工智能实验室、联想研究院及合作者）
- **发表处：** ISCA 2026；arXiv:2605.21952
- **上游仓库：** https://github.com/Intelligent-Computing-Research-Group/NasZip
- **许可证：** MuLan PSL 2.0（README 标注；再分发前请核对仓库许可证文件）
- **硬件/软件需求：** 预建索引路线：x86 服务器，16 核以上、256 GB 以上 DRAM；从头构建路线需大显存 GPU，耗时更长

## 核心方法

- 特征级提前退出（FEE）：不等部分距离收敛，用基于统计的 PCA 估计并修正全维距离，从而更早退出且不损失精度。
- 位级 NDP 感知的动态浮点格式：削减 NDP 硬件上向量数据所需的存储流量。
- 数据感知邻居列表映射：削减邻居检索延迟与通道间通信；另有利用数据局部性与预取的专用缓存。
- 系统结构：宿主 CPU 经存储通道连接 DIMM 式 DRAM 模块，每个 rank 内嵌近存硬件。

## 核心效果

- 论文/README 报告：在同等精度下，相对最先进的 CPU 实现（SCANN）最高 8.4 倍，相对最先进的 GPU 实现 1.4 倍，相对最先进的 NDP 近似最近邻加速器 ANSMET 最高 1.69 倍；报告配置下 recall@1 与 recall@10 均不低于 90%。
- 以上数字引自论文/README，未在本机重新测量；分数据集的召回率/吞吐表格以原文为准。
- 意义在于应用层面：把 NDP/CIM 思路从矩阵乘法扩展到检索（RAG 的关键环节），而非只做更快的距离核。

## 复现要点

- 最小复现（预建索引路线，按文档）：`git clone https://github.com/Intelligent-Computing-Research-Group/NasZip.git`，`conda create -n naszip python=3.12`，`bash init_env.sh`，`pip install torch torchvision huggingface_hub matplotlib pandas seaborn numba`，随后依次运行 `download_full_dataset.py SIFT GIST GloVe Wiki --output-dir Datasets`、`download_query_groundtruth.py`、`download_anns_idx_cache.py`，再运行 `bash fee_dim_freq.sh`、`bash get_var.sh`，在 `result/` 下同步 CSV 并在 `Plot/` 下绘制图 8。
- 预期检查：在符合硬件要求的服务器上，图 8 流水线约 10 分钟完成并更新 CSV 与图；图 15/18 约 1 小时，图 16 约 2.5 小时。
- 诚实说明：本机未端到端运行——仅运行了 `download_anns_idx_cache.py --help`（打印 Hugging Face 索引缓存选项）。原因纯粹是硬件：本虚拟机为 4 核 CPU、7.7 GB 内存，远低于 README 要求的 16 核、256 GB；数据集与索引下载也很大。这不是仓库缺陷。

## 代码来源

- 上游代码见上游仓库链接；本文件夹的 `code/CODE.md` 给出完整性清单与最小复现命令。
- **本文件夹的 `code/reproduce.py` 是原创复现骨架，仅用 Python 标准库，用于理解核心思想，不是上游代码，也不是原文硬件/仿真器，不能直接复现原文数字。**

