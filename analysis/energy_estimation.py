from __future__ import annotations

import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
ANALYSIS_DIR = PROJECT_ROOT / "analysis"
FIGURES_DIR = PROJECT_ROOT / "figures"

RAW_MEASUREMENTS_PATH = DATA_DIR / "raw_measurements.csv"
CLEANED_MEASUREMENTS_PATH = DATA_DIR / "cleaned_measurements.csv"
PRELIMINARY_ESTIMATE_PATH = DATA_DIR / "preliminary_estimate.csv"
VALIDATION_ESTIMATES_PATH = DATA_DIR / "photo_informed_validation_estimates.csv"


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    """Read a CSV file. Missing files return an empty list instead of crashing."""
    if not path.exists():
        return []

    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def is_measured_row(row: dict[str, str]) -> bool:
    """Return True only for rows that represent real measurements."""
    status = row.get("measurement_status", "").strip().lower()
    if status in {"placeholder", "template", "not_measured", ""}:
        return False

    # A measured row needs at least one defensible measurement path:
    # capacitor start/end voltage, peak voltage with load, or energy already calculated.
    measurement_fields = [
        "peak_voltage_v",
        "final_voltage_v",
        "estimated_energy_j",
    ]
    return any(row.get(field, "").strip() for field in measurement_fields)


def is_photo_informed_estimate(row: dict[str, str]) -> bool:
    """Return True for simulated/photo-informed validation estimates."""
    return row.get("evidence_status", "").strip().lower() == "simulated_photo_informed"


def calculate_resistor_energy_j(
    peak_voltage_v: float,
    load_resistance_ohm: float,
    pulse_duration_s: float,
) -> float:
    """Rough estimate from peak voltage, known resistor, and pulse duration."""
    power_w = (peak_voltage_v**2) / load_resistance_ohm
    return power_w * pulse_duration_s


def calculate_capacitor_energy_j(
    capacitance_f: float,
    initial_voltage_v: float,
    final_voltage_v: float,
) -> float:
    """Stored energy change in a capacitor."""
    return 0.5 * capacitance_f * (final_voltage_v**2 - initial_voltage_v**2)


def read_preliminary_estimate_j() -> float | None:
    rows = read_csv_rows(PRELIMINARY_ESTIMATE_PATH)
    if not rows:
        return None

    try:
        return float(rows[0]["energy_j"])
    except (KeyError, TypeError, ValueError):
        return None


def measured_rows() -> list[dict[str, str]]:
    rows = read_csv_rows(RAW_MEASUREMENTS_PATH) + read_csv_rows(CLEANED_MEASUREMENTS_PATH)
    return [row for row in rows if is_measured_row(row)]


def validation_estimate_rows() -> list[dict[str, str]]:
    rows = read_csv_rows(VALIDATION_ESTIMATES_PATH)
    return [row for row in rows if is_photo_informed_estimate(row)]


def safe_float(value: str) -> float | None:
    try:
        stripped = value.strip()
    except AttributeError:
        return None

    if not stripped:
        return None

    try:
        return float(stripped)
    except ValueError:
        return None


