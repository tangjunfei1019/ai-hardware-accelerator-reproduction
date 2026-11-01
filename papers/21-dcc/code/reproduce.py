"""Reproduction skeleton (original, not the original authors' code): DCC's core idea — data layout determines PIM gain.
Python standard library only. Demonstrates: for the same matrix tiling, host-contiguous layout and
PIM-local bank layout have different rearrangement costs; aligning the tiling strategy with
compute loop tiling reduces rearrangement.
Run: python3 reproduce.py
"""
def rearrangement_cost(rows, banks, layout):
    # layout='host': contiguous elements span banks, so rearrangement is needed before PIM compute; 'pim': contiguous elements already sit in the local bank
    if layout == 'host':
        return rows * (banks - 1)
    return rows // banks

def main():
    rows, banks = 1024, 8
    host = rearrangement_cost(rows, banks, 'host')
    pim = rearrangement_cost(rows, banks, 'pim')
    print('Host-layout rearrangement cost (relative units):', host)
    print('PIM-local-layout rearrangement cost (relative units):', pim)
    print('Reduction after alignment: %.2f' % (host / max(pim, 1)))
    print('Point: DCC does not optimize compute alone — it maps data tiling to compute loop tiling, jointly optimizing rearrangement and compute.')

if __name__ == '__main__':
    main()
