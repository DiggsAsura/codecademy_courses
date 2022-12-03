#include <LiquidCrystal.h>

// Initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Initialize buttons
const int buttonPin1 = 6;
const int buttonPin2 = 7;
const int buttonPin3 = 8;
const int buttonPin4 = 9;

int buttonState1 = 0;
int buttonState2 = 0;
int buttonState3 = 0;
int buttonState4 = 0;

int num = 0;
String hex;	// Hexadecimal. 0-9, A-F

void setup()
{
  // set up lcd
  lcd.begin(16,2);
  // print to display
  lcd.print("Decimal - Hex");
  
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin1, INPUT);
  pinMode(buttonPin2, INPUT);
  pinMode(buttonPin3, INPUT);
  pinMode(buttonPin4, INPUT);
}

void loop()
{
  num = 0;	// to reset every loop
  lcd.setCursor(0,1);
  lcd.print("    ");	// Cleaning display
  buttonState1 = 0;
  buttonState2 = 0;
  buttonState3 = 0;
  buttonState4 = 0;
  buttonState1 = digitalRead(buttonPin1);
  buttonState2 = digitalRead(buttonPin2);
  buttonState3 = digitalRead(buttonPin3);
  buttonState4 = digitalRead(buttonPin4);
  
  lcd.setCursor(0, 1); // nødvendig?
  if (buttonState1 == HIGH) num=num+1; // 2^0
  if (buttonState2 == HIGH) num=num+2; // 2^1
  if (buttonState3 == HIGH) num=num+4; // 2^2
  if (buttonState4 == HIGH) num=num+8; // 2^3
  
  switch(num) {
    case 0 ... 9:
      hex=String(num); // Gjør tall om til tegn
      break;
    case 10:
      hex="A";
      break;
    case 11:
      hex="B";
      break;
    case 12:
      hex="C";
      break;
    case 13:
      hex="D";
      break;
    case 14:
      hex="E";
      break;
    case 15:
      hex="F";
      break;
  } // end-switch
  lcd.setCursor(0, 1);
  lcd.print(num);
  lcd.setCursor(12,1);
  lcd.print(hex);
  delay(1000);
  
}
