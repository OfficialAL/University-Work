int forceSensorPin = A0;
int tiltSensorPin = 2;
int ledPin = 8;
int buzzerPin = 9;

const int forceThreshold = 2000;   // Adjust based on testing
bool crashDetected = false;

void setup() {
  pinMode(forceSensorPin, INPUT);  // Force sensor input
  pinMode(tiltSensorPin, INPUT);   // Tilt sensor input
  pinMode(ledPin, OUTPUT);         // LED output
  pinMode(buzzerPin, OUTPUT);      // Buzzer output
  Serial.begin(9600);              // Initialize serial communication
}

void loop() {
  int forceValue = analogRead(forceSensorPin);   // Read force sensor
  int tiltState = digitalRead(tiltSensorPin);    // Read tilt sensor

  // Check if either force or tilt sensors detect a potential crash
  if (forceValue > forceThreshold || tiltState == HIGH) {
    digitalWrite(ledPin, HIGH);   // Turn on LED
    tone(buzzerPin, 2000);        // Activate buzzer at 2000 Hz
    Serial.println("Crash detected!");
    crashDetected = true;
  } else {
    digitalWrite(ledPin, LOW);    // Turn off LED
    noTone(buzzerPin);            // Deactivate buzzer
    crashDetected = false;
  }

  // Print sensor values to Serial Monitor for debugging
  Serial.print("Force Sensor Value: ");
  Serial.print(forceValue);
  Serial.print(" | Tilt Sensor State: ");
  Serial.println(tiltState);

  delay(100); // Delay for debounce and to reduce serial output frequency
}
