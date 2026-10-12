# Pentacene Atom Receiver (repo: Unit)

This repo holds a concept and a sandbox simulation of a single-molecule quantum receiver and clock: one pentacene molecule in a p-terphenyl host acts as antenna, mixer and local oscillator. Per the README, it is "concept + sandbox simulation, not a fabricated lab result".

## Getting started

```bash
pip install -r requirements.txt   # numpy>=1.24
python sim/demo.py
```

## Files

| Path | Role |
|---|---|
| `sim/zfs_clock.py` | `ZFSClock` (zero-field-splitting lines, Lorentzian), `clock_report` |
| `sim/receiver.py` | `odmr_spectrum`, `ramsey_contrast`, `photon_shot_snr`, `demo_sweep` |
| `sim/demo.py` | runs the demo |
| `data/zfs_nominal.json` | nominal parameters |
| `WHITEPAPER.md`, `docs/index.html`, `docs/whitepaper.md` | white paper (also the website) |
| `CONCEPT.md`, `BOM.yaml` | concept notes and bill of materials |

The README links a PDF (`docs/pentacene-receiver-whitepaper.pdf`) that is not in the repo, and a Pages URL under the name `pentacene-atom-receiver`. The repo has no tests and no CI.

MIT License. Copyright (c) 2026 Joshua Almeida
