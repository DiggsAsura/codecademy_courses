/*
 * Ok so this is a bit different than python and rust afaik.
 *
 * Initializing a Vector
 *
 * Now we know how to create a vector, we can also initialize a vector,
 * giving it values, as we are creating it in the same line. 
 *
 * For example, instead of just creating a double vector named 
 * location:
 *
 * std::vector<double> location;
 *
 * We can create AND initialize location with specific values (similar
 * to variables tbh):
 *
 * std::vector<double> location = {42.123123, -73.23213}
 *
 * Note the curlies 
 *
 * Here, we are storing a latitude and a longitude. 
 *
 * Another way we can initialize our vector is by presizing, or 
 * setting the size. 
 *
 * Suppose we want to create and initialize a vector with two elements.
 * However, we don't know what the values we want to add yet: 
 *
 * std::vector<double> location(2);
 *
 * Here, we are creating a double vector and setting the initial size
 * to two using parantheses. 
 *
 * It would look something like this: 
 *
 * |   0.0   |   0.0  |
 *
 * Because 0.0 is the default value for double.
 *
 */

#include <iostream>
#include <vector>

int main() {
  std::vector<double> subway_adult = {800, 1200, 1500};
  std::vector<double> subway_child = {400, 600, 750};
}
