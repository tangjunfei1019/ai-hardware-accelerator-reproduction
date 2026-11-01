"""Reproduction skeleton (original, not the original authors' code): the idea of bulk bit operations inside a DRAM subarray.
Python standard library only. Demonstrates: two bit vectors AND/OR inside the same subarray, in an
abstract model without moving data through a CPU ALU.
Run: python3 reproduce.py
"""
def main():
    a = 0b11010110
    b = 0b10101100
    print('A      :', format(a, '08b'))
    print('B      :', format(b, '08b'))
    print('In-subarray AND:', format(a & b, '08b'))
    print('In-subarray OR :', format(a | b, '08b'))
    print('Point: gem5-CIMD\'s key contribution is not these two bit operations themselves, but the complete simulation of operand co-location, the instruction set, and the memory-management stack.')

if __name__ == '__main__':
    main()
