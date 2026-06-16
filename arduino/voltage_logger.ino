/*
  EcoStep voltage logger

  Logs analog voltage readings from a piezoelectric tile measurement circuit.
  Connect the measured voltage across a known load resistor to A0 through a
  safe voltage divider or input protection circuit.

  Important:
  - Keep voltage within the safe analog input range of the board.
  - Use a voltage divider or protection circuit if the piezo output may exceed it.
  - Record the voltage-divider ratio in the measurement notes.
  - Record the load resistance in the CSV notes for energy calculation.
*/

const int SENSOR_PIN = A0;
const float ADC_REFERENCE_VOLTAGE = 5.0;
const int ADC_MAX = 1023;
const unsigned long SAMPLE_DELAY_MS = 5;

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("time_ms,analog_value,voltage_v");
}

void loop() {
  unsigned long now = millis();
  int raw = analogRead(SENSOR_PIN);
  float voltage = (raw * ADC_REFERENCE_VOLTAGE) / ADC_MAX;

  Serial.print(now);
  Serial.print(",");
  Serial.print(raw);
  Serial.print(",");
  Serial.println(voltage, 4);

  delay(SAMPLE_DELAY_MS);
}
