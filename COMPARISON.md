# 对比矩阵 / Comparison Matrix

English note: the same table in English is in [COMPARISON-en.md](COMPARISON-en.md).
本表基于各论文文件夹内的 README.md 与 code/CODE.md 填写，**没有从网上新抄数字**。
峰值一列的标签含义：**论文声称** = 原文报告的数字；**模型估算** = 模拟器/工具给出的估计，
不是硅片实测；**未给出** = 该论文文件夹内没有给出可比的峰值数字（相对加速比、带宽、
能效等不等于峰值，已在括号中注明，仅作上下文）。

## 不确定性说明

- 峰值性能：39 篇中只有 2 篇（06 TPU、07 EIE）在文件夹内给出了可比的峰值数字；
  其余 37 篇均为“未给出”。不要把相对加速比当作峰值来比较。
- 精度：以下论文在文件夹内未说明位宽：01、04、05、09、10、12、15、16、17、18、21、
  23、26、28、29、30、36，以及 39（模拟器，不适用）；07、08、19、20、22、25、27、
  31、32、34、37 只提到量化/格式，未给单一固定位宽（表中已注明）。
- 工作负载不确定：23 CIM-Tuner（未说明具体工作负载）、30 PIMeval（宽泛，无单一工作负载）。
- 本地运行状态：31 与 35 已按最新证据更新为“上游已运行”（见 `runs/` 文件夹），
  与其文件夹内较旧的“未运行”文字不一致时，以 `runs/` 证据为准；23 的运行是 2026-10-31
  的历史记录（工具估算），不在本次新增的 `runs/` 内。

## 对比表

