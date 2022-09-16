/* Functions: Scope & Flexibility
 * How to Build Function Templates
 *
 * So how do we implement templates with actual code? Unlike regular functions,
 * templates are entirely created in header files.
 *
 * Templates let us choose the type implementation right when you call the 
 * function. The type we choose may apply to the return type, a parameter type,
 * or both.
 *
 * Here's how we could build a template for print_cat_ears() so that the 
 * parameter type is flexible:
 *
 * template <typename T>
 * void print_cat_ears(T item) {
 * 	std::cout << " " << item << "   " << item << " " << "\n";
 * 	std::cout << item << item << item << " " << item << item << item << "\n";
 * }
 *
 *
 * We can call the function for int, char, std::string, or double:
 *
 *
 * print_cat_ears(2);
 *
 * // the output:
 *   2   2
 *  222 222
 *
 *
 *  Now we can use print_cat_ears() with a parameter of any type we want, as 
 *  long as the type can be used with the methods expected. For example,
 *  we couldn' pass an std::vector into the current print_cat_ears() because
 *  << won't work with std::vector.
 *
 *  Note: Using templates will slow down the program's compile time, but speed
 *  up the execution time.
 *
 */

#include <iostream>
#include "08__numbers.hpp"

int main() {
	std::cout << get_smallest(100, 60) << "\n";
	std::cout << get_smallest(2543.2, 324.3) << "\n";
}

