# Prototype Photo Analysis

This file documents visual observations from all prototype photos currently stored in `hardware/prototype_photos/`. It separates confirmed observations from assumptions so the project remains impressive without overstating the evidence.

## Photo Set Reviewed

The folder contains final prototype photos from `20-00-06` and build/test photos from `20-05-13`.

Key files:

| Photo | What it shows |
| --- | --- |
| `photo_1_2026-06-16_20-00-06.jpg` | Full tile with two footprint markers and external electronics module |
| `photo_4_2026-06-16_20-00-06.jpg` | Close-up of display, perfboard, battery holder, LED strip, and wiring |
| `photo_5_2026-06-16_20-00-06.jpg` to `photo_7_2026-06-16_20-00-06.jpg` | Side/internal views of layered structure, wires, fasteners, and spring/bolt mechanism |
| `photo_1_2026-06-16_20-05-13.jpg` to `photo_5_2026-06-16_20-05-13.jpg` | Build-stage layout, PZT placement, measuring, and marking on plywood |
| `photo_6_2026-06-16_20-05-13.jpg` and `photo_7_2026-06-16_20-05-13.jpg` | Multimeter measurement attempt during loading/stepping |
| `photo_8_2026-06-16_20-05-13.jpg` and `photo_9_2026-06-16_20-05-13.jpg` | Close-up of the PZT discs on the wooden layout |
| `photo_10_2026-06-16_20-05-13.jpg` | Bench setup with a PZT disc, oscilloscope-like test instrument, multimeter, battery cell, and sketched circuit notes |

## Confirmed Visual Observations

### Mechanical Structure

- The prototype is a physical tile made from wooden or plywood sheets.
- The final top surface has two foot-shaped placement markers.
- The build photos show drawn layout lines on the wooden sheet before final assembly.
- The side photos show spacing between layers, suggesting that the top plate can move under load.
- Bolts/screws are visible around the tile and side structure.
- Springs are visible near the side mechanism, suggesting a return mechanism after compression.
- The final prototype includes a side-mounted electronics section.

### PZT Array

- The user confirmed the prototype uses 16 PZT piezoelectric elements arranged as a 4 x 4 array.
- Build-stage photos show many circular brass/white PZT discs with red and black wires.
- Several PZT discs are visibly placed on a marked wooden layout.
- The close-up build photos show solder joints or attached leads on the PZT discs.

### Electronics and Test Equipment

- A small digital voltage display is visible on the final electronics module.
- A green perfboard/prototyping board is visible in the final electronics module.
- Red and black wires connect parts of the module.
- A capacitor is visible on the electronics module.
- Several small black components on the perfboard appear to be discrete components; they may be diodes, but this is not fully confirmed from the photo alone.
- An LED strip is mounted next to the electronics board and appears lit in at least one photo.
- A battery holder with two cylindrical rechargeable cells is visible.
- A handheld multimeter is visible in multiple build/test photos.
- One photo shows a multimeter display around `3.46` during a foot/loading test, but the mode, wiring, and exact trial conditions are not fully documented.
- One bench photo shows an oscilloscope-like handheld instrument connected near a PZT disc.

## Reasonable Assumptions

These points are likely, but should not be written as final verified facts until the circuit is mapped:

- The black components on the perfboard may be rectifier diodes.
- The capacitor may be used for smoothing or short-term energy storage.
- The LED strip may be a visual demonstration indicator.
- The display module may be used to show voltage from the electronics module.
- The PZT elements may be wired in groups, but the exact series/parallel configuration is not visible enough to confirm.

## Important Honesty Notes

- The visible battery holder means the LED/display module may be separately powered.
- The repository should not claim that the PZT array directly supplies power to the LED strip, display, or battery pack unless a controlled test proves it.
- The remembered `0.4 J` value should remain labeled as a preliminary remembered estimate.
- The visible multimeter reading should be described as evidence that measurement attempts were made, not as final validated data.
- A final energy claim requires voltage-time data, known load resistance, or a capacitor charging test with known capacitance.

## Engineering Strengths Shown by the Photos

- Real physical build, not only a simulation.
- Multi-element PZT array rather than a single sensor demonstration.
- Mechanical compression structure with visible spacing and return hardware.
- Build process documented through layout, measuring, wiring, and testing photos.
- Electrical testing tools appear in the workflow.
- The project naturally connects mechanical design, circuits, sensors, data logging, and Python analysis.

## Next Photos or Evidence to Add

1. A labeled wiring diagram for the 16 PZT elements.
2. A photo showing the exact final PZT wiring before the tile is closed.
3. A measurement video or voltage-time data file from a controlled step.
4. A close-up showing whether the perfboard uses a bridge rectifier, single diode, capacitor, or other conditioning circuit.
5. A table of load resistance, peak voltage, pulse duration, and estimated energy for repeated trials.
