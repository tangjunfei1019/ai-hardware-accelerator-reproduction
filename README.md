# AI 硬件加速器论文复现

> 使用方法：一边看每篇论文文件夹里的中文总结，一边看同文件夹 `code/` 里的代码来源与复现骨架。

## 重要说明：代码从哪里来

- **大多数原始硬件 RTL 并不开源。** 本仓库不声称拥有原文芯片代码，也不把第三方代码标注为原作者代码。
- 每篇论文的 `code/CODE.md` 会明确标注：官方 / 第三方 / 仿真工具 / 仅骨架 / 未找到，并给出已核实的链接与使用前需阅读许可证的提醒。
- 每篇论文的 `code/reproduce.py` 都是**原创复现骨架**，仅用 Python 标准库，可直接运行，用于理解核心思想（分块、数据流、稀疏、脉动阵列、存算一体、领域专用指令等），**不是原文代码，也不是 RTL**，不能直接复现原文的面积、功耗与时钟数字。
- 复现原文芯片数字需要原文 PDF、工艺库、综合流程与真实仿真器；本仓库的骨架只能验证算法与数据流层面的正确性与相对趋势。

## 论文索引

| 序号 | 论文（中文标题） | 作者与年份 | 代码状态 |
|---|---|---|---|
| 1 | [深度神经网络的高效处理：教程与综述](papers/01-sze-survey/README.md) | Vivienne Sze、Yu-Hsin Chen、Tien-Ju Yang、Joel Emer，2017 | 仿真工具 |
| 2 | [DianNao：面向普适机器学习的小面积高吞吐加速器](papers/02-diannao/README.md) | Tianshi Chen、Zidong Du、Ninghui Sun 等，2014 | 仅骨架（未找到官方开源代码） |
| 3 | [DaDianNao：机器学习超级计算机](papers/03-dadiannao/README.md) | Yunji Chen、Tao Luo、Shaoli Liu 等，2014 | 仅骨架（未找到官方开源代码） |
| 4 | [ShiDianNao：将视觉处理移近传感器](papers/04-shidiannao/README.md) | Zidong Du、Robert Fasthuber、Tianshi Chen 等，2015 | 仅骨架（未找到官方开源代码） |
| 5 | [Eyeriss：面向深度卷积神经网络的节能可重构加速器](papers/05-eyeriss/README.md) | Yu-Hsin Chen、Tushar Krishna、Joel Emer、Vivienne Sze，2017 | 第三方 RTL（已核实存在，非官方） |
| 6 | [数据中心张量处理单元的性能分析](papers/06-tpu/README.md) | Norman P. Jouppi、Cliff Young、Nishant Patil、David Patterson 等，2017 | 仿真工具（谷歌硬件不开源） |
| 7 | [EIE：面向压缩深度神经网络的高效推理引擎](papers/07-eie/README.md) | Song Han、Xingyu Liu、Huizi Mao 等，2016 | 仅骨架（硬件 RTL 未找到官方开源代码） |
| 8 | [ISAAC：基于交叉阵列原位模拟运算的卷积神经网络加速器](papers/08-isaac/README.md) | Ali Shafiee、Anirban Nag、Naveen Muralimanohar 等，2016 | 仿真工具（无官方 ISAAC 代码） |
| 9 | [Cambricon：面向神经网络的指令集架构](papers/09-cambricon/README.md) | Shaoli Liu、Zidong Du、Jinhua Tao 等，2016 | 仅骨架（未找到官方开源代码） |
| 10 | [SCNN：面向压缩稀疏卷积神经网络的加速器](papers/10-scnn/README.md) | Angshuman Parashar、Minsoo Rhu、Anurag Mukkara 等，2017 | 仿真工具（原仿真器未发布） |
| 11 | [EVA：基于高效向量量化架构的大模型解码加速](papers/11-eva/README.md) | Bowen Duan、Cong Guo、Chiyue Wei 等，ISCA 2026 | 官方代码（是否含可综合 RTL 未核实） |
| 12 | [Focus：面向高效视觉语言模型的流式集中架构](papers/12-focus/README.md) | Chiyue Wei、Cong Guo 等，HPCA 2026（最佳论文提名） | 官方实现（非 RTL 声明） |
| 13 | [BitDecoding：用张量核心解锁长上下文大模型的低比特 KV 缓存解码](papers/13-bitdecoding/README.md) | Dayou Du、Shijie Cao 等，HPCA 2026 | 官方 GPU 系统代码（非 RTL） |
| 14 | [P3-LLM：基于混合数值格式的 NPU-PIM 融合边缘大模型推理加速器](papers/14-p3-llm/README.md) | Yuzong Chen、Chao Fang 等，ISCA 2026 | 官方量化代码；PIM 硬件 RTL 不开源 |
| 15 | [MTIA 300：Meta 首款内置网卡与集合通信卸载引擎的训练芯片](papers/15-mtia300/README.md) | MTIA Team（Meta），ISCA 2026 | 未找到官方开源代码；工业专有，RTL 不开源 |
| 16 | [Raptor 早期硅片：首款面向生成式推理的 3D-DRAM 加速器](papers/16-raptor/README.md) | d-Matrix 与英属哥伦比亚大学，ISCA 2026 | 未找到官方开源代码；工业专有，RTL 不开源 |
| 17 | [OSCAR：开源灵活分层 AI 加速器生成器与精确功耗模型](papers/17-oscar/README.md) | Jay Zhe-An Mok、Qijun Zhang 等，TODAES 2026 | 官方开源生成器，含 Chisel 与可综合 RTL |
| 18 | [FSGen：面向大模型应用的敏捷融合稀疏加速器生成器与精确功耗模型](papers/18-fsgen/README.md) | Jay Zhe-An Mok、Qijun Zhang、Zhiyao Xie，DAC 2026 | 官方开源生成器，含 Chisel RTL |
| 19 | [LoCaLUT：利用容量-计算权衡实现基于查表的 DRAM 存内推理](papers/19-localut/README.md) | AISys Lab 等，HPCA 2026（最佳论文提名） | 官方 PIM 实现（UPMEM，非商用 DRAM RTL） |
| 20 | [对抗存储墙：长上下文智能体大模型推理的优化路径（PLENA）](papers/20-memory-walls/README.md) | Haoran Wu 等，ISCA 2026 | 未找到官方开源代码；论文称将开源，链接尚未核实 |
| 21 | [DCC：面向存内处理架构的数据中心机器学习内核编译器](papers/21-dcc/README.md) | Peiming Yang 等，ISCA 2026 | 可复现 B：官方开源，完整数字需 PIM 后端仿真器 |
| 22 | [XBTorch：面向交叉阵列深度学习加速器的统一建模与协同设计框架](papers/22-xbtorch/README.md) | Osama Yousuf 等，APL Machine Learning 2026 | 可复现 A：官方开源，标准 CPU + PyTorch |
| 23 | [CIM-Tuner：通过硬件-映射协同探索平衡 SRAM-CIM 计算与存储容量](papers/23-cim-tuner/README.md) | Jinwu Chen 等，arXiv 2026 | 可复现 A：官方开源，标准 CPU + Python |
| 24 | [gem5-CIMD：面向 DRAM 存内计算的全应用 gem5 仿真框架](papers/24-gem5-cimd/README.md) | Alexander Kusnezoff 等，arXiv 2026 | 可复现 A：官方开源，标准 Linux + gem5 构建环境 |
| 25 | [OpenACM：开源 SRAM 近似数字存内计算编译器](papers/25-openacm/README.md) | Yiqi Zhou 等，DATE 2026 | 可复现 B：官方开源，完整物理流程需 OpenROAD + FreePDK45 |
| 26 | [TetrisG-SDK：面向快速存内计算的自适应窗口与分组卷积映射框架](papers/26-tetrisg-sdk/README.md) | Ke Dong 等，IEEE JETCAS 2026 | 可复现 A：官方开源，标准 CPU + Python |
| 27 | [NeuroSim V1.5：面向存内计算加速器的改进软件基准框架](papers/27-neurosim-v15/README.md) | James Read 等，IEEE TCAD 2026 | 可复现 A：官方开源，标准 CPU + C++（非商业许可） |
| 28 | [DRAMatic：面向同态加密运算的 UPMEM 存内处理加速](papers/28-dramatic/README.md) | Niklas Klinger 等，arXiv 2026 | 可复现 B：官方开源，完整速度复现需 UPMEM 硬件 + SDK |
| 29 | [AHASD：面向移动端自适应草稿推测解码的异步异构 NPU-PIM 架构](papers/29-ahasd/README.md) | Ma Zirui 等，arXiv 2026 | 可复现 A：官方开源，标准机器 + PIM 仿真器工具链 |
| 30 | [PIMeval-PIMbench 2026 扩展：面向数字 DRAM PIM 的建模与基准扩展](papers/30-pimeval-2026/README.md) | 以原文作者表为准，ACM TACO 2026 | 可复现 A：官方开源，标准 Linux + C++，不需 UPMEM 硬件 |
| 31 | [AIHWKit：面向模拟交叉阵列的灵活快速 PyTorch 工具包](papers/31-aihwkit/README.md) | Malte J. Rasch 等（IBM Research），AICAS 2021 | 完整开源：MIT，30 个示例，标准 CPU，GPU 可选 |
| 32 | [Gemmini：敏捷脉动阵列生成器](papers/32-gemmini/README.md) | UC Berkeley，DAC 2021 | 完整开源：Chisel RTL，Linux + Chipyard/Verilator，FPGA 可选 |
| 33 | [NVDLA：NVIDIA 深度学习加速器（开放架构）](papers/33-nvdla/README.md) | NVIDIA，开源发布 2017–2018（非传统会议论文，已标注） | 完整开源：406 个 Verilog 文件，Linux + Verilog 工具链 |
| 34 | [PrIM：面向真实存内处理系统的首个基准测试集](papers/34-prim/README.md) | Juan Gómez-Luna 等，IEEE Access 2022 | 完整开源：MIT，16 个基准；CPU 基线仅需 GCC，完整 DPU 结果需 UPMEM 硬件 + SDK |
| 35 | [ColumnQuant / RUnQuant：面向存内计算加速器的列粒度量化](papers/35-columnquant/README.md) | DATE 2025 / Journal of Systems Architecture 2026 | 完整框架代码；标准 CPU + PyTorch，根目录未找到许可证与 requirements 文件 |

