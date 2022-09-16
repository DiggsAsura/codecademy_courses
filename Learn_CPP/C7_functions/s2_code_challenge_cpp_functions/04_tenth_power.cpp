/* Code Challenge: C++ Functions
 * Tenth Power
 *
 * Write a function named tenth_power() that has:
 *
 * 	- An int parameter named num.
 *
 * The function should return num raised to the 10th power.
 *
 */

#include <iostream>
#include <cmath>

int tenth_power(int num) {
	return pow(num, 10);
}

int main() {
	std::cout << tenth_power(0) << "\n";
	std::cout << tenth_power(1) << "\n";
	std::cout << tenth_power(2) << "\n";
	std::cout << tenth_power(1001) << "\n";
}