| # | 论文 | 工作负载 | 数据流/架构 | 精度 | 峰值性能（标签：论文声称 / 模型估算 / 未给出） | 代码类型 | 本地能否运行 |
|---|---|---|---|---|---|---|---|
| 1 | [Sze 综述](papers/01-201712-sze-survey/README.md) | DNN 处理（综述，无单一工作负载） | 空间架构；权平稳/输出平稳/行平稳数据流 | 未说明 | 未给出 | 仿真工具 + 骨架 | 骨架 |
| 2 | [DianNao](papers/02-201403-diannao/README.md) | 机器学习/神经网络推理 | NFU（乘法树+加法树+激活），分块，独立缓冲 | 16 位定点 | 未给出 | 仅骨架（未找到官方代码） | 骨架 |
| 3 | [DaDianNao](papers/03-201412-dadiannao/README.md) | 大规模模型机器学习推理，多芯片 | 多片、eDRAM 中心、权本地化、激活广播 | 16/32 位定点 | 未给出 | 仅骨架（未找到官方代码） | 骨架 |
| 4 | [ShiDianNao](papers/04-201506-shidiannao/README.md) | 近传感器的小模型视觉/CNN 处理 | 传感器直连 NFU，模型驻留片上 SRAM，绕过 DRAM | 未说明 | 未给出 | 仅骨架（未找到官方代码） | 骨架 |
| 5 | [Eyeriss](papers/05-201701-eyeriss/README.md) | 深度 CNN 推理（卷积层） | 168-PE 空间阵列，行平稳数据流，可重构多播 NoC | 未说明 | 未给出（论文声称：AlexNet 卷积层约 35 fps，约 278 mW） | 第三方 RTL + 骨架 | 骨架（第三方 RTL 未运行） |
| 6 | [TPU](papers/06-201706-tpu/README.md) | 数据中心推理：MLP、CNN、LSTM | 256×256 脉动阵列矩阵乘单元，约 28 MiB 片上存储 | INT8 推理 | 论文声称：峰值约 92 TOPS（8 位） | 仿真工具 + 骨架 | 骨架 |
| 7 | [EIE](papers/07-201606-eie/README.md) | 压缩 DNN 推理（尤全连接层） | 稀疏 PE 阵列，CSC 压缩稀疏格式，权共享码本，跳过零值 | 权共享量化（位宽未说明） | 论文声称：压缩网络约 102 GOPS，约合未压缩约 3 TOPS | 仅骨架（未找到官方硬件 RTL） | 骨架 |
| 8 | [ISAAC](papers/08-201606-isaac/README.md) | CNN 推理 | CIM：ReRAM 交叉阵列原位模拟矩阵乘，分层结构，位切片+流水线 | 位切片模拟（切片宽未说明） | 未给出 | 仿真工具 + 骨架 | 骨架 |
| 9 | [Cambricon](papers/09-201606-cambricon/README.md) | 通用神经网络算法（10 个基准） | 领域专用存取指令集架构，非固定数据流加速器 | 未说明 | 未给出 | 仅骨架（未找到官方代码） | 骨架 |
| 10 | [SCNN](papers/10-201706-scnn/README.md) | 压缩稀疏 CNN 推理 | 乘法阵列+散射累加阵列，压缩权/激活格式 | 未说明 | 未给出（论文声称：相对稠密约 2.7 倍性能、2.3 倍能效） | 仿真工具 + 骨架 | 骨架 |
| 11 | [EVA](papers/11-202606-eva/README.md) | LLM 解码（访存受限小 GEMV） | 向量量化查表架构：输入×码本点积代替反量化后乘加 | 约 2 位级权压缩（码本索引） | 未给出（论文声称：最高约 11.17 倍加速、7.17 倍能效） | 官方 + 骨架 | 骨架（上游未运行） |
| 12 | [Focus](papers/12-202602-focus/README.md) | 视觉语言模型推理（视觉 token 缩减） | 流式集中模块 + 脉动阵列：语义剪枝、时空块集中、运动感知去重 | 未说明 | 未给出（论文声称：约 2.4 倍加速、3.3 倍能耗降低） | 官方 + 骨架 | 骨架（上游未运行） |
| 13 | [BitDecoding](papers/13-202602-bitdecoding/README.md) | 长上下文 LLM 解码，低位 KV 缓存 | GPU CUDA 核 + Tensor 核协同执行（非加速器 RTL） | 低位 KV：NVFP4 / MXFP4 | 未给出（论文声称：相对 FP16 FlashDecoding-v2 平均约 7.5 倍解码加速） | 官方 + 骨架 | 骨架（上游未运行） |
| 14 | [P3-LLM](papers/14-202606-p3-llm/README.md) | 边缘 LLM 推理：预填充 GEMM + 解码 | NPU-PIM 集成：NPU 做预填充，DRAM PIM 做解码 | 4 位权/KV，8 位激活与注意力分数 | 未给出 | 官方（部分）+ 骨架 | 骨架 |
| 15 | [MTIA 300](papers/15-202606-mtia300/README.md) | 推荐/排序训练（150B 参数生产模型） | 封装内建网络：2 个网络芯片，12×800 Gbps RDMA NIC，集体卸载引擎 | 未说明 | 未给出（约 1.2 TB/s 总 I/O，论文声称，非算力峰值） | 未找到 + 骨架 | 骨架 |
| 16 | [Raptor](papers/16-202606-raptor/README.md) | 生成式推理，长上下文 KV 主导解码 | 3D-DRAM：逻辑裸片与定制 DRAM 裸片面对面键合 | 未说明 | 未给出（论文声称：单卡带宽 >100 TB/s，非算力峰值） | 未找到 + 骨架 | 骨架 |
| 17 | [OSCAR](papers/17-202609-oscar/README.md) | 加速器生成（可配置目标） | 分层生成器：由硬件/工作负载规格自动生成 Chisel RTL，含功耗模型 | 未说明 | 未给出（论文声称：功耗模型误差约 3.8%） | 官方 + 骨架 | 骨架 |
| 18 | [FSGen](papers/18-202607-fsgen/README.md) | LLM 应用（融合算子、稀疏计算） | 统一数据流表示 + Chisel RTL 生成 + 早期 PPA 估计 | 未说明 | 未给出（论文声称：约 1.4 倍功耗效率或约 10 倍加速） | 官方 + 骨架 | 骨架 |
| 19 | [LoCaLUT](papers/19-202602-localut/README.md) | DRAM-PIM 上的 DNN 推理 | LUT 推理：多 MAC 打包进一次查表，LUT 规范化/去重 | 未说明（多精度） | 未给出（论文声称：几何平均加速约 1.82 倍） | 官方 + 骨架 | 骨架 |
| 20 | [Memory Walls / PLENA](papers/20-202606-memory-walls/README.md) | 长上下文智能体 LLM 推理 | PLENA 系统：扁平脉动阵列 + 混合精度非对称量化 + PLENA_ISA | 混合精度（位宽未说明） | 未给出（论文声称：相对 A100 最高约 2.23 倍吞吐） | 未找到 + 骨架 | 骨架 |
| 21 | [DCC](papers/21-202606-dcc/README.md) | 数据中心 ML 内核，PIM 上的端到端 LLM 推理 | 多层 PIM 抽象，数据分片到计算循环分片的映射 | 未说明 | 未给出（论文声称：HBM-PIM 最高约 7.68 倍加速） | 官方 + 骨架 | 骨架 |
| 22 | [XBTorch](papers/22-202610-xbtorch/README.md) | 基于交叉阵列的深度学习推理与硬件感知训练 | PyTorch 原生交叉阵列建模：权映射为电导，器件变化与噪声注入 | 量化（位宽未说明） | 未给出（数字见原文表） | 官方 + 骨架 | 骨架 |
| 23 | [CIM-Tuner](papers/23-202601-cim-tuner/README.md) | SRAM-CIM 硬件-映射协同探索（具体工作负载未说明） | SRAM-CIM 宏矩阵抽象 + 通用加速器模板，面积约束下联合搜索 | 未说明 | 未给出（论文声称：能效约 1.58 倍、吞吐约 2.11 倍；工具估算见注） | 官方 + 骨架 | 上游曾运行（2026-10-31：CIMMA 编译器 + 单算子模拟，工具估算，非硅片实测） |
| 24 | [gem5-CIMD](papers/24-202610-gem5-cimd/README.md) | 全应用存内 DRAM 计算（KNN 案例） | gem5 内 DRAM 子阵列计算：扩展 ISA、子阵列感知地址映射 | 4–64 位（ISA 操作宽度） | 未给出 | 仿真器（官方）+ 骨架 | 骨架（gem5 构建未运行） |
| 25 | [OpenACM](papers/25-202604-openacm/README.md) | SRAM 数字 CIM 上的代表性 CNN | SRAM 数字 CIM 编译器：精确/可调近似/对数量化乘法器库 | 近似乘法（位宽未说明） | 未给出（论文声称：代表性 CNN 节能最高约 64%） | 官方 + 骨架 | 骨架 |
| 26 | [TetrisG-SDK](papers/26-202604-tetrisg-sdk/README.md) | 卷积层：CNN8、GoogLeNet、DenseNet40 | 移位复制核（SDK）映射 + 自适应窗口 + 分组卷积 | 未说明 | 未给出（论文声称：约 1.2–1.3 倍加速，模拟估算） | 官方 + 骨架 | 骨架 |
| 27 | [NeuroSim V1.5](papers/27-202600-neurosim-v15/README.md) | CIM 基准：CNN 与 Transformer（ViT 案例） | 混合 ACIM/DCIM 基准框架，TensorRT 后训练量化 + 统计噪声注入 | 量化（位宽未说明） | 未给出（论文声称：相对 V1.4 运行速度最高约 6.5 倍） | 仿真器（官方）+ 骨架 | 骨架 |
| 28 | [DRAMatic](papers/28-202602-dramatic/README.md) | PIM 上的同态加密运算：BGV 乘法、NTT 等 | UPMEM 通用 PIM；RNS + NTT 多项式运算 | 未说明 | 未给出（论文声称：相对此前 UPMEM HE 实现约 334 倍） | 官方 + 骨架 | 未运行（需 UPMEM 硬件） |
| 29 | [AHASD](papers/29-202604-ahasd/README.md) | 移动设备上的 LLM 自适应草稿推测解码 | 任务级异步：草稿模型在 PIM，目标模型在单 NPU 批量验证 | 未说明 | 未给出（论文声称：相对 GPU 基线吞吐最高约 4.2 倍，模拟） | 仿真器（官方）+ 骨架 | 骨架 |
| 30 | [PIMeval-PIMbench](papers/30-202600-pimeval-2026/README.md) | 数字 DRAM PIM 工作负载（宽泛，无单一工作负载） | 三类数字 PIM：子阵列位串行、位并行、bank 级位并行；屋顶线分析 | 未说明 | 未给出（适用区间与交叉点，非单一数字） | 仿真器（官方）+ 骨架 | 骨架 |
| 31 | [AIHWKit](papers/31-202106-aihwkit/README.md) | 模拟交叉阵列上的 DNN 训练/推理 | 权在阻性交叉阵列“模拟单元”上，ADC/DAC 与噪声建模 | ADC/DAC 量化（位宽未说明） | 未给出（工具，不引用单一加速比） | 官方 | 上游已运行（见 runs/aihwkit-20261101） |
| 32 | [Gemmini](papers/32-202112-gemmini/README.md) | 边缘深度学习推理（含 ResNet-50 级程序） | Chisel 生成的脉动阵列，输出平稳+权平稳，集成 Rocket Chip SoC | 多种数据类型（位宽未说明） | 未给出（论文声称：相对主机 100–1000 倍范围，配置相关，非单一结果） | 官方 | 未构建（Chipyard 多小时构建未尝试） |
| 33 | [NVDLA](papers/33-201709-nvdla/README.md) | 深度学习推理 | 模块化流水线：CDMA→CSC→CMAC→CACC→SDP→PDP→CDP | 8 位（2048 MAC）/ 16 位（1024 MAC），nvdlav1 固定版本 | 未给出（无单一加速比；性能见 Primer 与 perf/ 估计表） | 官方 | 未运行（无完整 Verilog 工具链） |
| 34 | [PrIM](papers/34-202205-prim/README.md) | 16 个基准：线性代数、数据库、图、神经网络等 | 真实 UPMEM 系统：每 DRAM bank 旁一个通用 DPU；640 与 2556 DPU 系统 | INT32（VA 示例命令；论文无单一精度） | 未给出（分工作负载的可扩展性/性能/能耗表） | 官方 | 上游部分已运行（VA CPU 基线 59.957 ms；DPU 需硬件未运行） |
| 35 | [ColumnQuant / RUnQuant](papers/35-202503-columnquant/README.md) | CIM 推理卷积；ResNet-20/18，CIFAR-10/100 与 ImageNet | CIM 交叉阵列，列粒度对齐缩放（权+部分和）；RUnQuant 非锚定权分解 | 3 位权与部分和（w_bit=3, ps_bit=3） | 未给出（论文声称：精度提升最高 4.05%，非峰值） | 官方 | 上游已运行（见 runs/columnquant-20261102） |
| 36 | [UniNDP](papers/36-202503-unindp/README.md) | GEMM、ResNet-18、VGG-11、LLaMA-2 预填充与解码 | 统一树形 NDP 硬件抽象 + 统一 ISA；周期精确指令驱动模拟器 | 未说明 | 未给出（论文声称：1.05–3.43 倍加速） | 仿真器（官方） | 上游小规模已运行（16×16×16 GEMM，best_result 98；工具最后非零退出） |
| 37 | [NasZip](papers/37-202606-naszip/README.md) | 近似最近邻搜索（SIFT、GIST、GloVe、Wiki），用于检索/RAG | DIMM 近数据处理：主机经内存通道，逐 rank 近存硬件；特征级提前退出 | 动态浮点格式（无固定位宽） | 未给出（论文声称：相对 CPU SCANN 最高 8.4 倍） | 官方 + 骨架 | 未端到端运行（仅 --help；需 16+ 核/256+ GB） |
| 38 | [CIM-Explorer / CIM-E](papers/38-202506-cim-explorer/README.md) | RRAM 交叉阵列上的二值/三值神经网络推理 | TVM 编译栈 + 多模拟后端 + 设计空间探索，统一编译-模拟-DSE 循环 | 二值/三值（1 位/三值权） | 未给出（工具/DSE 流程，无单一 headline 数字） | 仿真器/工具（官方） | 未运行（缺 TVM/Docker） |
| 39 | [Ramulator 2.1](papers/39-202606-ramulator21/README.md) | DRAM 轨迹工作负载（非加速器；仅示例轨迹） | 周期级 DRAM 器件 + 控制器模型，Python 可配置；DDR/GDDR/LPDDR/HBM | 不适用（模拟器，无计算精度） | 未给出（示例统计：控制器周期 81302，平均读延迟 45.2 周期，模型估算） | 仿真器（官方） | 上游已运行（example_config.py；完整测试未运行） |
