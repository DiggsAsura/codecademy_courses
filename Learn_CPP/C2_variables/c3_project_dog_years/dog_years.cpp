#include <iostream>
using namespace std;

int main() {
  int dog_age = 120238;
  int early_years, later_years, human_years;

  // First 2 years for a dog is considered 21 years for a human
  early_years = 21;

  // Each following year is considered 4 human years
  later_years = 4;

  human_years = later_years + early_years;

  cout << "My name is Doggystyle! Ruff Ruff! I am " << human_years << " years old in human years.\n";
}
