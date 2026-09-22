from __future__ import annotations
import math
from dataclasses import dataclass
from .zfs_clock import ZFSClock

@dataclass
class IncomingTone:
    freq_mhz: float
    amplitude: float
    phase_rad: float = 0.0

def odmr_spectrum(clock, freqs_mhz, tone=None):
    out = []
    for f in freqs_mhz:
        dip = 0.0
        for line in clock.lines_mhz().values():
            dip += clock.contrast * clock.lorentzian(f, line)
        if tone is not None:
            dip += tone.amplitude * clock.contrast * clock.lorentzian(f, tone.freq_mhz)
        out.append(max(0.0, 1.0 - dip))
    return out

def ramsey_contrast(clock, field_phase_rad, tau_us=None, line="T_xz"):
    tau = clock.t2_echo_us / 2.0 if tau_us is None else tau_us
    decay = math.exp(-tau / clock.t2_echo_us)
    fringe = 0.5 * (1.0 + decay * math.cos(field_phase_rad))
    return clock.contrast * fringe

def photon_shot_snr(contrast, photons):
    return 0.0 if photons <= 0 else contrast * math.sqrt(photons)

def demo_sweep(clock=None):
    c = clock or ZFSClock.nominal()
    freqs = [50.0 + (1600.0 - 50.0) * i / 399 for i in range(400)]
    quiet = odmr_spectrum(c, freqs)
    driven = odmr_spectrum(c, freqs, IncomingTone(c.t_xz_mhz, 0.35))
    phases = [i * math.pi / 8 for i in range(17)]
    return {"freqs_mhz": freqs, "odmr_quiet": quiet, "odmr_driven": driven, "phases_rad": phases, "ramsey": [ramsey_contrast(c, p) for p in phases], "single_molecule_snr_10k": photon_shot_snr(c.contrast, 10000), "clock": c}
