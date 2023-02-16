// Swith = Match in rust!
//

// The case keyword checks if the expression matches.. 
//
// The break keyword tells the computer to exit the block and not execute any more code or check any other cases inside the code block
//
// At the end of each switch statement, there is a default statement. If none of the cases are true, then the code in the default statement (_ in Rust) statement will run. It's essentially the else part.

#include <iostream>
using namespace std;

int main() {
  int number = 9;

  switch(number) {
    case 1:
      cout << "Bulbasaur\n";
      break;
    case 2:
      cout << "Ivysaur\n";
      break;
    case 3:
      cout << "Venusaur\n";
      break;
    case 4:
      cout << "Charmander\n";
      break;
    case 5:
      cout << "Charmeleon\n";
      break;
    case 6:
      cout << "Charizard\n";
      break;
    case 7:
      cout << "Squirtle\n";
      break;
    case 8:
      cout << "Wartortle\n";
      break;
    case 9:
      cout << "Blastoise\n";
      break;

    default:
      cout << "Unkonwn\n";
  }
}
