int signal = 4;
int sensorPin = A0;

void setup() {
  pinMode(signal, OUTPUT);
}

void loop() {
  // getting the voltage reading from the temperature sensor
  int reading = analogRead(sensorPin);
  
  // converting that reading to voltage, for 3.3v arduino use 3.3
  float voltage = reading * 5.0;
  voltage /= 1024.0;
  
  // temp
  float temperatureC = (voltage - 0.5) * 100;
  // converting from 10mv per degree with 500 mV offset
  // to degrees ((voltage - 500mV) times 100)
  
  if (temperatureC<21) {
    digitalWrite(signal, LOW);
  } else {
    digitalWrite(signal, HIGH);
  }
}
