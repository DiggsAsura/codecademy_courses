/* Parameters & Arguments
 *
 * Returning data is all well and good, but let's say you're visiting NYC and
 * you've been told that New Yorkers usually add a 20% tip for resurants and
 * taxis. It would be really convenient if you could just build a function that 
 * accepts different prices as input and figured out how much you should tip.
 *
 * As it happens, you can do that with parameters. Parameters (sometimes called
 * formal parameters) are variables used in a function's definition. They act
 * as placeholders for the input values you'll use during your function call.
 *
 * Parameters vs arguments
 * In the function below, price is the function's parameter and it's a double.
 * It is declared between the parentheses and then used in the body of the 
 * function.
 *
 * double get_tip(double price) {
 * 	return price * 0.2;
 * }
 *
 * Then, when you're ready to use your function, the value you pass to the 
 * function is called an argument (also known as an actual parameter). In this
 * case, 15.75 is the argument that is passed to the function:
 *
 *
 * double tip = get_tip(15.75);
 * 	// tip would be 3.15
 *
 *
 * ------------------------------------
 * int do_something(int PARAMETER) {
 * 	// stuff happens
 * }
 * do_something(ARGUMENT);
 * ------------------------------------
 *
 */

#include <iostream>

// Define get_emergency_number()
void get_emergency_number(std::string emergency_number) {
	std::cout << "Dial " << emergency_number << "\n";
}

int main() {
	// Original emergency services number
	std::string old_emergency_number = "9999";

	// For nicer ambulances, faster response times and better
	// looking drivers:
	std::string new_emergency_number = "1234 232 141 523 223 533 4";

	// Call get_emergency_number() below with the number you want!
	get_emergency_number(new_emergency_number);
}
