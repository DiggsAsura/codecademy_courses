/* How Return Values Work
 *
 * When functions have a return type other than void, the function has two new 
 * requirements:
 *
 * - There must be a value returned from the function.
 *
 * - The return value must be the same type as the function's return type.
 *
 * But where does the return value get returned to?
 *
 * It gets returned to the place where the function is called. For example,
 * if you have the following function:
 *
 *
 * std::string feed_the_cat() {
 * 	return "Cat is fed!";
 * }
 *
 *
 * And then print the function call inside of main():
 *
 * int main() {
 * 	std::string cat_message = feed_the_cat();
 * 	std::cout << cat_message;
 * }
 *
 * The return value of the function is what gets printed to the terminal. 
 */

#include <iostream>

bool morning = true;

std::string make_sandwich() {
	std::string sandwich = "";
	sandwich += "bread\n";
	if (morning == true) {
		sandwich += "egg\n";
	}
	sandwich += "cheese\n";
	sandwich += "bread\n";
	return sandwich;
}

int main() {
	std::cout << "Your sandwich now:\n" << make_sandwich() << "\n";
}
