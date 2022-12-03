#include <LiquidCrystal.h>

// Initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
  // set up lcd
  lcd.begin(16,2);
  // print to display
  lcd.print("Hello world!");
}

void loop()
{
  // set the cursor to column 0, line 1
  // Note: line 1 is the second row, since counting begins at 0
  lcd.setCursor(0,1);
  // print the number of seconds since reset:
  lcd.print(millis() / 1000);
}
