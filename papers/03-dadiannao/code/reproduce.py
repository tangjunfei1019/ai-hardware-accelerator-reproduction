"""Reproduction skeleton (original, not the paper's code): DaDianNao-style
multi-tile partitioning and broadcast accounting.

Uses only the Python standard library. Demonstrates: when output channels are
split across multiple tiles, weights become local and activations are broadcast.
Run: python3 reproduce.py
"""


def model(tiles, out_channels, in_channels):
    """Returns per-tile local weight count, broadcast activation count, and MACs per tile."""
    per_tile_out = out_channels // tiles
    weight_local = per_tile_out * in_channels  # Each tile stores only its own weights
    act_broadcast = in_channels  # Activations are broadcast to all tiles (counted once as a broadcast)
    macs_per_tile = per_tile_out * in_channels
    return weight_local, act_broadcast, macs_per_tile


def main():
    for tiles in (1, 2, 4, 8):
        w, a, m = model(tiles, out_channels=256, in_channels=256)
        print(f"tiles={tiles}  weights per tile={w}  broadcast activations={a}  MACs per tile={m}")
    print("Conclusion: more tiles means fewer weights per tile; one activation broadcast can be reused by all tiles, so off-chip weight reads no longer grow linearly with output channels.")


if __name__ == "__main__":
    main()
