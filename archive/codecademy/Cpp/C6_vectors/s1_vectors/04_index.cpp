/* Index
 *
 * Now that we have a vector, how do we access an individual element?
 * This is where index comes into play. 
 *
 * An index refers to an element's position within an ordered list. 
 * Vectors are 0-indexed, meaning the first element has index 0, the
 * second index 1, and so on.
 *
 * For example, suppose we have a char vector with all the vowels: 
 *
 * std::vector<char> vowels = {'a', 'e', 'i', 'o', 'u'};
 *
 * It would look something like this:
 *
 * | a | e | i | o | u |
 *
 * - The character at index 0 is 'a'
 * - The character at index 1 is 'e'
 *   ..
 *   ..
 *
 * To output each of the elements, we can do: 
 *
 * std::cout << vowels[0] << "\n";
 * std::cout << vovels[1] << "\n";
 * ...
 * ...
 *
 * Using the notation vector[index] with square brackets after the vector
 * name and the elemtn's index number inside.
 *
 * This will output:
 * a
 * e
 * i
 * o
 * u
 *
 */

#include <iostream>
#include <vector>

int main() {
  std::vector<double> subway_adult = {800, 1200, 1500};
  std::vector<double> subway_child = {400, 600, 750};

  std::cout << subway_child[2] << "\n";
}
