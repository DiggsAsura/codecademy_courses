/* Review
 *
 * Congratulations! You have learned about how to store groups of data into
 * vectors in C++. 
 *
 * Here are some of the things that we learned:
 *
 * - Vectors are a sequence of elements that you can access by an index.
 *
 *   std::vector<int> even = {2, 4, 6, 8, 10};
 *
 * - The first index in a vector is 0.
 *
 * - Some of the functions that come with vectors:
 *    - .push_back()
 *    - .pop_back()
 *    - .size()
 *
 * - We can use a for loop to iterate through a vector
 */

#include <iostream>
#include <vector>

int main() {
  int even = 0;
  int odd  = 1;

  std::vector<int> nums = {2, 4, 3, 6, 1, 9, 11, 231, 432};

  for (int i=0; i < nums.size(); i++) {
    if (nums[i] % 2 == 0) {
      even = even + nums[i];
    }
    else {
      odd = odd + nums[i];
    }
  }

  std::cout << "Sum of even numbers is " << even << "\n";
  std::cout << "Product of odd numbers is " << odd << "\n\n";
}
