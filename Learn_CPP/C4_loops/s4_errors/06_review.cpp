/* Review
 *
 * Finding bugs is a huge part of a programmer's life. Don't be 
 * intimdated by them... embrace them. Errors in your code means you're
 * trying to do something cool!
 *
 * In this lesson, we have learned about the four types of C++ errors:
 *
 * - Compile-time errors: Errors ound by the compiler
 *
 * - Link-time errors: Errors found by the linker when it is trying 
 *   to combine object files into an executeable program.
 *
 * - Errors found by the programmer looking for the causes of errenous
 *   results.
 *
 * Remember, Google and Stack Overflow are a programmer's best friends.
 * For some more motivation, check out this blog post: Thinking About 
 * Errors in Your Code Differently:  https://news.codecademy.com/errors-in-code-think-differently
 *
 *
 * TIP: If you encounter a long error message, always scrool to the top 
 * tro try debug the very first bug.
 */

#include <iostream>
#include <stdlib.h>
#include <ctime>
using namespace std;

int main() {
  srand (time(NULL));
  int fortune = rand() % 10;

  switch (fortune) {
    case 0:
      cout << "Flattery will go far tonight.\n";
      break;
    case 1:
      cout << "Don't behave with cold manners.\n";
      break;
    case 2:
      cout << "May you someday be a carbon neutral.\n"; 
      break;
    case 3:
      cout << "You have rice in your teeth.\n";
      break;
    case 4:
      cout << "A conclusion is simply the place where you got tired o thinking.\n";
      break;
    case 5:
      cout << "No snowflake feels responsible in an avalanche.\n";
      break;
    case 6:
      cout << "He who laughs last is laughint at you.\n";
      break;
    case 7:
      cout << "If you look back, you'll soon be going that way.\n";
      break;
    case 8:
      cout << "You will die alone and poorly dressed.\n";
      break;
    case 9:
      cout << "The fortune you seek is in another cookie.\n";
      break;
    default:
      cout << "Invalid fortune: " << fortune << "!\n";
      break;
  }
}
