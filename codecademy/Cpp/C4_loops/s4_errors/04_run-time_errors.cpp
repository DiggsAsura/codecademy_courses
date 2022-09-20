// Run-time Errors
//
// If our program has no compile-time errors and no link-time errors,
// it'll run. This is where the fun really starts.
//
// Errors which happen during program execution (run-time) after successful
// compilation are called run-time errors. Run-time errors occur
// and link-time errors asks the computer to do something that the computer
// is unable to reliably do. 
//
// It happens after we give the ./ execute command:
//
// ./a.out
//
// Some common run-time errors:
//
// - Division by zero also known as division error. These types of
//   error are hard to find as the compiler doesn't point to the line
//   at which the error occurs. 
//
// - Trying to open a file that doesn't exist
//
// There is no way for the compiler to know about these kinds of errors
// when the program is compiled. 
//
// Here's an example of a run-time error message:
//
// g++ example.cpp
// ./a.out
// Floating point exception (core dumped)
//
//
// Clear as mud. Is Rust this bad? 
//

#include <iostream>

int main() 
{
  int width = 100;
  int length = 90;

  int ratio = width / length;

  std::cout << ratio << "\n";
}
