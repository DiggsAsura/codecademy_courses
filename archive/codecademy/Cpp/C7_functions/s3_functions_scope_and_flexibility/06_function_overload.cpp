/* Functions: Scrope & Flexibility
 * Function Overload!
 *
 * What if you want a function to accept an argument that can be either an int
 * OR a double? Or what if you want some function parameters to be optional?
 * C++ has a trick up its sleeve just for such situations.
 *
 * In a process known as function overloading, you can give mulitple C++
 * functions the same name. Just make sure at least one of these conditions 
 * is true:
 *
 * 	- Each has different type parameters.
 *
 * 	- Each has a different number of parameters.
 *
 * Overloading enables you to change the way a function behaves depending on 
 * what is passed in as an argument:
 *
 * 
 * void print_cat_ears(char let) {
 * 	std::cout << " " << let << "  " << let << " " << "\n";
 * }
 *
 * void print_cat_ears(int num) {
 * 	std::cout << " " << num << "  " << num << " " << "\n";
 * }
 *
 *
 * Given the above functions, you could call the functions like so and C++ 
 * will know what to do:
 *
 *
 * print_cat_ears('A');
 * print_cat_ears(4);
 *
 * Output:
 *
 *   A    A
 *  AAA  AAA
 *
 *   4    4
 *  444  444
 */

// In short. You can have a funciton accept different type values, or different
// lenght of arguments: but you by overloading, aka two functions with the same
// name.

#include <iostream>
#include "06__num_ops.hpp"

int main() {
	std::cout << fancy_number(12, 3) << "\n";
	std::cout << fancy_number(12, 3, 19) << "\n";
	std::cout << fancy_number(13.5, 3.8) << "\n";
}
