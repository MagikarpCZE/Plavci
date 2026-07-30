#include <Arduino.h>

#define LORA_RX_PIN D7
#define LORA_TX_PIN D6

const int ledPin = 2;   // Pin D10 na XIAO ESP32-C6
const int freq = 30000;
const int res = 10;     // 10-bit rozliseni (0-1023)

bool ledOn = false;

void initLoRa();
void startListening();
void handleLoRaData();
void setLed(bool on);

void setup() {
  Serial.begin(115200);

  if (ledcAttach(ledPin, freq, res)) {
    Serial.println("PWM pro LED/MOSFET pripraveno");
  }
  setLed(false);

  initLoRa();
  startListening();
}

void loop() {
  handleLoRaData();
}

void initLoRa() {
  Serial1.begin(9600, SERIAL_8N1, LORA_RX_PIN, LORA_TX_PIN);
  delay(2000);

  Serial.println("--- LoRa-E5 Receiver Setup ---");
  Serial1.println("AT+MODE=TEST");
  delay(500);
  // Musi odpovidat konfiguraci na vysilaci (transmitter.ino)
  Serial1.println("AT+TEST=RFCFG,868,SF7,125,12,15,14,ON,OFF,OFF");
  delay(500);
}

void startListening() {
  Serial1.println("AT+TEST=RXLRPKT");
}

void handleLoRaData() {
  static String line = "";

  while (Serial1.available()) {
    char c = Serial1.read();
    Serial.write(c);

    if (c == '\n') {
      line.trim();

      int rxIndex = line.indexOf("+TEST: RX \"");
      if (rxIndex != -1) {
        int hexStart = rxIndex + strlen("+TEST: RX \"");
        int hexEnd = line.indexOf('"', hexStart);

        if (hexEnd != -1) {
          String hexPayload = line.substring(hexStart, hexEnd);
          String message = "";

          for (int i = 0; i + 1 < hexPayload.length(); i += 2) {
            String byteStr = hexPayload.substring(i, i + 2);
            char decoded = (char) strtol(byteStr.c_str(), nullptr, 16);
            message += decoded;
          }

          Serial.print("[RECEIVED] -> ");
          Serial.println(message);

          if (message == "BTN:1") {
            ledOn = !ledOn;
            setLed(ledOn);
          }
        }

        // Modul se po prijeti paketu vraci do standby, znovu spustime naslouchani
        startListening();
      }

      line = "";
    } else if (c != '\r') {
      line += c;
    }
  }
}

void setLed(bool on) {
  ledcWrite(ledPin, on ? 1023 : 0);
  Serial.print("LED ");
  Serial.println(on ? "ON" : "OFF");
}