## 目录结构

```
papers/
  01-sze-survey/README.md        # 综述：数据搬运与数据流框架
  02-diannao/README.md
  03-dadiannao/README.md
  04-shidiannao/README.md
  05-eyeriss/README.md
  06-tpu/README.md
  07-eie/README.md
  08-isaac/README.md
  09-cambricon/README.md
  10-scnn/README.md
  11-eva/README.md … 20-memory-walls/README.md   # 2026 年补充：ISCA / HPCA / DAC / TODAES 2026
  21-dcc/README.md … 30-pimeval-2026/README.md   # 2026 年 CIM 补充：可复现筛选，A 为标准机器可跑，B 需特殊硬件/工具链
  31-aihwkit/README.md … 35-columnquant/README.md   # 影响力 CIM 补充：完整开源代码，骨架不是上游代码，复现以上游步骤为准
  <每篇>/code/CODE.md              # 代码来源、性质、运行步骤
  <每篇>/code/reproduce.py         # 原创复现骨架（标准库可运行）
```

每个论文文件夹都包含：原文信息、核心方法、核心效果、复现要点、代码来源。

## 快速开始

```bash
# 任选一篇，先读总结，再跑骨架
python3 papers/05-eyeriss/code/reproduce.py
python3 papers/06-tpu/code/reproduce.py
python3 papers/07-eie/code/reproduce.py
```

## 许可证说明

- 本仓库的原创内容（中文总结与 `reproduce.py` 复现骨架）为复现学习示例。
- 上游代码不在本仓库内拷贝；使用任何上游仓库前，请以该仓库自带的许可证为准，不要把上游许可证套用到本仓库的骨架上。
