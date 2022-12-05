#include <IRremote.h>
int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;
int count = 0;
int signal = 4;

void setup() {
  pinMode(signal, OUTPUT);
  Serial.begin(9600);
  Serial.println("Enabling IRin");
  irrecv.enableIRIn();
  Serial.println("Enabled IRin");
}

void loop() {
  // irrecv.decode(&results) returns true if anything is received, and stores
  // info in variable results
  if (irrecv.decode(&results)) {
    unsigned int value = results.value; // Get the value as an unsigned int
    Serial.println(value);
    if (value==2295)
      digitalWrite(signal, LOW);
    if (value == 12495)
      digitalWrite(signal, HIGH);
  }
  irrecv.resume();
 }
