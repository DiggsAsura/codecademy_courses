// Before we dive deep into the syntax of the if statement, let's do a demo
//
// Here we have coinflip.cpp program that ismulates a coin toss:
// * 50% of the time, it's Heads
// * 50% of the time, it's Tails
//
// Note to self. Notice the sweet modulo usage

#include <iostream>
#include <stdlib.h>
#include <ctime>
using namespace std;

int main() {
  // Create a number that's 0 or 1
  srand (time(NULL));
  int coin = rand() % 2;
  cout << coin << "\n";

  // If number is 0: Heads
  // If number is not 0: Tails

  if (coin == 0) {
    cout << "Heads\n";
  }
  else {
    cout << "Tails\n";
  }
}
