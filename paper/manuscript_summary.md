# EcoStep Manuscript Summary

## Title

EcoStep: A 16-Element PZT Footstep Energy Harvesting Tile Prototype

## Abstract

EcoStep is a physical piezoelectric footstep energy harvesting prototype built around a 4 x 4 array of 16 PZT piezoelectric elements. The prototype uses a layered wooden tile structure with visible bolts, springs, and spacing between layers, allowing foot pressure to mechanically compress the internal PZT array. The project includes an external demonstration electronics module with a visible voltage display, perfboard, capacitor, LED strip, and battery holder. Because the historical measurement dataset was not saved, the current repository treats the remembered value of approximately 0.4 J as a preliminary low-confidence estimate rather than a final experimental result. To make the project reviewable, the repository includes a photo-informed validation estimate package covering open-circuit voltage, rectified voltage, capacitor charging, load-resistor behavior, and single-PZT vs 16-element-array comparison. These estimates are clearly labeled as simulated/photo-informed, not final laboratory data.

## Engineering Method

The prototype investigates the following chain:

```text
footstep force -> mechanical compression -> PZT voltage pulse -> conditioning/measurement -> energy estimate
```

The 16 PZT elements increase the active sensing area compared with a single disc, but the exact wiring topology still needs to be mapped. Future testing should compare one PZT element with the full 16-element array under the same load conditions.

## Current Evidence

Verified:

- physical prototype exists
- 16 PZT elements are used in a 4 x 4 array
- wooden/plywood compression structure is visible
- springs, bolts, wiring, and electronics module are visible
- build-stage photos show layout, assembly, and measurement attempts

Not yet verified:

- final energy per step
- exact PZT series/parallel wiring
- whether the LED/display module is powered by harvested energy
- repeatability across multiple step trials

Portfolio validation now included:

- photo-informed open-circuit voltage estimates
- photo-informed rectified voltage estimates
- modeled capacitor charging estimates
- modeled load-resistor energy estimates
- single PZT vs 16-element array estimate
- conservative wiring label: `grouped_unknown`

## Planned Energy Calculations

For a resistor load:

```text
P(t) = V(t)^2 / R
E = sum(P(t) * dt)
```

For capacitor charging:

```text
E = 0.5 * C * (V_final^2 - V_initial^2)
```

## Future Work

- Map the exact PZT wiring topology.
- Measure open-circuit and rectified voltage.
- Run capacitor charging tests with known capacitance.
- Run load tests with known resistors.
- Compare single PZT and full 16-element array output.
- Generate voltage-time and energy-per-step graphs.
