/* How Parameters & Arguments Work
 *
 * A function with parameters has a couple of requirements:
 *
 * - The function call must include the same number of arguments as there
 *   are parameters.
 * - The corresponding arguments must be passed in the same order.
 * 
 * By calling a function with arguments, you are telling a function, "Hey 
 * function, when you execute, use these values where you have parameters
 * in your definition". 
 *
 * While it executes, anywhere the function comes across a parameter, it 
 * replaces the parameter with the corresponding argument you gave it.
 *
 */

#include <iostream>

std::string make_sandwich(std::string ing1, std::string ing2) {
	std::string sandwich = "";

	sandwich += "bread\n";
	sandwich += ing1 + "\n";
	sandwich += ing2 + "\n";
	sandwich += "bread\n";

	return sandwich;
}

int main() {
	std::cout << make_sandwich("peanut butter", "jelly");
}
