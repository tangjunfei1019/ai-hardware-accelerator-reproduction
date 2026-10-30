"""复现骨架（原创，非原文代码）：OSCAR 式配置驱动加速器生成。

只用 Python 标准库。演示：给出一份硬件配置，生成对应的
PE 数量、片上存储量级与功耗估计，并校验配置合法性。
运行：python3 reproduce.py
"""


def generate(config):
    rows, cols = config["array"]
    assert rows > 0 and cols > 0, "阵列规模必须为正"
    assert config["style"] in ("systolic", "reconfigurable", "winograd", "dense"), "未知架构风格"
    pes = rows * cols
    sram_kb = config["sram_kb"]
    # 功耗估计示意：PE 功耗 + SRAM 功耗的线性模型（系数仅为示意，非原文拟合值）
    power_w = pes * 0.002 + sram_kb * 0.0005
    return {"pes": pes, "sram_kb": sram_kb, "power_w_est": round(power_w, 3),
            "rtl": f"{config['style']}_{rows}x{cols}.scala（示意文件名）"}


def main():
    cfg = {"array": (16, 16), "sram_kb": 512, "style": "systolic"}
    out = generate(cfg)
    print("输入配置:", cfg)
    print("生成结果:", out)
    assert out["pes"] == 256
    cfg2 = dict(cfg, array=(32, 32))
    out2 = generate(cfg2)
    print("阵列翻倍后:", out2)
    assert out2["power_w_est"] > out["power_w_est"]
    print("要点：生成器的价值在于配置一改，RTL 与功耗估计一起跟着变——设计空间探索不需要每次都手写 RTL、跑综合。")


if __name__ == "__main__":
    main()
