# Circuit Notes

This file documents what is visible and what still needs verification in the EcoStep electronics.

## Confirmed from Photos

- The final prototype includes an external electronics module.
- A small digital voltage display module is visible.
- A green perfboard/prototyping board is visible.
- Red and black wires connect parts of the circuit.
- A capacitor is visible.
- A battery holder with two cylindrical rechargeable cells is visible.
- An LED strip is mounted near the electronics board.
- Build-stage photos show a multimeter and an oscilloscope-like instrument used during testing.

## Likely but Not Fully Verified

- The small black components on the perfboard appear to be discrete components and may include rectifier diodes.
- The capacitor may be used for smoothing or temporary storage.
- The LED strip may be a demonstration indicator rather than a direct harvested-energy load.
- The display may be powered by the battery holder rather than only by the PZT output.

## Recommended Circuit Documentation

Before making stronger claims, document:

1. PZT wiring topology: series, parallel, or grouped.
2. Whether the PZT output passes through a bridge rectifier.
3. Capacitor value and voltage rating.
4. Load resistor value used during each measurement.
5. Whether the battery is connected or disconnected during each test.
6. Where the multimeter or Arduino analog input is connected.

The current working topology label is documented in `hardware/wiring_topology.md` as:

```text
grouped_unknown
```

This label is used in `data/photo_informed_validation_estimates.csv` to avoid claiming an exact series/parallel connection before the wiring is physically traced.

## Measurement-Safe Wiring Path

A clean measurement setup should separate three paths:

```text
PZT array -> direct voltage measurement
PZT array -> rectifier -> capacitor charging test
PZT array -> known load resistor -> voltage logger
```

The demonstration module should be treated separately:

```text
Battery/display/LED module -> visual demonstration only unless isolated and verified
```

## Arduino Input Protection

Piezoelectric elements can produce short high-voltage spikes. If using Arduino:

- use a voltage divider
- add input protection diodes or a Zener clamp if available
- keep the analog input below the board limit
- record the divider ratio in the dataset
