/* Functions: Scope & Flexibility
 * Getting a Header Yourself
 *
 * If your program keeps growing, you may have to scroll through many 
 * declarations before you see main(). That doesn't seem like the best way to
 * to do things. Plus you don't want to keep declaring the same functions over
 * and over for different files - making changes would be incredibly tiresome!
 *
 * Well, you can take those function declarations and move them all over to a
 * header file, another file - usually with the same name as the file with all
 * of the function definitions - with the extension .hpp or .h. For example,
 * if your function definition are in my_functions.cpp, the corresponding
 * header file would be my_functions.hpp or my_functions.h.
 *
 * So how do you bring everything from a header file into scoope for another 
 * file? Do you just link the header in the compilation statement like you
 * did with the second .cpp file?
 *
 * As it turns out, with headers, you can just add #include "my_functions.hpp"
 * to the very top of main.cpp:
 *
 * #include "my_functions.hpp"
 *
 *
 * Boom! This line pastes in everything from my_functions.hpp. Now you have
 * access to all of the functions declarations you stowed away in your
 * header.
 *
 */

#include <iostream>
#include "03__fns.hpp"

int main() {
	std::cout << is_palindrome("noon") << "\n";
	std::cout << tenth_power(4) << "\n";
	std::cout << average(4.0, 7.0) << "\n";
}

