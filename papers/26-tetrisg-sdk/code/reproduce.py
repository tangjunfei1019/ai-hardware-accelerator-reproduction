"""Reproduction skeleton (original, not the original authors' code): adaptive windows raising CIM array utilization.
Python standard library only. Demonstrates: a fixed window leaves gaps when channel depth is not
divisible by the window, while an adaptive window can fill the marginal space.
Run: python3 reproduce.py
"""
def util(channels, window):
    used = (channels // window) * window
    return used / channels

def main():
    ch = 90
    print('Fixed window 32 utilization: %.2f' % util(ch, 32))
    print('Adaptive window 45 utilization: %.2f' % util(ch, 45))
    print('Point: TetrisG-SDK\'s gain comes from window-shape search and grouping, not just from replicating convolution kernels more times.')

if __name__ == '__main__':
    main()
