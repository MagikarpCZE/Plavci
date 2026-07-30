#include <Arduino.h>

const int mofsetPin = 2;   // Pin D10 na XIAO ESP32-C6
const int freq = 30000;       // Frekvence 100 Hz
const int res = 10;         // 10-bit rozlišení (0-1023)

void setup() {
  Serial.begin(115200);
  
  // Inicializace PWM na pinu D10
  if (ledcAttach(mofsetPin, freq, res)) {
    Serial.println("PWM pro MOSFET test spuštěno na 100 Hz");
  }
}

void loop() {
  // Plynulé zvyšování výkonu
  for (int duty = 0; duty <= 1023; duty += 5) {
    ledcWrite(mofsetPin, duty);
    delay(10); 
  }
  
  // Plynulé snižování výkonu
  for (int duty = 1023; duty >= 0; duty -= 5) {
    ledcWrite(mofsetPin, duty);
    delay(10);
  }
}