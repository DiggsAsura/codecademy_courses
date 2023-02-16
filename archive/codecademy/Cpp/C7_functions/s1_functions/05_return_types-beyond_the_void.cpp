/* Return Types - Beyond the Void
 *
 * When you do in fact want your function to return something and pass
 * information back to the rest of your program, C++ has you covered.
 * Just like there are many variable types, there are many different return
 * types for functions.
 *
 * A function can return most data types we've covered, including double,
 * int, bool, char, std::string, and std::vector.
 *
 *
 * std::string always_blue() {
 *
 * 	return "blue!\n";
 *
 * }
 *
 *
 * Note: The return statement is the last line of code that a function
 * will execute. For example:
 *
 *
 * std::string always_blue() {
 * 	return "blue!\n";
 * 	std::cout << "Returned blue!";
 * }
 *
 *
 * The final line will not execute because a value has already been 
 * returned. So "Returned blue!" won't be printed to the terminal. 
 */

#include <iostream>

// Change needs_it_support so that it returns support:
bool needs_it_support() {
	bool support;

	std::cout << "Hello. IT. Have you tried turning it off and on again? Enter 1 for yes, 0 for no. \n";
	std::cin >> support;
	return support;
}

int main() {
	// Change the following line to print the fucntion result:
	std::cout << needs_it_support() << "\n";
}
