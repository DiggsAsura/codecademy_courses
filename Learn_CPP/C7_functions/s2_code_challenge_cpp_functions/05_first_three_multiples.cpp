/* Code Challenge: C++ Functions
 * First Three Multiples
 *
 * Write a function named first_three_multiples() that has:
 *
 * 	- An int parameter named num
 *
 * The function should return an std::vector of the first three multiples of
 * num in ascending order.
 *
 * For example, first_three_multiples(7) should return a vector with 7, 14 
 * and 21
 *
 */
#include <iostream>
#include <vector>

// Define first_three_multiples() here:
std::vector<int> first_three_multiples(int num) {

  std::vector<int> multis{num, num*2, num*3};
  return multis;
}

int main() {
  
  for (int element : first_three_multiples(8)) {
    std::cout << element << "\n";
  }
  
}
