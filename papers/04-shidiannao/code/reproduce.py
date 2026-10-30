"""复现骨架（原创，非原文代码）：ShiDianNao 式传感器直连 vs 经 DRAM。

只用 Python 标准库。演示：小模型放进片上 SRAM 时，直连省掉的 DRAM 访问量。
运行：python3 reproduce.py
"""


def accesses(model_bytes, sram_bytes, image_bytes, via_dram=True):
    """返回 DRAM 访问字节数（简化记账）。"""
    if via_dram:
        return model_bytes + image_bytes * 2  # 写入 DRAM 再读回
    if model_bytes <= sram_bytes:
        return 0  # 模型在片上，图像直连进入计算
    return model_bytes - sram_bytes  # 模型放不下，溢出部分仍需走 DRAM


def main():
    for model in (1_000_000, 10_000_000, 100_000_000):
        d = accesses(model, 2_000_000, 1_000_000, True)
        s = accesses(model, 2_000_000, 1_000_000, False)
        print(f"模型={model} 字节  经DRAM={d}  直连={s}  省掉={d-s}")
    print("结论：模型越小、越能放进片上 SRAM，直连的收益越大；模型过大时收益会衰减。")


if __name__ == "__main__":
    main()
