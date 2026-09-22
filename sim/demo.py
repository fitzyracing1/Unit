#!/usr/bin/env python3
from __future__ import annotations
import math, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from sim.receiver import demo_sweep
from sim.zfs_clock import clock_report

def main():
    print(clock_report()); print()
    d = demo_sweep(); c = d["clock"]
    driven, quiet, freqs = d["odmr_driven"], d["odmr_quiet"], d["freqs_mhz"]
    i_min = min(range(len(driven)), key=lambda i: driven[i])
    print("CW ODMR (toy lineshape)")
    print(f"  quiet min fluorescence  {min(quiet):.3f}")
    print(f"  driven min @ {freqs[i_min]:.1f} MHz  fluorescence {driven[i_min]:.3f}")
    print(f"  extra dip from tone on T_xz ({c.t_xz_mhz:.1f} MHz)\n")
    print("Ramsey mixer (incoming phase -> contrast)")
    for phi, y in zip(d["phases_rad"], d["ramsey"]):
        bar = "#" * int(round(40 * y / max(d["ramsey"])))
        print(f"  phi={phi/math.pi:5.2f} pi   C={y:.4f}  {bar}")
    print(f"\nSingle-molecule shot SNR after 10k photons: {d['single_molecule_snr_10k']:.2f}")
    print("Antenna = one pentacene. Clock = same triplet.")

if __name__ == "__main__":
    main()
