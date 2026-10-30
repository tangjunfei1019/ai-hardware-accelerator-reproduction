"""复现骨架（原创，非原文代码）：DaDianNao 式多 tile 分区与广播记账。

只用 Python 标准库。演示：输出通道分给多个 tile 时，权重本地化、激活广播的效果。
运行：python3 reproduce.py
"""


def model(tiles, out_channels, in_channels):
    """返回每个 tile 的权重本地量、广播激活量、MAC 数。"""
    per_tile_out = out_channels // tiles
    weight_local = per_tile_out * in_channels  # 每个 tile 只存自己的权重
    act_broadcast = in_channels  # 激活广播给所有 tile（记一次广播量）
    macs_per_tile = per_tile_out * in_channels
    return weight_local, act_broadcast, macs_per_tile


def main():
    for tiles in (1, 2, 4, 8):
        w, a, m = model(tiles, out_channels=256, in_channels=256)
        print(f"tile 数={tiles}  每 tile 权重={w}  广播激活={a}  每 tile MAC={m}")
    print("结论：tile 越多，每 tile 权重越少；激活广播一次可被所有 tile 复用，片外权重读取不再随输出通道线性增长。")


if __name__ == "__main__":
    main()
