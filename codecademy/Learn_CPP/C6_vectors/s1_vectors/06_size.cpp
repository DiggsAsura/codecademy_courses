/* .size()
 *
 * <std::vector> not only stores the elements; it also stores the size
 * of the vector:
 *
 * The .size() function returns the number of elements in the vector.
 *
 * For example, suppose we have a std::string vector with Sonny's grocery
 * list:
 *
 * std::vector<std::string> grocery = {"Hot Pepper Jam", "Dragon Fruit", "Brussel Sprouts"};
 *
 * - The string at index 0 is "Hot Pepper Jam"
 * - The string at index 1 is "Dragon Fruit"
 * - The string at index 2 is "Brussel Sprouts"
 *
 * std::cout << grocery.size() << "\n";
 *
 * will return
 *
 * 3
 *
 * Notice how nothing goes in the parentheses. 
 *
 */

#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> grocery = {"Hot Pepper Jam", "Dragon Fruit", "Brussel Sprouts"};

  grocery.push_back("Bananas");
  grocery.push_back("Aquavit");

  std::cout << grocery.size() << "\n";
}
