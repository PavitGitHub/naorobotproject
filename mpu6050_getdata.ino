#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <math.h>

const char* ssid = "Xiaomi_7331";  // WiFi SSID
const char* password = "coreshaw738";  // WiFi password
const char* serverName = "http://192.168.31.215:5000/nao/command";  // Flask server URL

Adafruit_MPU6050 mpu;

String lastCommand = "";  // Store the last sent command

void setup() {
  Serial.begin(115200);
  
  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize MPU6050
  if (!mpu.begin()) {
    Serial.println("MPU6050 not found!");
    while (1);
  }
  Serial.println("MPU6050 initialized.");
}

void loop() {
  // Read accelerometer and gyroscope data
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  // Calculate tilt angles for X and Y axes
  float angleX = atan2(a.acceleration.y, a.acceleration.z) * 180 / PI;
  float angleY = atan2(a.acceleration.x, a.acceleration.z) * 180 / PI;

  String command;

  // Determine the command based on tilt angles
  if (angleY > 20) {  // Tilt forward more than 20 degrees
    command = "forward";
  } else if (angleY < -20) {  // Tilt backward more than -20 degrees
    command = "backward";
  } else if (angleX > 20) {  // Tilt right more than 20 degrees
    command = "right";  // Turn right in place
  } else if (angleX < -20) {  // Tilt left more than -20 degrees
    command = "left";  // Turn left in place
  } else {
    command = "stop";  // Stop moving
  }

  // Send the command only if it has changed
  if (command != lastCommand) {
    lastCommand = command;
    
    // Send the command to the Flask server
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(serverName);  // Flask server URL
      http.addHeader("Content-Type", "application/json");
      
      String httpRequestData = "{\"command\":\"" + command + "\"}";
      int httpResponseCode = http.POST(httpRequestData);
      
      if (httpResponseCode > 0) {
        String response = http.getString();
        Serial.println(httpResponseCode);
        Serial.println(response);
      } else {
        Serial.print("Error on sending POST: ");
        Serial.println(httpResponseCode);
      }
      http.end();
    } else {
      Serial.println("Wi-Fi not connected, skipping HTTP request.");
    }
  }

  delay(500);  // Check status every 500 milliseconds
}
