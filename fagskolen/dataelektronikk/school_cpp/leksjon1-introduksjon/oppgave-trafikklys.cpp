// Lights
int cG 	= 3;		// car green
int cY 	= 4;		// car yellow
int cR	= 5;		// car red
int pG	= 1;		// pedestrian green
int pR	= 2;		// pedestrian red

// Delays
int cGD	= 5000;		// carGreenDeleay
int cYD	= 1500;		// carYellowDelay
int cFD	= 1500;		// carFinishDelay
int pGD	= 5000; 	// pedGreenDelay
int pFD	= 1500; 	// pedFinishDelay

void setup()
{
  for (int i=1; i<6; i++) {
    pinMode(i, OUTPUT);
  }
}

void loop()
{
  // Both starts in red 
  digitalWrite(cG, LOW);
  digitalWrite(cY, LOW);
  digitalWrite(pG, LOW);
  digitalWrite(cR, HIGH);
  digitalWrite(pR, HIGH);
  
  // Wait until pedestrian is out of the road
  delay(pFD);
  
  // Yellow lights for the cars, in addition to the red
  digitalWrite(cY, HIGH);
  
  // Delay
  delay(cYD);
  
  // Turning off yellow and red, turns on green
  digitalWrite(cR, LOW);
  digitalWrite(cY, LOW);
  digitalWrite(cG, HIGH);
  
  // Let the cars drive
  delay(cGD);
  
  // Yellow light for the cars
  digitalWrite(cG, LOW);
  digitalWrite(cR, LOW);
  digitalWrite(cY, HIGH);
  
  // Delay yellow light
  delay(cYD);
  
  // Cars red
  digitalWrite(cY, LOW);
  digitalWrite(cR, HIGH);
  
  // Wait a bit
  delay(cFD);
  
  // Green for the pedestrian
  digitalWrite(pR, LOW);
  digitalWrite(pG, HIGH);
  delay(pGD);
  
  // Blinking green before red
  for (int i=1; i<6; i++) {
    digitalWrite(pG, HIGH);
    delay(1000);
    digitalWrite(pG, LOW);
    delay(300);
  }

}
