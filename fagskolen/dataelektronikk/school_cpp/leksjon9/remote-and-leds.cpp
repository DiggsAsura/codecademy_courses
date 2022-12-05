#include <IRremote.h>

// Define pins
int redLed = 7;
int yellowLed = 6;
int greenLed = 5;
int blueLed = 4;
int RECV_PIN = 11;

// IR Library stuff
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
  // Set Led Pins
  pinMode(redLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(blueLed, OUTPUT);
  
  // Enable serial usage and IR signal in
  Serial.begin(9600);	// whats the 9600 value?
  Serial.println("Enabling IRin");
  irrecv.enableIRIn();
  Serial.println("Enabled IRin");
}

void loop() {
  if (irrecv.decode(&results)) { 
    unsigned int value = results.value;
    Serial.println(value);
    
    switch (value) {
      case 2295:
      	digitalWrite(redLed, HIGH);
      	delay(500);
      	digitalWrite(redLed, LOW);
      	break;
      case 34935:
      	digitalWrite(yellowLed, HIGH);
      	delay(500);
      	digitalWrite(yellowLed, LOW);
      	break;
      case 18615:
      	digitalWrite(greenLed, HIGH);
      	delay(500);
      	digitalWrite(greenLed, LOW);
      	break;
      case 10455:
      	digitalWrite(blueLed, HIGH);
      	delay(500);
      	digitalWrite(blueLed, LOW);
      	break;
      case 39015:
      	digitalWrite(blueLed, HIGH);
      	delay(300);
      	digitalWrite(greenLed, HIGH);
      	delay(300);
      	digitalWrite(yellowLed, HIGH);
      	delay(300);
      	digitalWrite(redLed, HIGH);
      	delay(1000);
      	digitalWrite(redLed, LOW);
      	digitalWrite(yellowLed, LOW);
      	digitalWrite(greenLed, LOW);
      	digitalWrite(blueLed, LOW);
      	break;
    }
    
    irrecv.resume();		// Receive the next value
  }
}
