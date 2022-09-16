// && and
// || or
// ! not

#include <iostream>
using namespace std;

int main() {

  int year;
  cout << "Type the year you want to check for leap year: ";
  cin >> year;
  

  if (year > 999 && year < 10000) {
    // check if leap year
    cout << year << "\n";
    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
      cout << "Leap year!\n";
    }
    else {
      cout << "Not a leap year\n";
    }
  }
  else {
    cout << "Mistyped? Try again\n";
  }

}
