// Codecademy Learn C++
// Rock, Paper, Scissors, Lizard, Spock

/*
Rock, Paper, Scissors, Lizard, Spock...
*/

#include <iostream>
#include <stdlib.h> // for random numbers
using namespace std;

int main() {
  srand (time(NULL)); 
  int user = 0;
  int computer = rand() % 3 + 1;

  cout << "============================\n";
  cout << "rock paper scissors!\n";
  cout << "============================\n";

  cout << "1) Rock\n";
  cout << "2) Paper\n";
  cout << "3) Schissor\n";

  cout << "shoot! ";

  cin >> user;


  switch (user) {
    case 1:
      switch (computer) {
        case 1:
          cout << "Rock vs Rock: Tie!\n";
          break;
        case 2:
          cout << "Rock vs Paper: You loose...\n";
          break;
        case 3:
          cout << "Rock vs Scissor: You win!\n";
          break;
      }
      break;
    case 2:
      switch (computer) {
        case 1:
          cout << "Paper vs Rock: You win!\n";
          break;
        case 2:
          cout << "Paper vs Paper: Tie!\n";
          break;
        case 3:
          cout << "Paper vs Scissor: You loose...\n";
          break;
      }
      break;
    case 3:
      switch (computer) {
        case 1:
          cout << "Scissor vs Rock: You loose...!\n";
          break;
        case 2:
          cout << "Scissor vs Paper: You win!\n";
          break;
        case 3:
          cout << "Scissor vs Scissor: Tie!\n";
          break;
      }
      break;
  }
}
