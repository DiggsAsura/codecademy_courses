/* Code Challenge: C++ Functions
 * Average
 *
 * Write a function average() that takes:
 *
 * 	- A double parameter named num1
 *
 * 	- A double parameter named num2
 *
 * The function should return a double that is the average of the arguments
 * passed in. 
 *
 */

#include <iostream>

double average(double num1, double num2) {
	return (num1 + num2) / 2;
}

int main() {
	std::cout << average(42.0, 24.0) << "\n";
	std::cout << average(1.0, 2.0) << "\n";
}

