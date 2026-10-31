# 代码来源与复现说明：AIHWKit

- 链接：https://github.com/IBM/aihwkit
- 性质：官方开源工具包，非第三方实现。
- 许可证：MIT（`LICENSE.txt`），使用前请以仓库自带许可证为准。

## 完整性清单

- [x] 真实代码，不只是 PDF：Python + C++/CUDA 模拟器（`src/`），PyTorch 集成
- [x] 安装/运行说明：README + 文档 https://aihwkit.readthedocs.io
- [x] 示例：`examples/`（30 个编号示例，如 `01_simple_layer.py`、LeNet-5、ResNet、BERT 示例）与 `notebooks/` 教程
- [x] 测试：`tests/`（克隆中数得 30 个测试文件）
- [x] 硬件需求：标准 CPU 可跑；GPU/CUDA 可选，仅在可用时使用

## 最小复现步骤（上游）

```bash
pip install aihwkit
git clone https://github.com/IBM/aihwkit
cd aihwkit
python examples/01_simple_layer.py
```

预期检查：脚本构建一个一层模拟网络（`AnalogLinear(4, 2)`，常数步进器件），训练它求输入之和，并打印训练过程。不需要 GPU。

## 不能仅凭本文复现的部分

- 完整的 PCM 器件统计模型校准、GPU 加速版模拟器性能、原文各实验的精度表，需要按原文与上游文档在有 PyTorch 的机器上跑完整示例。
- 本次未端到端运行上游示例的原因：当前虚拟机无 PyTorch，且 CPU 版 PyTorch 下载多次超时；这是环境限制，不是仓库缺陷。

## 本目录骨架

`reproduce.py` 为原创标准库骨架，演示模拟片上的矩阵向量乘 + 噪声 + ADC 量化，与上游代码无关。
