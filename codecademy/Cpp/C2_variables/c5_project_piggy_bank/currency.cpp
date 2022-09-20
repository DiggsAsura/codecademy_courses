// Small project
// Currency converter
// CodeCademy Learn C++

#include <iostream>
using namespace std;

int main() {
  double pesos, reais, soles, dollars;

  // Colombian Pesos:
  cout << "Enter number of Colombian Pesos: ";
  cin >> pesos;

  // Brazilian Reais:
  cout << "Enter number of Brazilian Reais: ";
  cin >> reais;

  // Peruvian Soles:
  cout << "Enter number of Peruvian Soles: ";
  cin >> soles;


  // Rates
  // 1 pesos = 0.05 usd 
  // 1 reais = 0.19 usd
  // 1 soles = 0.26 usd

  dollars = 0.05 * pesos + 0.19 * reais + 0.26 * soles;
  cout << "Total USD = $" << dollars << "\n";
}
