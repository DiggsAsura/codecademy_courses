/* Code Challenge: C++ Functions
 * Water Plant
 *
 * Define a function needs_water() that accepts:
 *
 * 	- An int number of days since the previous watering.
 *
 * 	- A bool value is_succulent. (A value of true would indicate
 * 	  that the plant is a succulent.)
 *
 * Inside the function, you'll need some conditional logic:
 *
 * 	- If is_succulent is false and days is greater than 3,
 * 	return  "Time to water the plant.".
 *
 * 	- If is_succulent is true and days is 12 or less, return
 * 	"Don't water the plant!".
 *
 * 	- If is_succulent is true and days is greater than or equal
 * 	to 13, return "Go ahead and give the plant a little water.".
 *
 * 	- Otherwise, return "Don't water the plant!".
 *
 * Note: Don't print the string:
 * return them from the function.
 *
 */

// This seems like the ultimate test so far haha. Let's see if we can do it. 

//#include <iostream>
//
//std::string needs_water(int days, bool is_succulent) {
//
//	std::string answer;
//
//	if (is_succulent == false && days < 3) {
//		answer = "Time to water the plant.\n";
//	} 
//	else if (is_succulent == true && days > 12) {
//		answer = "Don't water the plant!\n";
//	}
//	else if (is_succulent == true && days < 13) {
//		answer = "Go ahead and give the plant a little water.\n";
//	} else {
//		answer = "Don't water the plant!\n";
//	}
//	return answer;
//}
//
//int main() {
//	std::cout << needs_water(10, false) << "\n";
//}
//
// Wrong. Wrong < > and could do it way esier. Above is my attempt, below is the// answer 

#include <iostream>

std::string needs_water(int days, bool is_succulent) {
	if (days > 3 && is_succulent == false) {
		return "Time to water the plant.";
	} else if (days < 13 && is_succulent) {
		return "Don't water the plant!";
	} else if (days >= 13 && is_succulent) {
		return "Go ahead and give the plant a little water.";
	} else {
		return "Don't water the plant!";
	}
}

int main() {
	std::cout << needs_water(10, false) << "\n";
}
