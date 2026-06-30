function calculateEstimate() {
  const steps = Number(document.getElementById("steps").value || 0);
  const joules = Number(document.getElementById("joules").value || 0);
  const tiles = Number(document.getElementById("tiles").value || 1);
  const totalJoules = steps * joules * tiles;
  const wattHours = totalJoules / 3600;
  document.getElementById("estimate").textContent =
    `${totalJoules.toLocaleString(undefined, { maximumFractionDigits: 1 })} J/day = ${wattHours.toLocaleString(undefined, { maximumFractionDigits: 3 })} Wh/day`;
}

calculateEstimate();
