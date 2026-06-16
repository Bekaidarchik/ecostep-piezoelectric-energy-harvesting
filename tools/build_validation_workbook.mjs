import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const __filename = fileURLToPath(import.meta.url);
const projectRoot = path.resolve(path.dirname(__filename), "..");
const dataDir = path.join(projectRoot, "data");
const outputPath = path.join(dataDir, "ecostep_validation_workbook.xlsx");

function parseCsv(text) {
  const rows = [];
  let row = [];
  let value = "";
  let quoted = false;

  for (let i = 0; i < text.length; i += 1) {
    const char = text[i];
    const next = text[i + 1];

    if (char === '"' && quoted && next === '"') {
      value += '"';
      i += 1;
    } else if (char === '"') {
      quoted = !quoted;
    } else if (char === "," && !quoted) {
      row.push(value);
      value = "";
    } else if ((char === "\n" || char === "\r") && !quoted) {
      if (char === "\r" && next === "\n") i += 1;
      row.push(value);
      if (row.some((cell) => cell !== "")) rows.push(row);
      row = [];
      value = "";
    } else {
      value += char;
    }
  }

  if (value || row.length) {
    row.push(value);
    rows.push(row);
  }

  return rows;
}

function numeric(value) {
  if (value === null || value === undefined || value === "") return null;
  const number = Number(value);
  return Number.isFinite(number) ? number : value;
}

function rowsToObjects(rows) {
  const [headers, ...body] = rows;
  return body.map((row) => Object.fromEntries(headers.map((header, index) => [header, row[index] ?? ""])));
}

function writeTable(sheet, startCell, rows, tableName) {
  const range = sheet.getRange(startCell).resize(rows.length, rows[0].length);
  range.values = rows.map((row, rowIndex) => row.map((cell) => (rowIndex === 0 ? cell : numeric(cell))));
  range.format.borders = { preset: "all", style: "thin", color: "#D9D9D9" };
  range.format.font = { name: "Aptos", size: 10, color: "#111111" };
  sheet.getRange(startCell).resize(1, rows[0].length).format = {
    fill: "#111111",
    font: { bold: true, color: "#FFFFFF" },
  };
  const table = sheet.tables.add(range.address, true, tableName);
  table.style = "TableStyleMedium1";
  return range;
}

function styleTitle(sheet, title, subtitle) {
  sheet.showGridLines = false;
  sheet.getRange("A1:H1").merge();
  sheet.getRange("A1").values = [[title]];
  sheet.getRange("A1").format = {
    fill: "#111111",
    font: { bold: true, color: "#FFFFFF", size: 18 },
  };
  sheet.getRange("A2:H2").merge();
  sheet.getRange("A2").values = [[subtitle]];
  sheet.getRange("A2").format = {
    fill: "#F3F4F6",
    font: { color: "#333333", size: 11 },
  };
}

const validationCsv = parseCsv(await fs.readFile(path.join(dataDir, "photo_informed_validation_estimates.csv"), "utf8"));
const preliminaryCsv = parseCsv(await fs.readFile(path.join(dataDir, "preliminary_estimate.csv"), "utf8"));
const rawCsv = parseCsv(await fs.readFile(path.join(dataDir, "raw_measurements.csv"), "utf8"));
const cleanedCsv = parseCsv(await fs.readFile(path.join(dataDir, "cleaned_measurements.csv"), "utf8"));
const validationObjects = rowsToObjects(validationCsv);

const workbook = Workbook.create();

const summary = workbook.worksheets.add("Summary");
styleTitle(summary, "EcoStep Validation Workbook", "Photo-informed estimates are clearly separated from real measured data.");
summary.getRange("A4:B10").values = [
  ["Prototype", "16 PZT elements in a 4 x 4 footstep tile"],
  ["Physical evidence", "Prototype and build-stage photos are included in the repository"],
  ["Real measured rows", 0],
  ["Photo-informed estimate rows", validationObjects.filter((row) => row.evidence_status === "simulated_photo_informed").length],
  ["Preliminary memory estimate", "0.4 J, low confidence, not measured"],
  ["Wiring status", "grouped_unknown until traced"],
  ["Honesty rule", "Do not present estimates as lab measurements"],
];
summary.getRange("A4:B10").format.borders = { preset: "all", style: "thin", color: "#D9D9D9" };
summary.getRange("A4:A10").format = { fill: "#E5E7EB", font: { bold: true } };
summary.getRange("A12:D18").values = [
  ["Validation Area", "Status", "Rows", "Reviewer Meaning"],
  ["Open-circuit voltage", "Estimated", 4, "Shows likely voltage pulse range"],
  ["Rectified voltage", "Estimated", 3, "Shows likely DC-side voltage after losses"],
  ["Capacitor charging", "Modeled", 3, "Shows aggregate stored-energy cases"],
  ["Load resistor", "Modeled", 5, "Shows useful-energy estimates under known load"],
  ["Single vs array", "Estimated", 2, "Shows why 16 PZT elements matter"],
  ["Wiring topology", "Inferred", 1, "Kept conservative as grouped_unknown"],
];
writeTable(summary, "A12", summary.getRange("A12:D18").values, "SummaryCoverageTable");
summary.getRange("A1:H20").format.autofitColumns();

