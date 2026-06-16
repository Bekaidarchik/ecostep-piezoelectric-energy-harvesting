# EcoStep Reviewer Summary

## 30-Second Project Explanation

EcoStep is a physical piezoelectric footstep energy harvesting tile prototype. It uses 16 PZT piezoelectric elements arranged as a 4 x 4 array inside a layered wooden compression structure. When a person steps on the tile, the mechanical force compresses the structure and stresses the PZT elements, producing short voltage pulses that can be measured and analyzed.

## What I Built

- A real wooden/plywood footstep tile prototype
- A 16-element PZT array
- A mechanical compression and return structure using bolts, spacing, and visible springs
- A demonstration electronics module with display, perfboard, LED strip, capacitor, wiring, and battery holder
- Arduino voltage logging code for future repeatable trials
- Python analysis code for energy-estimation documentation
- Hardware documentation, photo analysis, diagrams, and measurement plan
- A photo-informed validation estimate package for open-circuit, rectified, capacitor, load, and single-vs-array cases

## Why It Matters

The project studies a practical Electrical and Computer Engineering question: how can mechanical energy from human motion be converted into measurable electrical output, conditioned by a circuit, stored or loaded, and analyzed with data?

It is a strong high school ECE project because it combines:

- sensor physics
- mechanical design
- circuits
- measurement planning
- embedded data logging
- Python analysis
- honest reporting of uncertainty

## What Is Verified

- The prototype physically exists and is photographed.
- The system uses 16 PZT elements in a 4 x 4 array.
- The mechanical structure uses layered wooden plates.
- Bolts/screws, spacing, springs, internal wiring, and a side electronics section are visible.
- Build-stage photos show layout, assembly, and measurement attempts.
- The repository includes simulated/photo-informed validation estimates clearly labeled as estimates.

## What Is Still Being Measured

- Exact energy per step
- Exact PZT wiring topology
- Repeatability across multiple steps
- Open-circuit voltage vs loaded voltage
- Capacitor charging performance
- Single PZT vs 16-element array comparison
- Whether any demo load can be powered only from harvested energy

## Honesty Note

The remembered estimate of about 0.4 J is treated only as a preliminary low-confidence estimate. The LED/display/battery module is documented as a demonstration electronics module unless future tests prove that it is powered by the PZT array.

The validation values in `data/photo_informed_validation_estimates.csv` are simulated/photo-informed estimates, not fabricated lab measurements.

## Why This Is Strong for Reviewers

EcoStep shows that the student can move beyond a software-only project into real engineering: building hardware, documenting constraints, identifying uncertain claims, planning controlled measurements, and preparing a reproducible GitHub portfolio. It is ambitious but still believable for a high school student because the repository clearly separates prototype evidence from future validation work.
