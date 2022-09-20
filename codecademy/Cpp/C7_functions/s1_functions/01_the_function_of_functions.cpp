/*
 * There are some great reasons to use functions:
 *
 * - A single line can make all that code fire off instead of a whole bunch 
 *   of lines
 *
 * - You can build DRY (Don't Repeat Yourself) code, reusing the code you 
 *   already wrote.
 *
 * - Functions make your code flexible and modular, meaning you can group
 *   your code more easily by task. 
 *
 * In fact, every C++ program has at least one function. "Hold on", you might
 * be thinking, "I've written some C++ programs, but I haven't written any 
 * functions yet!"
 *
 * Well: main()
 *
 */

// Task just demonstrates a code which could def been written shorter.
// copy/paste

#include <iostream>

int main() {
  
  // Conduct IT support
  std::string on_off_attempt;
  std::cout << "Hello. IT.\n";
  std::cout << "Have you tried turning it off and on again? y/n\n";
  std::cin >> on_off_attempt;
  
  // Check in with Jen
  std::cout << "Oh hi Jen!\n";
  
  // Conduct IT support again...
  std::cout << "Hello. IT.\n";
  std::cout << "Have you tried turning it off and on again? y/n\n";
  std::cin >> on_off_attempt;

  // Check in with Roy
  std::cout << "You stole the stress machine? But that's stealing!\n";
  
  // Conduct IT support yet again...zzzz...
  std::cout << "Hello. IT.\n";
  std::cout << "Have you tried turning it off and on again? y/n\n";
  std::cin >> on_off_attempt;
  
}
