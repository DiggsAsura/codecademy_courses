// if (condition)
// else if (condidtion
// else


#include <iostream>

int main() {
  double ph = 4.6;

  // Write the if, else if, else here: 
  if (ph > 7) {  // GREATER - fuck i mix up < > still
    std::cout << "Basic\n"; 
  }
  else if (ph < 7) {  // LESSER
    std::cout << "Acidic\n";
  }
  else {
    std::cout << "Neutral\n";
  }
}
