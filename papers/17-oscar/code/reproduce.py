"""Reproduction skeleton (original, not the original authors' code): OSCAR-style configuration-driven accelerator generation.

Python standard library only. Demonstrates: given a hardware configuration, generate the corresponding
PE count, on-chip memory magnitude, and power estimate, and validate the configuration.
Run: python3 reproduce.py
"""


def generate(config):
    rows, cols = config["array"]
    assert rows > 0 and cols > 0, "Array size must be positive"
    assert config["style"] in ("systolic", "reconfigurable", "winograd", "dense"), "Unknown architecture style"
    pes = rows * cols
    sram_kb = config["sram_kb"]
    # Power-estimate sketch: linear model of PE power + SRAM power (coefficients are illustrative only, not the paper's fitted values)
    power_w = pes * 0.002 + sram_kb * 0.0005
    return {"pes": pes, "sram_kb": sram_kb, "power_w_est": round(power_w, 3),
            "rtl": f"{config['style']}_{rows}x{cols}.scala (illustrative file name)"}


def main():
    cfg = {"array": (16, 16), "sram_kb": 512, "style": "systolic"}
    out = generate(cfg)
    print("Input configuration:", cfg)
    print("Generated result:", out)
    assert out["pes"] == 256
    cfg2 = dict(cfg, array=(32, 32))
    out2 = generate(cfg2)
    print("After doubling the array:", out2)
    assert out2["power_w_est"] > out["power_w_est"]
    print("Point: a generator's value is that when the configuration changes, the RTL and power estimate change with it — design-space exploration needs no hand-written RTL or synthesis run each time.")


if __name__ == "__main__":
    main()
