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
