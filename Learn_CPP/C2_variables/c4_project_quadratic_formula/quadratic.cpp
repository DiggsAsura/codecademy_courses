// Quadratic formula
//
// In algebra, a quadratic equation is an equation having the form:
// ax**2 + bx + c = 0
//
// In a graph (cant write here) - The corresponding x values are the x-intercepts of 
// the graph, while a, b and c are constants.
//
// Write a C++ program called quadratic.cpp that solves the quadratic equation for the
// x's:
//
// fuck it i cant type the formula which is listed here: 
// https://www.codecademy.com/courses/learn-c-plus-plus/projects/cpp-quadratic-formula
//
//

#include <iostream>
#include <cmath>
using namespace std;

int main() {
  double a, b, c;

  cout << "Enter a: ";
  cin >> a;
  cout << "Enter b: ";
  cin >> b;
  cout << "Enter c: ";
  cin >> c;

  double root1, root2;
  
  // now get the root with std::sqrt()
  // f.x std::sqrt(9) would be 3
  root1 = (-b + sqrt(pow(b, 2) - 4*a*c)) / (2*a);
  root2 = (-b - sqrt(pow(b, 2) - 4*a*c)) / (2*a);

  cout << root1 << "\n";
  cout << root2 << "\n";

}
