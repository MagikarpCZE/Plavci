#include <Arduino.h>
#include "Adafruit_VL53L1X.h"

#define RX_PIN D7
#define TX_PIN D6

Adafruit_VL53L1X vl53 = Adafruit_VL53L1X();

const int SEND_INTERVAL = 5000;
unsigned long lastSendTime = 0;
int messageCount = 1;

// Global variable renamed to currentDistanceCm
float currentDistanceCm = 0.0;

void initSensors();
void initLoRa();
void readSensor();
void sendData();
void handleLoRaResponse();

void setup() {
  Serial.begin(115200);
  initSensors();
  initLoRa();
}

void loop() {
  readSensor();

  if (millis() - lastSendTime > SEND_INTERVAL) {
    sendData();
    lastSendTime = millis();
  }

  handleLoRaResponse();
}

void initSensors() {
  Wire.begin();
  if (!vl53.begin(0x29, &Wire)) {
    Serial.println("Error: VL53L1X sensor not found!");
    while (1);
  }
  
  vl53.startRanging();
  Serial.println("VL53L1X initialized.");
}

void initLoRa() {
  Serial1.begin(9600, SERIAL_8N1, RX_PIN, TX_PIN);
  delay(2000);

  Serial.println("--- LoRa-E5 Setup ---");
  Serial1.println("AT+MODE=TEST");
  delay(500);
  Serial1.println("AT+TEST=RFCFG,868,SF7,125,12,15,14,ON,OFF,OFF");
  delay(500);
}

void readSensor() {
  if (vl53.dataReady()) {
    // Convert mm to cm by dividing by 10.0
    currentDistanceCm = (float)vl53.distance() / 10.0;
    vl53.clearInterrupt();
    
    Serial.print("Current distance: ");
    // Print with 3 decimal places
    Serial.print(currentDistanceCm, 3);
    Serial.println(" cm");
  }
}

void sendData() {
  // Convert float to string with 3 decimal places
  String distStr = String(currentDistanceCm, 3);
  String payload = "Dist: " + distStr + "cm";
  String command = "AT+TEST=TXLRSTR,\"" + payload + "\"";

  Serial.print("\n[SENDING] -> ");
  Serial.println(payload);

  Serial1.println(command);
  messageCount++;
}

void handleLoRaResponse() {
  while (Serial1.available()) {
    Serial.write(Serial1.read());
  }
}