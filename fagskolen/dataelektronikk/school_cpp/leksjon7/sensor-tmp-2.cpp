#include <LiquidCrystal.h>
// initialize the library with the numbers of the interface pins

LiquidCrystal lcd(0, 1, 8, 9, 10, 11);

int sensorPin = 0; // uhm double really?

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
}

void loop() {
  // getting the voltage reading from the temperature sensor
  int reading = analogRead(sensorPin);
  
  // converting that reading to voltage, for 3.3v arduino use 3.3
  float voltage = reading * 5.0;
  voltage /= 1024.0;
  
  // now print out the temperature C
  float temperatureC = (voltage - 0.5) * 100;
  
  // temp farenheit
  float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
  
  // converting from 10 mv per degree with 500 mV offset
  // to degrees ((voltage - 500mV) times 100)
  
  lcd.setCursor(0, 0);
  lcd.print(reading);
  lcd.setCursor(10, 0);
  lcd.print(voltage);
  lcd.setCursor(0, 1);
  lcd.print(temperatureC); // print temperature C
  lcd.setCursor(10, 1);
  lcd.print(temperatureF); // print temp F
  delay(1000);
  lcd.clear();
}
