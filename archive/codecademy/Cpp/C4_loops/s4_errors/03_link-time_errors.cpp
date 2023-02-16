// Link-time Errors
//
// Sometimes the code compiles fine, but there is still a message
// because the program needs some function or library that
// it can't find. This is known as a link-time error. 
//
// As our program gets bigger, it is good practice to divide the
// program into separate files. After compiling them, the linker takes
// those separate object files and combins them into a single executable
// file. Lin-time errors are found by the linker when it is trying to
// combine files into an executeable file. 
//
// Some common link-time errors:
//
// - Using a function that was never defined (more on this later)
//
// - Writing Main() instead of main() 
//
// Here's an example of a link-time error message:
//
// .... In function '_start':
// blablabla: undifined refrence to 'main'
// collect2: error: ld return 1 exit satus
//
// These errors are more hard to find, but remember, Google is your
// friend! Here, a good Google search would be: "C++ undefined
// reference to main".
//
// (lol thanks CC).
//

#include <iostream>
using namespace std;

int main() {
  int num = 0;
  int sum = 0;

  cout << "Enter a number: ";
  cin >> num;

  for (int i = 1; i <= num; i++)
  {
    sum = sum + i;
    cout << i << " ";
  }
  cout << "\nSum: " << sum << "\n";
}
