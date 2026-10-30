"""复现骨架（原创，非原文代码）：自适应窗口提升 CIM 阵列利用率。
只用 Python 标准库。演示：固定窗口在通道深度不整除时留空，自适应窗口可填满边际空间。
运行：python3 reproduce.py
"""
def util(channels, window):
    used = (channels // window) * window
    return used / channels

def main():
    ch = 90
    print('固定窗口 32 利用率: %.2f' % util(ch, 32))
    print('自适应窗口 45 利用率: %.2f' % util(ch, 45))
    print('要点：TetrisG-SDK 的收益来自窗口形状搜索与分组，而不只是把卷积核复制更多份。')

if __name__ == '__main__':
    main()
