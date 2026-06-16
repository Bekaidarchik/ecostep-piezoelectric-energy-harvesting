# Data Dictionary

## Shared Trial Columns

| Column | Unit / Type | Description |
| --- | --- | --- |
| `case_id` / `trial_id` | text | Unique identifier for an estimate case or measured trial |
| `date` | yyyy-mm-dd | Date of the measurement, when real trials are collected |
| `test_type` | category | Type of validation test |
| `array_mode` | category | Whether the row describes a single PZT or the 16-element array |
| `pzt_count` | count | Number of PZT elements represented |
| `wiring_assumption` | category | Wiring description, such as `single_disc` or `grouped_unknown` |
| `pzt_configuration` | text | Physical/electrical PZT setup used for a trial |
| `step_type` | category | Light, normal, strong, or mixed step condition |
| `load_resistance_ohm` | ohms | Known resistor value used for load testing |
| `capacitance_f` | farads | Known capacitor value used for capacitor charging tests |
| `initial_voltage_v` | volts | Capacitor voltage before the test |
| `final_voltage_v` | volts | Capacitor voltage after the test |
| `peak_voltage_v` | volts | Peak observed voltage |
| `pulse_duration_s` | seconds | Approximate pulse duration |
| `sampling_rate_hz` | Hz | Data logging rate, if voltage-time data is collected |
| `steps` | count | Number of steps used in an aggregate test |
| `estimated_energy_j` | joules | Estimated energy from the documented equation |
| `measurement_status` | category | Status used in raw/cleaned measurement templates |
| `evidence_status` | category | Status used in validation estimate rows |
| `notes` | text | Context, caveats, and assumptions |

## Test Types

| Value | Meaning |
| --- | --- |
| `open_circuit_voltage` | Voltage measured with no load; useful for signal presence, not energy delivery |
| `rectified_voltage` | Estimated or measured DC-side voltage after rectification |
| `capacitor_charging` | Energy estimated from capacitor voltage change |
| `load_resistor_test` | Energy estimated from voltage across a known resistor |
| `single_vs_array` | Comparison between one PZT element and the full array |
| `wiring_topology` | Documentation row for wiring assumptions |

## Equations

Resistor-load energy:

```text
P(t) = V(t)^2 / R
E = sum(P(t) * dt)
```

Rough peak estimate:

```text
E = (V_peak^2 / R) * pulse_duration
```

Capacitor charging:

```text
E = 0.5 * C * (V_final^2 - V_initial^2)
```
