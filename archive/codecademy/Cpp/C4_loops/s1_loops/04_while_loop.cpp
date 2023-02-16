#include <iostream>
using namespace std;

int main() {
  int i = 0;
  int square = 0;

  while (i < 10) {
    square = i * i;
    cout << i << " " << square << "\n";
    i++;
  }
}
