"""复现骨架（原创，非原文代码）：3D-DRAM 带宽与 I/O 能效模型。

只用 Python 标准库。演示：同样数量的 KV/权重字节，
在不同带宽与 pJ/bit 下的传输时间与 I/O 能耗差异。
运行：python3 reproduce.py
"""


def transfer_time(data_tb, bandwidth_tbps):
    return data_tb / bandwidth_tbps  # 秒（量级示意）


def io_energy(data_bits, pj_per_bit):
    return data_bits * pj_per_bit * 1e-12  # 焦耳


def main():
    data_tb = 10.0  # 示意：10 TB 数据
    bits = data_tb * 8e12
    for name, bw, pj in [("HBM 式（示意 3 TB/s，约 10 pJ/bit）", 3.0, 10.0),
                         ("3D-DRAM 式（示意 100 TB/s，0.37 pJ/bit）", 100.0, 0.37)]:
        t = transfer_time(data_tb, bw)
        e = io_energy(bits, pj)
        print(f"{name}：传输时间约 {t:.3f} s，I/O 能耗约 {e:.2f} J")
    assert transfer_time(data_tb, 100.0) < transfer_time(data_tb, 3.0)
    print("要点：生成式推理的解码阶段是带宽受限的，带宽密度与 pJ/bit 直接决定延迟与能耗——这正是 Raptor 把 DRAM 做进 3D 封装的动机。")


if __name__ == "__main__":
    main()
