# A Single-Molecule Pentacene Receiver with an On-Molecule Clock

**White paper v0.1**  
21 September 2026  
Organic Spin Processor / pentacene-atom-receiver  
Conceptual architecture. Simulation supported. Not a fabricated laboratory result.

## Abstract

A radio receiver does not need a metal antenna whose size tracks wavelength. It needs a dipole that couples to the field, a local oscillator that holds phase, and a readout that converts that phase into a countable signal. A single pentacene molecule in a *p*-terphenyl host already contains all three.

Photoexcitation creates a spin-1 triplet. The zero-field splitting of that triplet is a molecular clock, with room-temperature lines near 108 MHz, 1.34 GHz, and 1.45 GHz. An incoming microwave or radio-frequency field shifts or phases those lines. ODMR turns the shift into fluorescence contrast. The same Hamiltonian that senses the field is the frequency reference. The physical aperture is the molecule.

## 1. Problem

Classical receiving antennas are bound by electrical size. Atomic and molecular sensors invert the scaling. Rydberg vapor cells already demonstrate RF reception with optical readout. They remain ensemble devices in a glass cell.

The question: can the receiver shrink to **one molecule**, and can that molecule also be the **clock**?

Pentacene in *p*-terphenyl is the historic single-molecule fluorescence system, a room-temperature triplet ODMR platform, and the guest-host pair for an Organic Spin Processor: microwave write, independent optical read.

## 2. The molecule as transducer and clock

Zero-field triplet:

    H0 = D (Sz^2 - S(S+1)/3) + E (Sx^2 - Sy^2)

Nominal room-temperature lines used as design values:

| Line | Frequency |
|------|-----------|
| Tyz | ~108 MHz |
| Txy | ~1.340 GHz |
| Txz | ~1.448 GHz |

Incoming field: H(t) = H0 + mu · B(t)

On resonance: Rabi / Autler-Townes. Off resonance: Ramsey phase. Optical pump (532 nm) initializes T1. Fluorescence is the IF. No analog mixer, no LNA, no antenna larger than the molecule.

Clock modes on the same spin: frequency lock to a ZFS line; Ramsey phase mixer; echo / CPMG coherent integration (T2 echo ~2.7 us, CPMG ~18 us published-scale).

## 3. Why pentacene, not Rydberg

Rydberg receivers are excellent ensemble vapor-cell instruments. This paper is the solid-state single-molecule path at room temperature, aligned with the Organic Spin Processor.

## 4. Receive chain

532 nm pump → T1 → choose ZFS line (clock) → incoming RF/microwave → contrast or Ramsey phase → photon counts → baseband.

## 5. Limits

Triplet lifetime caps coherent tau. One molecule is shot-noise limited. D and E move with T and P. This paper does not report a new measured BER. Numbers are published-scale design inputs.

## 6. Bench path

P0 ensemble CW ODMR on Txz. P1 Rabi + Hahn echo. P2 Ramsey mixer curve. P3 confocal single molecule.

P2 is the receiver proof. P3 is the shrink.

## 7. Organic Spin Processor

Microwave write, optical read. The receiver is the same split in the opposite direction.

## 8. Conclusion

Shrink the receiver to one pentacene. Keep the clock on the same triplet. Use fluorescence as the IF.

v0.1 — 21 September 2026 — fitzyracing1 / pentacene-atom-receiver