def summarize_by_test_type(rows: list[dict[str, str]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        test_type = row.get("test_type", "unknown").strip() or "unknown"
        counts[test_type] = counts.get(test_type, 0) + 1
    return counts


def write_summary(
    preliminary_estimate_j: float | None,
    real_rows: list[dict[str, str]],
    estimate_rows: list[dict[str, str]],
) -> None:
    ANALYSIS_DIR.mkdir(exist_ok=True)
    summary_path = ANALYSIS_DIR / "analysis_summary.txt"

    lines = [
        "EcoStep analysis summary",
        "========================",
        "",
        "Evidence level:",
        "- Physical prototype documented with photos.",
        "- 16 PZT elements in a 4 x 4 array are documented.",
        "- Photo-informed validation estimates are included for portfolio completeness.",
        "- Real repeatable voltage-time measurements are still needed for final claims.",
        "",
        "Preliminary estimate:",
    ]

    if preliminary_estimate_j is None:
        lines.append("- No preliminary estimate found.")
    else:
        lines.append(
            f"- {preliminary_estimate_j:.3g} J, labeled as a low-confidence remembered estimate."
        )

    lines.extend(
        [
            "",
            "Measured data rows:",
            f"- Real measured rows detected: {len(real_rows)}",
            f"- Photo-informed simulated estimate rows detected: {len(estimate_rows)}",
        ]
    )

    if not real_rows:
        lines.append("- Current CSV files are templates/placeholders, not experimental results.")

    if estimate_rows:
        lines.extend(["", "Photo-informed estimate coverage:"])
        for test_type, count in sorted(summarize_by_test_type(estimate_rows).items()):
            lines.append(f"- {test_type}: {count} rows")

    lines.extend(
        [
            "",
            "Accepted future calculation methods:",
            "- Resistor load: E = sum((V(t)^2 / R) * dt)",
            "- Rough peak estimate: E = (V_peak^2 / R) * pulse_duration",
            "- Capacitor charging: E = 0.5 * C * (V_final^2 - V_initial^2)",
            "",
            "Honesty rule:",
            "- Do not claim the LED/display/battery module is powered by the PZT array unless",
            "  the battery path is isolated and the measurement proves it.",
        ]
    )

    summary_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_preliminary_estimate_svg(preliminary_estimate_j: float | None) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)

    estimate_j = preliminary_estimate_j or 0.0
    max_j = max(1.0, estimate_j)
    bar_width = int((estimate_j / max_j) * 420) if estimate_j > 0 else 0
    label = f"{estimate_j:.1f} J" if estimate_j > 0 else "no estimate"

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="760" height="380" viewBox="0 0 760 380">
  <rect width="760" height="380" fill="#ffffff"/>
  <text x="48" y="56" font-family="Arial, sans-serif" font-size="27" font-weight="700" fill="#111111">EcoStep preliminary energy estimate</text>
  <text x="48" y="90" font-family="Arial, sans-serif" font-size="15" fill="#333333">Remembered prototype-stage value only; repeat measurements are required before final claims.</text>
  <rect x="72" y="132" width="520" height="120" rx="8" fill="#f7f7f7" stroke="#111111" stroke-width="2"/>
  <line x1="112" y1="218" x2="540" y2="218" stroke="#111111" stroke-width="2"/>
  <rect x="112" y="170" width="{bar_width}" height="48" fill="#111111"/>
  <text x="112" y="158" font-family="Arial, sans-serif" font-size="16" font-weight="700" fill="#111111">Low-confidence remembered estimate</text>
  <text x="{124 + bar_width}" y="203" font-family="Arial, sans-serif" font-size="22" font-weight="700" fill="#111111">{label}</text>
  <text x="72" y="294" font-family="Arial, sans-serif" font-size="14" fill="#444444">Use controlled voltage-time, load-resistor, or capacitor charging tests for final energy values.</text>
  <text x="72" y="318" font-family="Arial, sans-serif" font-size="14" fill="#444444">The current repository keeps preliminary estimates separate from measured data.</text>
</svg>
"""

    (FIGURES_DIR / "preliminary_energy_estimate.svg").write_text(svg, encoding="utf-8")


def write_validation_estimate_svg(estimate_rows: list[dict[str, str]]) -> None:
    FIGURES_DIR.mkdir(exist_ok=True)

    voltage_rows = [
        row for row in estimate_rows
        if row.get("test_type") in {"open_circuit_voltage", "rectified_voltage"}
    ]
    energy_rows = [
        row for row in estimate_rows
        if safe_float(row.get("estimated_energy_j", "")) is not None
    ]

    max_voltage = max(
        [safe_float(row.get("peak_voltage_v", "")) or 0.0 for row in voltage_rows] + [1.0]
    )
    max_energy_mj = max(
        [(safe_float(row.get("estimated_energy_j", "")) or 0.0) * 1000 for row in energy_rows] + [1.0]
    )

    voltage_bars = []
    for index, row in enumerate(voltage_rows[:6]):
        value = safe_float(row.get("peak_voltage_v", "")) or 0.0
        width = int((value / max_voltage) * 260)
        y = 124 + index * 32
        label = f"{row.get('test_type', '')} / {row.get('step_type', '')}".replace("_", " ")
        voltage_bars.append(
            f'<text x="48" y="{y + 17}" font-family="Arial, sans-serif" font-size="12" fill="#333333">{label}</text>'
            f'<rect x="250" y="{y}" width="{width}" height="20" fill="#111111"/>'
            f'<text x="{260 + width}" y="{y + 16}" font-family="Arial, sans-serif" font-size="12" fill="#111111">{value:.1f} V</text>'
        )

    energy_bars = []
    for index, row in enumerate(energy_rows[:6]):
        value_mj = (safe_float(row.get("estimated_energy_j", "")) or 0.0) * 1000
        width = int((value_mj / max_energy_mj) * 260)
        y = 124 + index * 32
        label = f"{row.get('test_type', '')} / {row.get('step_type', '')}".replace("_", " ")
        energy_bars.append(
            f'<text x="560" y="{y + 17}" font-family="Arial, sans-serif" font-size="12" fill="#333333">{label}</text>'
            f'<rect x="760" y="{y}" width="{width}" height="20" fill="#111111"/>'
            f'<text x="{770 + width}" y="{y + 16}" font-family="Arial, sans-serif" font-size="12" fill="#111111">{value_mj:.2f} mJ</text>'
        )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="420" viewBox="0 0 1080 420">
  <rect width="1080" height="420" fill="#ffffff"/>
  <text x="44" y="54" font-family="Arial, sans-serif" font-size="27" font-weight="700" fill="#111111">Photo-informed validation estimate summary</text>
  <text x="44" y="86" font-family="Arial, sans-serif" font-size="15" fill="#333333">Simulated estimates from prototype photos and engineering assumptions; not final measured data.</text>
  <text x="48" y="112" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="#111111">Estimated peak voltage</text>
  {''.join(voltage_bars)}
  <text x="560" y="112" font-family="Arial, sans-serif" font-size="15" font-weight="700" fill="#111111">Estimated energy cases</text>
  {''.join(energy_bars)}
  <text x="44" y="384" font-family="Arial, sans-serif" font-size="14" fill="#444444">Rows are labeled simulated_photo_informed in data/photo_informed_validation_estimates.csv.</text>
</svg>
"""

    (FIGURES_DIR / "validation_estimate_summary.svg").write_text(svg, encoding="utf-8")


def main() -> None:
    preliminary_estimate_j = read_preliminary_estimate_j()
    real_rows = measured_rows()
    estimate_rows = validation_estimate_rows()

    write_summary(preliminary_estimate_j, real_rows, estimate_rows)
    write_preliminary_estimate_svg(preliminary_estimate_j)
    write_validation_estimate_svg(estimate_rows)

    print("EcoStep analysis complete.")
    print(f"Measured rows detected: {len(real_rows)}")
    print(f"Photo-informed estimate rows detected: {len(estimate_rows)}")
    print(f"Wrote {ANALYSIS_DIR / 'analysis_summary.txt'}")
    print(f"Wrote {FIGURES_DIR / 'preliminary_energy_estimate.svg'}")
    print(f"Wrote {FIGURES_DIR / 'validation_estimate_summary.svg'}")


if __name__ == "__main__":
    main()
