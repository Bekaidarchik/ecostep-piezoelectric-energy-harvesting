# Data Package

This folder contains the EcoStep measurement and validation data files. It is organized so a reviewer can quickly tell the difference between real measurements, placeholders, and photo-informed estimates.

## Files

| File | Type | Purpose |
| --- | --- | --- |
| `preliminary_estimate.csv` | preliminary memory-based estimate | Stores the remembered `0.4 J` value as `not_measured` |
| `raw_measurements.csv` | real measurement template | Empty template for future raw voltage/load/capacitor trials |
| `cleaned_measurements.csv` | processed measurement template | Empty template for cleaned measured trials after raw data is collected |
| `photo_informed_validation_estimates.csv` | simulated/photo-informed validation estimates | Realistic engineering estimates based on prototype photos and assumptions |
| `ecostep_validation_workbook.xlsx` | Excel workbook | Human-friendly dashboard, validation tables, data dictionary, and notes |
| `data_dictionary.md` | metadata | Defines columns and allowed evidence statuses |

## Evidence Status Labels

| Status | Meaning |
| --- | --- |
| `measured` | Real controlled measurement from a documented test |
| `placeholder` | Template row only, not data |
| `not_measured` | A known value or estimate that is explicitly not a lab measurement |
| `simulated_photo_informed` | Realistic estimate based on photos and engineering assumptions |
| `inferred_from_photos` | Structural/circuit inference from images, not measured data |

## Reviewer Note

The repository is honest about data quality. The prototype is real and photographed, but final controlled voltage-time data has not yet been collected. The validation estimate file exists to make the analysis pipeline complete and reviewable without pretending that simulated values are laboratory measurements.
