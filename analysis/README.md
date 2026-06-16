# Analysis README

This folder contains the Python analysis workflow for EcoStep.

## What the Script Does

`energy_estimation.py`:

- reads `data/preliminary_estimate.csv`
- reads `data/photo_informed_validation_estimates.csv`
- checks `data/raw_measurements.csv` and `data/cleaned_measurements.csv`
- ignores placeholder/template rows
- creates `analysis/analysis_summary.txt`
- creates `figures/preliminary_energy_estimate.svg`
- creates `figures/validation_estimate_summary.svg`
- keeps the remembered `0.4 J` value separate from measured results
- keeps simulated/photo-informed estimates separate from real measurements

## How to Run

From the project root:

```bash
python analysis/energy_estimation.py
```

## How to Add Real Measurements

Replace the placeholder row in `data/raw_measurements.csv` with real trials.

Minimum useful fields:

```text
trial_id,test_type,pzt_configuration,step_type,load_resistance_ohm,
capacitance_f,initial_voltage_v,final_voltage_v,peak_voltage_v,
pulse_duration_s,sampling_rate_hz,estimated_energy_j,measurement_status,notes
```

Use `measurement_status=measured` only after the values come from a real controlled test.

## Photo-Informed Estimate Rows

`data/photo_informed_validation_estimates.csv` contains realistic engineering estimates based on the prototype photos, the 16-element PZT array, and the visible testing setup.

These rows use:

```text
evidence_status=simulated_photo_informed
```

They are useful for portfolio completeness and analysis demonstrations, but they are not final lab measurements.

## Energy Equations

For a known load resistor:

```text
P(t) = V(t)^2 / R
E = sum(P(t) * dt)
```

For a capacitor charging test:

```text
E = 0.5 * C * (V_final^2 - V_initial^2)
```
