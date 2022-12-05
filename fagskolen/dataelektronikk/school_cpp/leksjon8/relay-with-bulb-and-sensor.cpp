int triggerValue=500;	// Grense for å slå av/på lys
int signal = 4;
int sensorValue = 0;

void setup() {
  pinMode(signal, OUTPUT);
  pinMode(A0, INPUT);
}

void loop() {
  sensorValue = analogRead(A0);
  if (sensorValue>triggerValue) {
    digitalWrite(signal, LOW);
  } else {
    digitalWrite(signal, HIGH);
  }
  delay(1000);
}
