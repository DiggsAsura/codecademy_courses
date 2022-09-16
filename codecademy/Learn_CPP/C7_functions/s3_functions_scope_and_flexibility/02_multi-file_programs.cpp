/* Functions: Scope & Flexibility
 * Multi-File Programs
 *
 * Programs can grow quickly. With a few functions, you can declare the function
 * above main() and then you can define the function below main() like this:
 *
 * #include <iostream>
 *
 * // Declaration at the top:
 * void();
 *
 * int main() {
 * 	eat();
 * }
 *
 * // Definition at the bottom:
 * void eat() {
 * 	std::cout << "nom nom nom\n";
 * }
 *
 *
 * But this isn't ideal when your code gets longer; it's common to use the same
 * function in more than one .cpp file.
 *
 * To make your code cleaner and more modular, you can move the function 
 * definitions over to another specialized .cpp file (e.g., my_functions.cpp), 
 * leavning a list of declarations above main().
 *
 * But files, like functions, have scope. So, how does the main() program know
 * about the function definitions?
 *
 * Before your program even compiles, it links together any files you list
 * in your compilation statement into a single executable:
 *
 * g++ main.cpp my_functions.cpp
 *
 * And voila! Your program knows the function definitions. 
 *
 */

#include <iostream>
#include <cmath>

// Add declarations - aka the function with parameters
double average(double num1, double num2);
int tenth_power(int num);
bool is_palindrome(std::string text);

int main() {
	std::cout << is_palindrome("racecar") << "\n";
	std::cout << tenth_power(3) << "\n";
	std::cout << average(8.0, 19.0) << "\n";
}
