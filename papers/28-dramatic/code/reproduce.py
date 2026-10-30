"""复现骨架（原创，非原文代码）：RNS 的思想——大整数拆为小模数余数分别运算。
只用 Python 标准库。演示：用中国剩余定理把余数还原，验证乘法在余数域的等价性。
运行：python3 reproduce.py
"""
def crt(rems, mods):
    M = 1
    for m in mods:
        M *= m
    x = 0
    for r, m in zip(rems, mods):
        Mi = M // m
        inv = pow(Mi, -1, m)
        x += r * Mi * inv
    return x % M

def main():
    a, b = 123, 456
    mods = [97, 89, 83]
    ra = [a % m for m in mods]
    rb = [b % m for m in mods]
    rc = [(x * y) % m for x, y, m in zip(ra, rb, mods)]
    print('直接乘法:', a * b)
    print('RNS 还原:', crt(rc, mods))
    print('要点：DRAMatic 用 RNS/NTT 绕开 DPU 的弱乘法与通信瓶颈，骨架只演示数论思想，不含 DPU 代码。')

if __name__ == '__main__':
    main()
