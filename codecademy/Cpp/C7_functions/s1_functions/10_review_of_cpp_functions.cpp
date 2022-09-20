/* Review of C++ Functions
 *
 * Wow! Check out all you've learned about C++ functions:
 *
 * 	- A function is a named group of statements that do something
 * 	together.
 *
 * 	- Functions allow you to create more flexible, modular, and DRY code.
 *
 * 	- C++ has many built-in functions that you can use.
 *
 * 	- Functions are called like function_name();
 *
 * 	- A function has a declaration with a return type and possible 
 * 	parameters.
 *
 * 	- A function has a definition (or body) with a group of statements and
 * 	a possible return value.
 *
 * 	- void functions do not have return values.
 *
 * 	- Functions with a return value have return statements.
 *
 * 	- Parameters are variables used as placeholders for function input
 * 	values.
 *
 * 	- Arguments are a function's actual input values.
 *
 * You now know enough C++ to create some pretty cool projects on your own.
 * But, as you'll see, there are still many ways to improve your code!
 *
 */

#include <iostream>

std::string intro() {
	std::string on_off_attempt;
	std::cout << "Hello. IT.\n";
	std::cout << "Did you try turn it off and on again? (y/n): ";
	std::cin >> on_off_attempt;

	return on_off_attempt;
}

int main() {
	intro();
	std::cout << "Oh hi Jen!\n";
	intro();
	std::cout << "You stole the stress machine? But that's stealing!\n";
	intro();
}
