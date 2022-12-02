// consts
const int buttonPin = 2;
const int ledPin	= 13;
const int buzzer	= 13;

// variables
int buttonState		= 0;	// variable for reading the pushbutton status

void setup() {
  // initialize the LED pin as an output
  pinMode(ledPin, OUTPUT);
  // initialize the pushbuton pin as an input
  pinMode(buttonPin, INPUT);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);
  
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH
  if (buttonState == HIGH) {
    // turn LED on
    digitalWrite(ledPin, HIGH);
    tone(buzzer, 1000);			// Send 1KHz sound signal
    delay(1000);				// ..for 1 second
    noTone(buzzer);				// Stop sound
  } else {
    // turn LED off:
    digitalWrite(ledPin, LOW);
  }
}
