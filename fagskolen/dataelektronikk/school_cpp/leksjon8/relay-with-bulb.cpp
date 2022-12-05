int signal = 4;

void setup() {
  pinMode(signal, OUTPUT);
}

void loop() {
  digitalWrite(signal, HIGH);
  delay(1000);
  digitalWrite(signal, LOW);
  delay(1000);
}
