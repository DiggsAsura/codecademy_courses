/* Functions: Scope & Flexibility
 * Function Templates
 *
 * Overloading can be really tedious. Imagine you want to create a new function
 * that works with int, float, double and other number types.
 * Do you really need to redefine the SAME function body over and over again
 * with different parameters?
 *
 * Thankfully not! When two functions have different types but the same body - 
 * as was the case with print_cat_ears() - , there is a cleaner solution you
 * can use: templates.
 *
 * A template is a C++ tool that allows programmers to add data types as
 * parameters.
 *
 * This feature comes in handy for classes as well as for functions. In fact,
 * std::string and std::vector are both template-based types. The C++ 
 * standard library is full of templates!
 *
 * https://en.cppreference.com/w/cpp/header
 *
 */

// T add_together()
//
// omg is THAT what T is? Is that the same in Rust?
