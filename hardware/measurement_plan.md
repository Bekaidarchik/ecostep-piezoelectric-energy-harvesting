# Measurement Plan

The prototype has been built and photographed, but a clean historical dataset was not saved. This plan defines how to move from prototype documentation to defensible electrical measurements.

The repository also includes a photo-informed estimate file:

```text
data/photo_informed_validation_estimates.csv
```

Those rows are useful for portfolio completeness and analysis demonstrations, but they are not final laboratory measurements.

## Goal

Measure the voltage and estimated energy produced by the 16-element PZT footstep tile under repeatable test conditions, while keeping the battery-powered demonstration module separate from the actual energy-harvesting measurements.

## Safety and Honesty Rules

- Do not connect unknown high-voltage PZT spikes directly to a microcontroller analog pin without a voltage divider or protection circuit.
- Do not claim that the tile powers the LED strip, display, or batteries unless the battery is disconnected and the measurement proves it.
- Record the circuit configuration for every trial.
- Keep the preliminary remembered `0.4 J` estimate separate from measured results.
- Use known component values: load resistance, capacitance, sampling rate, and wiring configuration.

## Test 1: Open-Circuit Voltage

Purpose: measure the maximum voltage pulse from the PZT array without a load.

Procedure:

1. Disconnect the LED/display/battery demonstration module from the PZT measurement output.
2. Connect a multimeter or oscilloscope across the PZT output.
3. Perform repeated light, normal, and strong steps.
4. Record peak voltage and whether the value is from a multimeter or oscilloscope.

Limit: open-circuit voltage does not directly give usable energy, because almost no current is delivered.

## Test 2: Rectified Voltage

Purpose: measure the DC output after rectification.

Procedure:

1. Connect the PZT array to a bridge rectifier or verified diode circuit.
2. Measure rectified voltage across the DC output.
3. Record peak and average voltage during repeated steps.
4. Compare direct PZT output with rectified output.

## Test 3: Capacitor Charging

Purpose: estimate harvested energy stored in a capacitor.

Procedure:

1. Use a known capacitor value, such as 100 uF, 470 uF, or 1000 uF.
2. Measure initial capacitor voltage before stepping.
3. Apply a fixed number of steps, such as 10, 25, and 50.
4. Measure final capacitor voltage.
5. Calculate stored energy:

```text
E = 0.5 * C * (V_final^2 - V_initial^2)
```

Where:

- `E` is energy in joules
- `C` is capacitance in farads
- `V_final` is capacitor voltage after stepping
- `V_initial` is capacitor voltage before stepping

## Test 4: Load Test with Resistor

Purpose: estimate electrical energy delivered to a known load.

Procedure:

1. Connect a known resistor across the output.
2. Log voltage over time during each step.
3. Repeat with several resistor values, such as 1 kOhm, 10 kOhm, and 100 kOhm.
4. Calculate instantaneous power and integrate over time:

```text
P(t) = V(t)^2 / R
E = sum(P(t) * dt)
```

This is stronger than using only peak voltage because it uses the full pulse shape.

## Test 5: Repeated Step Trials

For each circuit configuration, collect repeated trials:

| Step type | Number of trials | Notes |
| --- | --- | --- |
| light | at least 10 | gentle step or press |
| normal | at least 10 | normal walking force |
| strong | at least 10 | firm step, without damaging the tile |

Record:

```text
trial_id,date,test_type,pzt_configuration,step_type,load_resistance_ohm,
capacitance_f,initial_voltage_v,final_voltage_v,peak_voltage_v,
pulse_duration_s,sampling_rate_hz,estimated_energy_j,measurement_status,notes
```

## Test 6: Single PZT vs 16-Element Array

Purpose: show why the multi-element array matters.

Procedure:

1. Measure one PZT disc using the same step or press setup.
2. Measure the full 16-element array under similar loading.
3. Compare peak voltage, stored capacitor energy, and delivered load energy.

Avoid claiming perfect 16x improvement. Real outputs depend on wiring, force distribution, contact quality, and internal impedance.

## Graphs to Generate

- voltage vs time for representative steps
- peak voltage by step type
- capacitor voltage vs number of steps
- estimated energy per step
- single PZT vs 16-element array comparison
- energy delivered across different load resistances

## Minimum Evidence Needed for a Strong Claim

A strong energy claim should include:

1. circuit diagram
2. known load resistance or known capacitor
3. repeated trials
4. voltage-time data or capacitor start/end voltage
5. calculation method
6. uncertainty or limitations

Until then, the current `0.4 J` value should remain a preliminary remembered estimate.

## Current Estimate Coverage

The current validation estimate package covers:

- open-circuit voltage estimates
- rectified voltage estimates
- capacitor charging estimates
- load-resistor estimates
- single PZT vs 16-element array comparison
- unresolved wiring topology labeled as `grouped_unknown`

See `docs/validation_report.md` for the current values and assumptions.
