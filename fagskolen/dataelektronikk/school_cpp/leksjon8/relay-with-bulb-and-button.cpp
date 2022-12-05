int signal = 4;
int buttonPin = 3;

void setup() {
  pinMode(signal, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {
  if (digitalRead(buttonPin) == LOW) {
    digitalWrite(signal, HIGH);
  } else {
    digitalWrite(signal, LOW);
  }
}
