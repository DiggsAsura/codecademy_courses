// Code should work, but still did not work. Wrong resistor?
const int pinSegG	= 13;
const int pinSegF	= 12;
const int pinSegA	= 11;
const int pinSegB	= 10;
const int pinSegE	= 9;
const int pinSegD	= 8;
const int pinSegC	= 7;
const int pinSegDP	= 6;	// DP=Decimal point

void setup(void) {
  pinMode(pinSegG, OUTPUT);
  pinMode(pinSegF, OUTPUT);
  pinMode(pinSegA, OUTPUT);
  pinMode(pinSegB, OUTPUT);
  pinMode(pinSegE, OUTPUT);
  pinMode(pinSegD, OUTPUT);
  pinMode(pinSegC, OUTPUT);
  pinMode(pinSegDP, OUTPUT);
}

// One function = one letter on the screen

void zero(void) {
  digitalWrite(pinSegG, LOW);
  digitalWrite(pinSegF, HIGH);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, HIGH);
  digitalWrite(pinSegD, HIGH);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void one(void) {
  digitalWrite(pinSegG, LOW);
  digitalWrite(pinSegF, LOW);
  digitalWrite(pinSegA, LOW);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, LOW);
  digitalWrite(pinSegD, LOW);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void two(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, LOW);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, HIGH);
  digitalWrite(pinSegD, HIGH);
  digitalWrite(pinSegC, LOW);
  digitalWrite(pinSegDP, LOW);
}

void three(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, LOW);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, LOW);
  digitalWrite(pinSegD, HIGH);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void four(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, HIGH);
  digitalWrite(pinSegA, LOW);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, LOW);
  digitalWrite(pinSegD, LOW);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void five(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, HIGH);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, LOW);
  digitalWrite(pinSegE, LOW);
  digitalWrite(pinSegD, HIGH);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void six(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, HIGH);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, LOW);
  digitalWrite(pinSegE, HIGH);
  digitalWrite(pinSegD, HIGH);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void seven(void) {
  digitalWrite(pinSegG, LOW);
  digitalWrite(pinSegF, LOW);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, LOW);
  digitalWrite(pinSegD, LOW);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void eight(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, HIGH);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, HIGH);
  digitalWrite(pinSegD, HIGH);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}

void nine(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, HIGH);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, LOW);
  digitalWrite(pinSegD, HIGH);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, LOW);
}
void ten(void) {
  digitalWrite(pinSegG, HIGH);
  digitalWrite(pinSegF, HIGH);
  digitalWrite(pinSegA, HIGH);
  digitalWrite(pinSegB, HIGH);
  digitalWrite(pinSegE, HIGH);
  digitalWrite(pinSegD, LOW);
  digitalWrite(pinSegC, HIGH);
  digitalWrite(pinSegDP, HIGH);
}

// Start
void loop(void)
{
  zero();
  delay(1000);
  
  one();
  delay(1000);
  
  two();
  delay(1000);
  
  three();
  delay(1000);
  
  four();
  delay(1000);
  
  five();
  delay(1000);
  
  six();
  delay(1000);
  
  seven();
  delay(1000);
  
  eight();
  delay(1000);
  
  nine();
  delay(1000);
  
  ten();
  delay(5000);
}

