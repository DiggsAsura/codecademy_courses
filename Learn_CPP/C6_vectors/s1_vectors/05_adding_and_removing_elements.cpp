/* Adding and Removing Elements
 *
 * Often, we start with a vector that's either empty or a certain
 * length. As we read or compute data we want, we can grow the vector
 * as needed. 
 *
 *
 * .push_back() 
 *
 * To add a new element to the "back", or the end of the vector, we can
 * use the .push_back() function.
 *
 * For example, suppose we have a vector called dna with three 
 * letter codes of nucleotides:
 *
 * std::vector<std::string> dna = {"ATG", "ACG"};
 *
 * dna.push_back("GTG");
 * dna.push_back("CTG");
 *
 *
 * .pop_back() 
 *
 * You can also remove elements from the "back" of the vector using
 * .pop_back(). 
 *
 * dna.pop_back() 
 *
 * Notice how nothing goes inside the parantheses.
 *
 * Note: If you have programmed in other languages, be aware that
 * .popback() has no return value in C++.
 *
 */

#include <iostream>
#include <vector>

int main() {
  std::vector<std::string> last_jedi;

  last_jedi.push_back("kylo");
  last_jedi.push_back("rey");
  last_jedi.push_back("luke");
  last_jedi.push_back("finn");

  std::cout << last_jedi[0] << " ";
  std::cout << last_jedi[1] << " ";
  std::cout << last_jedi[2] << " ";
  std::cout << last_jedi[3] << " \n";
}
