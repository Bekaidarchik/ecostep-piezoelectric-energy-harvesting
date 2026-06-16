# PZT Wiring Topology

## Current Status

The exact electrical topology of the 16 PZT elements is **not fully confirmed** from the available photos. The photos clearly show multiple wired PZT discs on a marked wooden layout, but they do not show a complete traceable final connection path for every element.

## Confirmed

- The prototype uses 16 PZT elements.
- The intended layout is a 4 x 4 array.
- Red and black leads are visible on many PZT discs.
- The wiring appears to route toward the electronics/measurement section.

## Working Assumption Used for Estimates

For the photo-informed validation estimates, the repository uses:

```text
wiring_assumption = grouped_unknown
```

This means the estimates assume the 16 PZT elements behave like a grouped array, but do not claim a specific series or parallel topology.

## Why Not Claim an Exact Topology Yet?

Series and parallel wiring affect voltage, current, impedance, and energy transfer. Claiming the wrong topology would make the energy estimates misleading.

Examples:

- Series wiring can increase voltage but may limit current.
- Parallel wiring can increase current capacity but may lower voltage.
- Grouped wiring can balance voltage and current depending on the load.

## Recommended Final Documentation Step

To complete the real hardware documentation, trace the wires and create one of these:

```text
Option A: 16 PZTs in parallel
Option B: 16 PZTs in series
Option C: 4 series strings connected in parallel
Option D: 4 parallel groups connected in series
Option E: other grouped topology
```

After the topology is confirmed, update:

- `figures/pzt_array_layout.svg`
- `figures/system_architecture.svg`
- `data/photo_informed_validation_estimates.csv`
- `hardware/circuit_notes.md`
