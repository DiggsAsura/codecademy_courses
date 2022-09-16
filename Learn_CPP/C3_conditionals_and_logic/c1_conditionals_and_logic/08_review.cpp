// Review
//
// if statement
// if / else
// if / else if / if
// Relational operators
// switch statement
//

// optional Little Mac task :) 
//

#include <iostream>
using namespace std;

int main() {
  int weight;
  int planet;
  double mercury = 0.38; // 1
  double venus = 0.91;   // 2
  double mars = 0.38;    // 3
  double jupiter = 2.34; // 4
  double saturn = 1.06;  // 5
  double uranus = 0.92;  // 6
  double neptune = 1.19; // 7

  cout << "Whats your weight Little Mac? Enter weight: ";
  cin >> weight;

  cout << "Which planet (1-7): ";
  cin >> planet;

  switch (planet) {
    case 1:
      cout << "Weight on Mercury: " << weight * mercury << "\n";
      break;
    case 2:
      cout << "Weight on Venus: " << weight * venus << "\n";
      break;
    case 3:
      cout << "Weight on Mars: " << weight * mars << "\n";
      break;
    case 4:
      cout << "Weight on Juptier: " << weight * jupiter << "\n";
      break;
    case 5: 
      cout << "Weight on Saturn: " << weight * saturn << "\n";
      break;
    case 6:
      cout << "Weight on Uranus: " << weight * uranus << "\n";
      break;
    case 7:
      cout << "Weight on Neptune: " << weight * neptune << "\n";
      break;
    default:
      cout << "No match\n";
  }
  
}
