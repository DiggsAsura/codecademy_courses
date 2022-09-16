/*
 * Two types of errors
 *
 * - Syntax error: Errors that occur when we violate the rules 
 *   of C++ syntax.
 *
 * - Type errors: Errors that occur when there are mismatch between the
 *   types we declared. 
 *
 *
 * Some common syntax errors: 
 *
 * - Missing semicolon;
 *
 * - Missing closing paranthesis ), square bracket [, or curly {
 *
 *
 * Some common type errors:
 *
 * - Forgetting to declare a variable
 *
 * - Storing a value into the wrong type
 *
 */

#include <iostream>
int main() {
  char answer;
  int score = 0;

  std::cout << "Who Wants To Be a Millionaire\n\n";

  std::cout << "For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Teat', 'Coke', and what?\n\n";

  std::cout << "A. Fresca   B. V8 \n";
  std::cout << "C. Yoo-hooo D. A&W \n\n";

  std::cout << "Enter your answer: ";
  std::cin >> answer;

  if (answer == 'A' || answer == 'a') {
    score = score + 100;
    std::cout << "Correct\n";
  }
}
