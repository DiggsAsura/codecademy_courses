/* Operations
 *
 * So what happens when you want to change each of the values within a 
 * vector?
 *
 * You can use a for loop!
 *
 * For example, suppose we have an int vector that looks like this:
 *
 * | 10 | 20 | 30 |
 * 
 * You can write a for loop that iterates from 0 to vector.size(). And
 * here's the cool part: you can use the counter of the for loopas the
 * index! Woah.
 *
 * for (int i = 0; i < vector.size(); i++) {
 *  vector[i] = vector[i] + 10;
 * }
 *
 * This will change the vector to:
 *
 * | 20 | 30 | 40 |
 *
 * Here, we incremented i from 0 to vector.size(), which is 3. During
 * each iteration, we are adding 10 to the element at position i:
 *
 * When i = 0, we added 10 to the vector[0]
 *
 * When i = 1, we added 10 to vector[1]
 * 
 * When i = 2, we added 10 to vector[2]
 *
 */

#include <iostream>
#include <vector>

int main() {
  std::vector<double> delivery_order;

  delivery_order.push_back(8.99);
  delivery_order.push_back(3.75);
  delivery_order.push_back(0.99);
  delivery_order.push_back(5.99);

  double total = 0.0;

  for (int i = 0; i < delivery_order.size(); i++) {
    total = total + delivery_order[i];
  }

  std::cout << "Total: $" << total << "\n";
}
