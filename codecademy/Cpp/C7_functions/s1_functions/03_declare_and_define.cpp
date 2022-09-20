/* Declase & Define
 *
 * Often, built-in functions aren't enough to tackle the wide array of 
 * programming challenges out there. But never fear: you can write your own
 * functions too!
 *
 * A C++ function is comprised of two distinct parts:
 *
 * - Declaration: this includes the function's name, what the return type is,
 *   and any parameters (if the function will accept input values, known as
 *   arguments).
 *
 * - Definition: also known as the body of the function, this contains the 
 *   instructions for what the function is supposed to do. 
 *
 * This is the overall structure: 
 *
 * return_type function_name( any, parameters, you, have) {
 * 	// Code block here
 * 	return output_if_there_is_any;
 * }
 *
 * This is what it might look like with real code:
 */

#include <iostream>

void make_sandwitch() {
	std::cout << "bread\n";
 	std::cout << "egg\n";
 	std::cout << "cheese\n";
 	std::cout << "avocado\n";
 	std::cout << "bread\n";
}

int main() {
	make_sandwitch();
}
 


