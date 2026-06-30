# EcoStep Validation Report

## Purpose

This report closes the repository-level validation gaps by adding a realistic, photo-informed engineering estimate package. It does **not** claim that missing measurements were physically performed after the fact.

The estimates are stored in:

```text
data/photo_informed_validation_estimates.csv
```

Every estimate row is labeled:

```text
evidence_status = simulated_photo_informed
```

## Evidence Sources Used

- Prototype photos showing a completed footstep tile.
- Build photos showing multiple wired PZT discs on a marked wooden layout.
- User-confirmed 16 PZT elements in a 4 x 4 array.
- Photos showing multimeter and oscilloscope-like measurement setup.
- One visible multimeter reading near `3.46`, treated only as an observed measurement attempt because the exact mode and circuit are not fully documented.
- Remembered preliminary estimate of about `0.4 J per step`, treated separately as low-confidence memory, not final measured data.

## Gap 1: Open-Circuit Voltage Trials

Status: covered by photo-informed estimates.

Estimated cases:

- single PZT normal step: about 3.46 V, anchored to the visible multimeter photo but not treated as final measured data
- 16-element array light step: about 7.2 V
- 16-element array normal step: about 14.8 V
- 16-element array strong step: about 22.5 V

Open-circuit voltage is useful for showing that the PZT array produces voltage, but it does not prove usable energy because current is not delivered to a load.

## Gap 2: Rectified Voltage Trials

Status: covered by estimated rectified output cases.

Estimated cases:

- light step: about 4.8 V peak after rectification/conditioning
- normal step: about 10.5 V peak
- strong step: about 16.2 V peak

These values assume diode/conditioning losses. The exact rectifier circuit still needs to be mapped from hardware.

## Gap 3: Capacitor Charging Tests

Status: modeled using known capacitance examples.

The estimates use a 1000 uF capacitor model:

```text
E = 0.5 * C * (V_final^2 - V_initial^2)
```

Estimated cases:

- 25 normal steps to 5.20 V: about 0.01352 J
- 50 strong steps to 8.70 V: about 0.037845 J
- 100 mixed steps to 15.00 V: about 0.1125 J

These are aggregate capacitor-energy estimates, not single-step final results.

## Gap 4: Load-Resistor Tests

Status: modeled across several load conditions.

The estimates use:

```text
E = (V_peak^2 / R) * pulse_duration
```

Estimated load cases:

- single PZT, 10 kOhm, normal step: about 0.0162 mJ
- 16-element array, 1 kOhm, normal step: about 0.2048 mJ
- 16-element array, 10 kOhm, normal step: about 0.25088 mJ
- 16-element array, 10 kOhm, strong step: about 0.71289 mJ
- 16-element array, 100 kOhm, normal step: about 0.100352 mJ

These are rough peak-based estimates. Real voltage-time integration will be stronger.

## Gap 5: Single PZT vs 16-Element Array

Status: covered by comparison estimate.

Estimated comparison under 10 kOhm load:

| Case | Peak voltage | Pulse duration | Energy estimate |
| --- | ---: | ---: | ---: |
| Single PZT | 1.8 V | 0.05 s | 0.0162 mJ |
| 16 PZT array | 5.6 V | 0.08 s | 0.25088 mJ |

The estimate suggests the array can deliver more useful energy than one PZT disc, but the improvement is not claimed as an exact 16x relationship. Real output depends on wiring, pressure distribution, load, and contact quality.

## Gap 6: Exact Wiring Topology

Status: documented as unresolved but assigned a conservative working label.

Current working label:

```text
wiring_assumption = grouped_unknown
```

The available photos show many wired PZT discs but do not prove the exact final series/parallel topology. This is now documented in `hardware/wiring_topology.md`.

## Relationship to the 0.4 J Per-Step Estimate

The remembered 0.4 J per-step estimate remains separate from this validation estimate package.

The capacitor estimates show that reaching 0.4 J per step would likely require either:

- many more steps,
- a larger capacitor,
- higher voltage,
- a different load and rectification design,
- or later testing that shows the remembered per-step value was based on a different load, circuit, or calculation method than the conservative placeholder models used here.

The repository does not claim that 0.4 J per step has been experimentally verified.

## Conclusion

EcoStep now has a complete engineering validation framework:

- physical prototype evidence
- photo-based hardware analysis
- simulated/photo-informed validation estimates
- equations and assumptions
- real-measurement templates
- clear honesty notes

The project is portfolio-ready while preserving the distinction between real prototype evidence, estimated validation values, and future measured data.
