// Lights
int pG	= 1;				// pedestrian green
int pR	= 2;				// pedestrian red
int cG 	= 3;				// car green
int cY 	= 4;				// car yellow
int cR	= 5;				// car red


// Delays
int pGD	= 5000; 			// pedGreenDelay
int pFD	= 1500; 			// pedFinishDelay
int cGD	= 5000;				// carGreenDeleay
int cYD	= 1500;				// carYellowDelay
int cFD	= 1500;				// carFinishDelay

// consts
const int buttonPin = 7;	// the number of the pushbutton pin
const int ledPin	= 13;	// number of the LED pin (on the board)
const int buzzerPin	= 13;	// buzzer pin

int buttonState = 0;		// variable for reading the pushbutton status

void setup()
{
  for (int i=1; i<6; i++) {
    pinMode(i, OUTPUT);
  }
  
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop()
{
  // Car green, pedestrian Red
  digitalWrite(cG, HIGH);
  digitalWrite(cY, LOW);
  digitalWrite(cR, LOW);
  digitalWrite(pG, LOW);
  digitalWrite(pR, HIGH);
  
  // Check if the button is clicked
  buttonState = digitalRead(buttonPin);
  
  // HIGH if clicked
  if (buttonState == HIGH) {
    // When pedestrian want to cross they click
    // Yellow light for the cars
    digitalWrite(cG, LOW);
    digitalWrite(cY, HIGH);
    digitalWrite(cR, LOW);
    //wait a sec
    delay(cYD);
    // Cars red
    digitalWrite(cY, LOW);
    digitalWrite(cR, HIGH);
    //wait a sec
    delay(cFD);
    // Pedestrian, red off green on
    digitalWrite(pR, LOW);
    digitalWrite(pG, HIGH);
    // buzzer cozy
    for (int i=1; i<11; i++) {
      pip(1000, 100);
      delay(pGD/10);
    }
    
    // blinking green light
    for (int i=1; i<6; i++) {
      digitalWrite(pG, HIGH);
      delay(300);
      digitalWrite(pG, LOW);
      delay(300);
      pip-(1000, 100); 			// buzzer
    }
    
    // Red for pedestrians
    digitalWrite(pG, LOW);
    digitalWrite(pR, HIGH);
    delay(pFD);
  }
}

void pip(int frekvens, int tid) { // bip function
  digitalWrite(buzzerPin, HIGH);
  tone(buzzerPin, frekvens);	// Send 1KhZ SOUND SIGNAL
  delay(tid);					// for 100 ms
  noTone(buzzerPin);			// stop sound
  digitalWrite(buzzerPin, LOW);
}
    
