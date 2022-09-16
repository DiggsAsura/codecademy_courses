/*
 * Void - The Point of No Return
 *
 * Let's build a simple function with no input and no output. We can do that?
 *
 * Enter the void specifier, which is added in the function declaration before
 * the function name. A void function, also known as a subroutine, has no
 * return value, making it ideally suited for situations where you just want
 * to print stuff to the terminal.
 *
 * For example:
 *
 * void animal_chat() {
 * 	std::string fav, pet;
 *
 * 	std::cout << "What's your favorite animal?\n";
 * 	std::cin >> fav;
 *
 * 	std::cout << "Do you have a " << fav << " as a pet? y/n\n";
 * 	std::cin >> pet;
 *
 * 	if (pet == "y") {
 * 		std::cout << "How lucky you have a " << fav << " as a pet!\n";
 * 	} else {
 * 		std::cout << "That's too bad.\n";
 * 	}
 * }
 *
 * The above chat program is built to capture user responses and print to the
 * terminal without returning any values.
 */

#include <iostream>

void oscar_wilde_quote() {
	std::cout << "The highest, as the lowest, form of criticism is a mode of autobiography.\n";
}

int main() {
	oscar_wilde_quote();
}
