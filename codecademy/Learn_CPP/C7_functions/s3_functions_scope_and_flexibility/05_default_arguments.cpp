/* Functions: Scope & Flexibility
 * Default Arguments
 *
 * If you add a parameter to a function in C++, then an argument will be 
 * required when you call the function. What does "required" mean here? Well,
 * you'll get an error. But what if 9 times out of 10, you know you'll use the
 * same input value? It would be really annoying to have to enter the same
 * value over and over again.
 *
 * To make your code more flexible for situations like this, you can add 
 * default arguments to your function declarations. Default arguments are
 * values assigned to parameters when the function is declared and defined:
 *
 * // Declaration
 * void intro(std::string name, std::string lang = "C++");
 *
 * // Definition
 * void intro(std::string name, std::string lang) {
 * 	std::cout << "Hi, my name is " << name << " and I'm learning " << lang << ".\n";
 * }
 *
 * Then, if you leave the argument blank in your function call, instead of an
 * error, your function will run with the default value.
 * Meanwhile, if you DO have an argument to add when you call the function, that
 * argument will replace the default argument when your code executes.
 *
 * Either of these will work for the function we defined:
 *
 * intro("Mariel")
 * // "Hi my name is Mariel and I'm learning C++"
 *
 * intro("Mariel", "Python")
 * // "Hi, my name is Mariel and I'm learning Python."
 *
 * 
 * Important! Your computer cannot read your mind; it determines which arguments
 * corresponds with which parameter based on ORDER.
 *
 * Parameters with default arguments come first. This Will work for add_nums(3);
 * because the computer knows 3 corresponds to num1:
 *
 * int add_nums(int num1, int num2 = 0);
 *
 *
 * But the following does NOT work for add_num(3); the computer assumes that
 * 3 still corresponds to num1:
 *
 * int add_nums(int num1 = 0, int num2);
 *
 * Similarly, when a function has two default arguments, you still need to call
 * both arguments - if BOTH of the following are true:
 *
 * 	- The first argument IS the default value
 * 	- The second argument is NOT the default value.
 *
 */

#include <iostream>
#include "05__coffee.hpp"

int main() {
	// coffe black
	std::cout << make_coffee();

	// coffee with milk
	std::cout << make_coffee(true);

	// coffee with milk and sugar
	std::cout << make_coffee(true, true);

	// coffee with sugar
	std::cout << make_coffee(false, true);
}
