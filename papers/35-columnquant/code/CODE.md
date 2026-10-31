# 代码来源与复现说明：ColumnQuant / RUnQuant

- 链接：https://github.com/jiyoonkm/ColumnQuant
- 性质：官方开源框架，非第三方实现。
- 许可证：仓库根目录未找到许可证文件；再分发或做产品前请先与作者/论文许可条款核对。

## 完整性清单

- [x] 真实代码，不只是 PDF：`SplitConv4Pim_group.py`（CIM 卷积框架）、`LSQ.py`（学习步长量化）、`any_quant.py`，外加 `legacy/` 目录
- [x] 完整克隆列表中另有入口文件（仅按文件名列出，内容本次未逐项检查，端到端复现时请先检查）：`main.py`、`resnet_quan.py`、`utils.py`
- [x] 检查点：`legacy/` 中的 ResNet-20 CIFAR-100 W3A3P3 检查点（`ResNet20_Cifar100_W3A3P3_ckpt.pth`）
- [x] 安装/运行说明：README 给出 API、参数与使用示例；但根目录没有单独的 `requirements.txt` 或安装脚本，依赖配置（PyTorch 等）需用户自行配置
- [x] 示例：README 使用示例即入口示例；没有单独的 `examples/` 目录
- [ ] 许可证：根目录未找到许可证文件
- [x] 硬件需求：框架本身用标准 CPU + PyTorch 即可；训练较大模型建议 GPU；运行量化框架不需要 CIM 硬件（它在软件中建模 CIM 约束）

## 最小复现步骤（上游，README 示例）

```bash
git clone https://github.com/jiyoonkm/ColumnQuant
cd ColumnQuant
python3 - << 'EOF'
import torch
from SplitConv4Pim_group import SplitConv4Pim_group

conv = SplitConv4Pim_group(
    w_bit=3, split_bit=1, w_mode='Array',
    ps_bit=3, num_sigma=6, psum_mode='Array',
    in_planes=64, planes=64, kernel_size=3,
    N=256, stride=1, padding=1,
)
x = torch.randn(1, 64, 32, 32)
y = conv(x)
print(y.shape)
EOF
```

预期检查：模块无错误构建，前向传播返回 64 通道、3×3 卷积在 32×32 输入上的预期输出形状（确切输出形状取决于框架的切分方式，首次运行时请对照 README 的参数文档核对）。

## 不能仅凭本文复现的部分

- 完整的 PyTorch 训练流程与原文精度表，需要已安装 PyTorch 的机器与检查点/训练脚本；骨架只演示列粒度量化。
- 本次未端到端运行上游，原因是该虚拟机无 PyTorch 且 CPU 版 PyTorch 下载多次超时；语法检查已通过（`SplitConv4Pim_group.py`、`LSQ.py`、`any_quant.py` 均通过 `python3 -m py_compile`）。

## 本目录骨架

`reproduce.py` 为原创标准库骨架，演示列粒度量化与反量化，与上游代码无关。
