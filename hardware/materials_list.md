# Materials List

This list is based on the prototype photos plus the confirmed note that EcoStep uses 16 PZT piezoelectric elements arranged as a 4 x 4 array.

## Confirmed Components

These components are visible in photos or confirmed by the project owner.

| Component | Purpose | Evidence |
| --- | --- | --- |
| 16 PZT piezoelectric elements | Convert mechanical stress from footsteps into voltage pulses | Confirmed by user and visible in build photos |
| 4 x 4 PZT array | Increases active harvesting/sensing area compared with one disc | Confirmed by user |
| Wooden or plywood plates | Form the layered tile structure | Visible |
| Top footstep surface | Receives foot pressure | Visible |
| Two foot-placement markers | Show intended stepping zones | Visible |
| Bolts/screws | Fasten layers and likely guide compression | Visible |
| Springs | Likely return the compressed tile after stepping | Visible |
| Red/black wires | Connect PZT elements and circuit sections | Visible |
| Digital voltage display module | Displays voltage in the demonstration module | Visible |
| Green perfboard/prototyping board | Holds electronic components and wiring | Visible |
| Capacitor | Likely smoothing or temporary storage component | Visible |
| LED strip | Demonstration indicator | Visible |
| Battery holder with two cylindrical cells | Powers or supports the demonstration module | Visible |
| Multimeter | Measurement tool used during build/testing | Visible |

## Likely Components

These appear in photos but should be verified before being treated as final circuit facts.

| Component | Possible purpose | Evidence level |
| --- | --- | --- |
| Rectifier diodes | Convert PZT AC-like pulses into DC | Likely, exact circuit not verified |
| Load or protection resistors | Measurement/protection for display or circuit | Possible |
| Adhesive or hot glue | Holds wires and PZT discs in place | Visible adhesive, exact type unknown |
| Handheld oscilloscope-like tester | Observe short PZT pulses | Visible in bench setup |

## Recommended Components for Next Version

These components would make the next measurement phase stronger and more defensible.

| Component | Why it helps |
| --- | --- |
| Known load resistors: 1 kOhm, 10 kOhm, 100 kOhm | Enables repeatable load testing and `P = V^2 / R` calculations |
| Bridge rectifier or four matched diodes | Converts PZT pulses into DC for capacitor charging tests |
| Known capacitor values: 100 uF, 470 uF, 1000 uF | Enables energy calculation using `E = 0.5 C V^2` |
| Arduino or ESP32 | Logs voltage over time instead of relying on peak visual readings |
| Voltage divider and input protection | Protects microcontroller analog input from high PZT voltage spikes |
| Screw terminals | Makes wiring easier to document and less fragile |
| Strain relief for wires | Reduces wire breakage under repeated steps |
| Transparent cover or labeled internal photo | Helps reviewers understand the PZT array layout |

## Documentation Note

The battery holder, LED strip, and voltage display are useful for demonstrating the system, but they should not be described as powered by the PZT array until a controlled test proves that claim.
