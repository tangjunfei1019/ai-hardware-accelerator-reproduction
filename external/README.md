# 上游项目收藏

English summary: this folder is a **collection (favorites) list, not this repository's code**.
Every project below is developed by its own authors, linked here only, and **not
redistributed** in this repository. Nothing here claims these projects as this repository's
own work, and no upstream code is copied into this repo from them.

## 跟随上游更新

Run:

```bash
bash external/sync-external.sh
```

The script clones each project below into `external-checkouts/<name>/` if it is
missing, or runs `git pull` there if it already exists, and prints the HEAD commit
of each project after the update. That is how you follow upstream updates:
re-run the script whenever you want the latest version.

- `external-checkouts/` is **not** committed to this repo (see the note in
  `external/.gitignore-note.txt`). The checkouts live only on your local machine.
- This repository does not use git submodules; the script above is the supported way
  to follow upstream updates. If you want to pin an upstream at a recorded commit
  instead, add it locally with a normal git client
  (`git submodule add <url> external-checkouts/<name>`).
- Licence note: licences below were checked via the GitHub API on 2026-11-02 where a
  licence field was returned. Where the API returned nothing or `NOASSERTION`,
  the licence is written as “未验证 / not verified” — check the upstream repo's
  licence file before redistributing or building a product on it.

## 收藏列表

### 1. Timeloop — https://github.com/NVlabs/timeloop
- 是什么：张量代数加速器的建模、映射与代码生成工具（C++）。
- 许可证：BSD-3-Clause（GitHub API 返回）。
- 为什么收藏：统一的评估语言——同一架构/工作负载/映射格式下可比的周期、能耗、面积，
  是本仓库“对比矩阵”思路的工具来源。对应本仓库论文 01（Sze 综述的建模路线）。
- 注意：安装较重（C++、scons，建议 Docker）。

### 2. Accelergy — https://github.com/Accelergy-Project/accelergy
- 是什么：架构级能耗/面积估算框架，常与 Timeloop 搭配（Python）。
- 许可证：MIT（GitHub API 返回）。
- 为什么收藏：提供可插拔的能耗/面积模型（CACTI、Aladdin 等），补齐 Timeloop 的能量一侧。

### 3. SCALE-Sim — https://github.com/scalesim-project/SCALE-Sim
- 是什么：面向 DNN/GEMM/注意力层的脉动阵列模拟器（Python）。
- 许可证：MIT（GitHub API 返回）。
- 为什么收藏：v2 的解析计算周期经 RTL 仿真验证，v3 支持稀疏、Ramulator 内存建模、
  Accelergy 能耗估算，上手快。对应本仓库论文 06（TPU）的模拟路线。
- 注意：仅适用于脉动/GEMM 形态设计，不能建模 CIM 交叉阵列。

### 4. Gemmini — https://github.com/ucb-bar/gemmini
- 是什么：可参数化的空间阵列加速器生成器，Chisel RTL + RISC-V SoC（Scala/Chisel）。
- 许可证：未验证（GitHub API 返回 NOASSERTION，请查上游许可证文件）。
- 为什么收藏：从论文到可运行硬件的完整路线，社区最大（约 1,545 stars），
  是“别人能在此基础上建造”所以被收藏的例子。对应本仓库论文 32。
- 注意：构建需 Chipyard/Verilator，耗时数小时。

### 5. DNN NeuroSim V2.1 — https://github.com/neurosim/DNN_NeuroSim_V2.1
- 是什么：CIM 加速器基准：面积、延迟、能耗、片上训练（C++）。
- 许可证：未验证（GitHub API 未返回许可证字段；V1.5 另注 CC BY-NC 4.0 非商业，
  使用前请核对本版本的许可证）。
- 为什么收藏：同一框架下可比的 CIM 指标，是“统一可运行路径”中 CIM 一侧的候选。
  对应本仓库论文 08、27。
- 注意：结果是模型估算，不是硅片实测。

### 6. CrossSim — https://github.com/sandialabs/cross-sim
- 是什么：模拟存算一体交叉阵列的模拟精度仿真（Jupyter/Python）。
- 许可证：未验证（GitHub API 返回 NOASSERTION，请查上游许可证文件）。
- 为什么收藏：模拟器件非理想性、噪声、电导变化对 DNN 精度的影响，
  是本仓库骨架没有覆盖的模拟真实性一侧。
- 注意：只给精度，不给面积/能耗/延迟。

### 7. PIMSimulator — https://github.com/SAITPublic/PIMSimulator
- 是什么：存内处理（PIM）模拟器，来自三星的工业实验室（C++）。
- 许可证：未验证（GitHub API 返回 NOASSERTION，请查上游许可证文件）。
- 为什么收藏：给 PIM 论文一个共同的评估平台，而不是每篇论文各用自己的模拟器。
- 注意：偏单一厂商平台，不覆盖模拟 CIM。

### 8. xpu-perf — https://github.com/bytedance/xpu-perf
- 是什么：HPCA 2026 的 AI 加速器基准，带生产视角（Python）。
- 许可证：Apache-2.0（GitHub API 返回）。
- 为什么收藏：不只看峰值 TOPS，还评估易用性与软硬件通用性——这是本仓库
  论文总结里缺失的评价维度。
- 注意：面向商用加速器，不能直接跑本仓库的论文设计。

### 9. awesome-ai-accelerators — https://github.com/LonghornSilicon/awesome-ai-accelerators
- 是什么：AI 加速器精选列表：论文、工具、课程，覆盖从硅片到服务的全栈（链接/笔记）。
- 许可证：未验证（GitHub API 未返回许可证字段，请查上游仓库）。
- 为什么收藏：导航与社区增长的范例——有 CONTRIBUTING.md，靠投稿扩展。
  本仓库可以借鉴它的投稿机制，而不是它的内容深度。
- 注意：它本身只是链接目录，没有逐篇分析与可运行代码。

### 10. awesome-ai-papers-reproduction — https://github.com/Maxbay1017/awesome-ai-papers-reproduction
- 是什么：双语（中英）论文复现合集，带“先最简单数据集、再训练评估、再完整复现”的方法论。
- 许可证：未验证（GitHub API 未返回许可证字段）。
- 为什么收藏：双语复现的方法论模板——复现声明要能用指标检验。
  注意它覆盖的是 ML 论文（NeurIPS/ICML/ICLR/AAAI），不是硬件论文。

### 11. code-reproductions — https://github.com/EYE-666/code-reproductions
- 是什么：中文的逐实验复现记录：环境、命令、日志、结果放在一起。
- 许可证：未验证（GitHub API 未返回许可证字段）。
- 为什么收藏：可审计性的格式范例——本仓库的 `runs/` 证据文件夹正是借鉴它。
- 注意：通用格式，不是硬件专属综述。
