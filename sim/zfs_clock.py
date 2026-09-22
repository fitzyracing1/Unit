from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
DATA = Path(__file__).resolve().parent.parent / "data" / "zfs_nominal.json"

@dataclass(frozen=True)
class ZFSClock:
    t_yz_mhz: float
    t_xy_mhz: float
    t_xz_mhz: float
    contrast: float
    linewidth_mhz: float
    t2_echo_us: float
    t2_cpmg_us: float
    @classmethod
    def nominal(cls) -> "ZFSClock":
        raw = json.loads(DATA.read_text())
        z = raw["zfs_MHz"]
        return cls(z["T_yz"], z["T_xy"], z["T_xz"], raw["odmr_contrast"], raw["linewidth_MHz"], raw["T2_echo_us"], raw["T2_cpmg_us"])
    def lines_mhz(self):
        return {"T_yz": self.t_yz_mhz, "T_xy": self.t_xy_mhz, "T_xz": self.t_xz_mhz}
    def lorentzian(self, f_mhz, line_mhz):
        h = self.linewidth_mhz / 2.0
        return (h**2) / ((f_mhz - line_mhz) ** 2 + h**2)

def clock_report(clock=None):
    c = clock or ZFSClock.nominal()
    lines = "\n".join(f"  {k:6s}  {v:8.1f} MHz" for k, v in c.lines_mhz().items())
    return f"Pentacene ZFS clock (nominal, 300 K)\n{lines}\n  contrast {c.contrast:.3f}  linewidth {c.linewidth_mhz:.1f} MHz\n  T2 echo {c.t2_echo_us:.1f} us  CPMG {c.t2_cpmg_us:.1f} us"
