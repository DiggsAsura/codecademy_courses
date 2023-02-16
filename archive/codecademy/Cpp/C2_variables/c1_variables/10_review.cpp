#include <iostream>
#include <string>
using namespace std;

int main() {
  string words = "hello ";
  string name;

  cout << "Whats your name: ";
  cin >> name;
  cout << words << name << "\n";
}
