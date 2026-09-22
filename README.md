# Pentacene Atom Receiver

Single-molecule quantum receiver + clock.

Not Rydberg. One pentacene molecule in a *p*-terphenyl host is the antenna, the mixer, and the local oscillator.

Physical aperture = one molecule. Clock = the same triplet Hamiltonian.

## Website

White paper is the site.

- HTML: `docs/index.html`
- Markdown: `WHITEPAPER.md`
- PDF: `docs/pentacene-receiver-whitepaper.pdf`

GitHub Pages (Settings → Pages → Deploy from branch `main`, folder `/docs`):

https://fitzyracing1.github.io/pentacene-atom-receiver/

Repo: https://github.com/fitzyracing1/pentacene-atom-receiver

## Why this molecule

- Photoexcited pentacene triplet in *p*-terphenyl is a room-temperature ODMR system.
- Zero-field splittings sit near **108 MHz**, **1.34 GHz**, **1.45 GHz**.
- Published room-temperature ODMR contrast ~17 %.
- Echo *T2* ~ 2.7 us; CPMG *T2* ~ 18 us.
- Same host/guest system that first isolated single-molecule fluorescence.

## Run the sim

```bash
pip install -r requirements.txt
python sim/demo.py
```

## Status

Concept + sandbox simulation. Not a fabricated lab result.

Related: Organic Spin Processor (Hardware-Prototype-Tracker #5).