const validation = workbook.worksheets.add("Validation_Estimates");
styleTitle(validation, "Photo-Informed Validation Estimates", "Use evidence_status to distinguish estimates from real measurements.");
writeTable(validation, "A4", validationCsv, "ValidationEstimatesTable");
validation.getRange("A1:P24").format.autofitColumns();
validation.freezePanes.freezeRows(4);

const chartData = workbook.worksheets.add("Chart_Data");
styleTitle(chartData, "Chart Data", "Helper ranges for the workbook charts.");
const voltageRows = validationObjects
  .filter((row) => ["open_circuit_voltage", "rectified_voltage"].includes(row.test_type))
  .map((row) => [`${row.test_type.replaceAll("_", " ")} / ${row.step_type}`, Number(row.peak_voltage_v || 0)]);
const energyRows = validationObjects
  .filter((row) => row.estimated_energy_j)
  .map((row) => [`${row.test_type.replaceAll("_", " ")} / ${row.step_type}`, Number(row.estimated_energy_j) * 1000]);
chartData.getRange("A4:B4").values = [["Case", "Peak voltage (V)"]];
chartData.getRange("A5:B" + (4 + voltageRows.length)).values = voltageRows;
chartData.getRange("D4:E4").values = [["Case", "Energy estimate (mJ)"]];
chartData.getRange("D5:E" + (4 + energyRows.length)).values = energyRows;
writeTable(chartData, "A4", [["Case", "Peak voltage (V)"], ...voltageRows], "VoltageChartTable");
writeTable(chartData, "D4", [["Case", "Energy estimate (mJ)"], ...energyRows], "EnergyChartTable");

const voltageChart = chartData.charts.add("bar", chartData.getRange("A4:B" + (4 + voltageRows.length)));
voltageChart.title = "Estimated Peak Voltage";
voltageChart.hasLegend = false;
voltageChart.setPosition("G4", "N18");

const energyChart = chartData.charts.add("bar", chartData.getRange("D4:E" + (4 + energyRows.length)));
energyChart.title = "Estimated Energy Cases";
energyChart.hasLegend = false;
energyChart.setPosition("G21", "N35");
chartData.getRange("A1:N36").format.autofitColumns();

const dictionary = workbook.worksheets.add("Data_Dictionary");
styleTitle(dictionary, "Data Dictionary", "Column meanings and evidence status labels.");
const dictRows = [
  ["Field", "Meaning"],
  ["case_id / trial_id", "Unique identifier for an estimate case or measured trial"],
  ["test_type", "open_circuit_voltage, rectified_voltage, capacitor_charging, load_resistor_test, single_vs_array, or wiring_topology"],
  ["array_mode", "single_pzt or array_16_pzt"],
  ["wiring_assumption", "single_disc or grouped_unknown"],
  ["load_resistance_ohm", "Known resistor value used for load testing"],
  ["capacitance_f", "Known capacitor value used for capacitor charging"],
  ["estimated_energy_j", "Energy estimate in joules from the documented equation"],
  ["measurement_status", "placeholder, measured, not_measured"],
  ["evidence_status", "simulated_photo_informed or inferred_from_photos"],
  ["notes", "Assumptions and caveats"],
];
writeTable(dictionary, "A4", dictRows, "DataDictionaryTable");
dictionary.getRange("A1:B20").format.autofitColumns();

const raw = workbook.worksheets.add("Raw_Template");
styleTitle(raw, "Raw Measurement Template", "Replace placeholder rows only after controlled tests.");
writeTable(raw, "A4", rawCsv, "RawMeasurementTemplate");
raw.getRange("A1:O8").format.autofitColumns();

const cleaned = workbook.worksheets.add("Cleaned_Template");
styleTitle(cleaned, "Cleaned Measurement Template", "Processed rows should come from raw measured trials.");
writeTable(cleaned, "A4", cleanedCsv, "CleanedMeasurementTemplate");
cleaned.getRange("A1:O8").format.autofitColumns();

const preliminary = workbook.worksheets.add("Preliminary_Estimate");
styleTitle(preliminary, "Preliminary Estimate", "Remembered value kept separate from measured and simulated data.");
writeTable(preliminary, "A4", preliminaryCsv, "PreliminaryEstimateTable");
preliminary.getRange("A1:F8").format.autofitColumns();

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});
console.log(errors.ndjson);

await workbook.render({ sheetName: "Summary", autoCrop: "all", scale: 1, format: "png" });
await workbook.render({ sheetName: "Chart_Data", autoCrop: "all", scale: 1, format: "png" });

const xlsx = await SpreadsheetFile.exportXlsx(workbook);
await xlsx.save(outputPath);
console.log(`Saved ${outputPath}`);
