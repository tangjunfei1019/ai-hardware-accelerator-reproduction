"""复现骨架（原创，非原文代码）：MTIA 300 式通信卸载与重叠。

只用 Python 标准库。演示：计算核兼做通信时通信串行占用计算时间；
专用消息引擎卸载后，通信与计算可重叠，总时间趋近两者最大值而非之和。
运行：python3 reproduce.py
"""


def total_time(compute, comm, overlap):
    """overlap 为 0~1：可与计算重叠的通信比例。"""
    return compute + comm * (1.0 - overlap)


def main():
    compute, comm = 100.0, 60.0
    serial = total_time(compute, comm, 0.0)
    offloaded = total_time(compute, comm, 0.9)
    print(f"计算时间 {compute}，通信时间 {comm}")
    print(f"串行（计算核兼做通信）总时间: {serial}")
    print(f"卸载+重叠 90% 后总时间: {offloaded:.1f}，加速约 {serial / offloaded:.2f} 倍")
    assert offloaded < serial
    print("要点：MTIA 300 的收益不在单卡峰值算力，而在把通信从计算关键路径上拿掉——"
          "12 个内置网卡 + 16 个消息引擎就是为这个目标服务的。")


if __name__ == "__main__":
    main()
