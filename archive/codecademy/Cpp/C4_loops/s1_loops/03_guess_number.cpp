// Guess Number

#include <iostream>
using namespace std;

int main() {
  int guess;
  int tries = 0;

  cout << "I have a number 1-10.\n";
  cout << "Please guess it: ";
  cin >> guess;

  while (guess !=8 && tries < 5) {
    cout << "Wrong number, try again: ";
    cin >> guess;
    tries++;
  }

  if (guess == 8) {
    cout << "Nailed it.\n\n";
  }
}
