// initialize the motor
int motorPin = 9;

void setup()
{
  //pinMode(motorPin, OUTPUT);
  // Choose speed additions
  /*Serial.begin(9600);
  while (! Serial);
  Serial.println("Speed 0 to 255");
  */
}

void loop()
{
  // on off motor
  //digitalWrite(motorPin, HIGH);
  //delay(1000);
  //digitalWrite(motorPin, LOW);
  //delay(1000);
  
  // change speeds, swap between two speeds
  //analogWrite(motorPin, 10);
  //delay(1000);
  //digitalWrite(motorPin, 255);
  //delay(1000);
  
  // change the speed through a for loop
  
  for (int i=1; i<255; i++) {
    analogWrite(motorPin, i);
    delay(100);
  }
  for (int i=255; i>0; i--) {
    analogWrite(motorPin, i);
    delay(100);
  }
  
  // Choose the speed
  // See additions in void setup()
  /*if (Serial.available()) {
    int speed = Serial.parseInt();
    if (speed >= 0 && speed <= 255) {
      analogWrite(motorPin, speed);
    }
  }*/
}
