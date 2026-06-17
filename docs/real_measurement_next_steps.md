# Real Measurement Next Steps

This checklist turns EcoStep from a photo-informed validation repository into a stronger measured engineering portfolio project.

## Goal

Replace simulated/photo-informed estimates with controlled voltage-time measurements from the physical piezoelectric tile.

## Evidence to Capture

- Photos of the full test setup, including tile, wiring, measurement device, load resistor or capacitor, and footstep/load method.
- Raw voltage-time readings from an oscilloscope, serial logger, or microcontroller ADC path.
- Known component values for each trial, including load resistor value, capacitor value, rectifier stage, and wiring topology.
- Repeated trials for light, normal, and strong steps.
- A single-PZT baseline trial and a full 16-element array trial under similar conditions.
- Notes on trial conditions: person/load, step style, surface, sampling rate, circuit configuration, and date.

## Minimum Dataset

Create or update these files:

```text
data/raw_measurements.csv
data/cleaned_measurements.csv
analysis/analysis_summary.txt
figures/voltage_pulse_real_trial.svg
figures/energy_per_step_real_trials.svg
hardware/prototype_photos/
```

Suggested raw CSV columns:

```text
trial_id,timestamp_s,voltage_v,load_resistance_ohm,capacitance_f,configuration,step_strength,measurement_status,notes
```

Use `measurement_status = measured` for real lab data. Keep simulated or photo-informed rows separated from measured rows.

## Analysis Targets

- Peak voltage by trial.
- Energy per step using `E = sum((V(t)^2 / R) * dt)` for load-resistor tests.
- Capacitor energy using `E = 0.5 * C * (V_final^2 - V_initial^2)` for capacitor tests.
- Comparison of single PZT vs 16-element array.
- Short explanation of losses and uncertainty.

## Portfolio Upgrade Criteria

The project becomes portfolio-strong when the README can say:

```text
Measured repeated footstep trials from the physical EcoStep tile, calculated energy per step from voltage-time data, and compared single-PZT output against the full 16-element array.
```
