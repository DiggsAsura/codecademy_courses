#include <LiquidCrystal.h>

// initialize buttons. linked, so this is for inside and outside.
int button1 		= 2;
int button2 		= 3;
int button3 		= 4;

// button states
int buttonState1	= 0;
int buttonState2	= 0;
int buttonState3	= 0;

// led pins, indicate at what floor
int ledPin1 = 5;
int ledPin2 = 6;
int ledPin3 = 7;

// interface pins on the display
LiquidCrystal lcd(0, 1, 8, 9, 10, 11);
int sensorPin = 0;

void setup()
{
  // set up lcd
  lcd.begin(16,2);
  
  // buttons
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  
  // leds
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
}

/* -------
TEMPERATURE CHECKER FUNCTION
--------- */
void tempc() {
  // sensor stuff
  int reading = analogRead(sensorPin);
  // Control: 184 = 40C 
  float voltage = reading * 5.0;
  voltage /= 1024.0;
  
  // turn reading volt into Celcius
  float tempC = (voltage - 0.5) * 100;
  
  lcd.clear();
  if (tempC > 40.0) {
    lcd.clear();
    lcd.setCursor(0, 1);
    lcd.print("STOP!");
    // SOME CHECK IF IN BETWEEN FLOORS, OR AT A FLOOR. 
    // IF AT A FLOOR, OPEN DOORS IMMEDIATLY
    // IF IN BETWEEN, OPEN DOORS IMMEDIATLY AT NEXT FLOOR.

  }
}

// MAIN FUNCTION
void loop()
{
  // Read button state
  buttonState1 = digitalRead(button1);
  buttonState2 = digitalRead(button2);
  buttonState3 = digitalRead(button3);
  
  /* -------------------------------------
  * Testing if buttons work
  */
  int currentFloor = 2;
  
  // led
  if (currentFloor == 1) {
      digitalWrite(ledPin1, HIGH);
      digitalWrite(ledPin2, LOW);
      digitalWrite(ledPin3, LOW);
  } else if (currentFloor == 2) {
      digitalWrite(ledPin2, HIGH);
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin3, LOW);
  } else if (currentFloor == 3) {
      digitalWrite(ledPin3, HIGH);
      digitalWrite(ledPin1, LOW);
      digitalWrite(ledPin2, LOW);
  }
  tempc();
  
  switch (buttonState1) {
    case HIGH:
    	lcd.setCursor(0, 0);
    	if (currentFloor == 1) {
          lcd.print("Doors open");
        } else { 
          lcd.print("Going to 1st");
          currentFloor = 1;
        }
    case LOW:
    	break;
  }
  switch (buttonState2) {
    case HIGH:
    	lcd.setCursor(0, 0);
    	if (currentFloor == 2) {
          lcd.print("Doors open");
        } else { 
          lcd.print("Going to 2nd");
          currentFloor = 2;
        }
    case LOW:
    	break;
  }
    switch (buttonState3) {
    case HIGH:
    	lcd.setCursor(0, 0);
    	if (currentFloor == 3) {
          lcd.print("Doors open");
        } else { 
          lcd.print("Going to 3rd");
          currentFloor = 3;
        }
    case LOW:
    	break;
  }   

  
  // Make function for checking temp to put in switch statement
  /*
 
  
  
  lcd.setCursor(0, 0);
  lcd.print("Current floor: ");
  lcd.print(floor);
  if (tempC < 40.0) {
    lcd.setCursor(0, 1);
    lcd.print("Ok, going up");
  } else {
    //lcd.clear();
    lcd.setCursor(0, 1);
    lcd.print("STOP!");
  }
  */
  
  // --------------
  // Keeping screen from overlap
  delay(500); // a bit delay to avoid screen overlaps 
  lcd.clear();
}
