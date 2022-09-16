/* Tackling Multiple Arguments
 *
 * Hang on, you may be thinking, are you limited to one parameter per function?
 * Not at all! You can add as may as you like, but you will have to remember
 * their order when you call the function. 
 * 		(Ok so unlie Python?)
 *
 * double get_tip(double price, double tip, bool total_included) {
 * 	if (total_included) {
 * 		return price * tip + price;
 * 	} else {
 * 		return price * tip;
 * 	}
 * }
 *
 * So here we have three parameters:
 * - double price
 * - double tip
 * - bool total_included
 *
 * When calling get_tip(), it's important to call it with price first, tip
 * second and return_total last:
 *
 *
 * get_tip(0.25, true, 45.50);
 * // this code will not work);
 *
 * get_tip(45.50, 0.25, true);
 * // this code result in 56.875, which you could round up to 56.88
 *
 */

#include <iostream>

void name_x_times(std::string name, int x) {
	while (x > 0) {
		std::cout << name << "\n";
		x--;
	}
}

int main() {
	name_x_times("kenneth", 10);
}
