/* Vector
 * The std::vector lives in the <vector> header. 
 *    Like what the actual fuck is this a introduction? lol 
 *    Clera as mud. 
 *  
 *  So first, we need to add this line of code to the top of the
 *  program:
 * 
 * #include <vector>
 *
 * For review, #include is a preprocessor directive that tells the
 * compiler to include whatever library that follows. In our case that
 * is the standard vector library. 
 *
 * And the syntax to create a vector looks like:
 *
 * std::vector<type> name;
 *
 * So to define a vector of ints called calories_today:
 *
 * std::vector<int> calories_today;
 *
 * Inside the angle brackets is the data type of the vector. After
 * the angle brackets is the name of the vector.
 *
 * Note: The type of the vector (i.e., what data type is stored
 * inside) cannot be changed after the declaration.
 */

#include <iostream>
#include <vector>

int main() {
  std::vector<double> subway_adult;
  std::vector<double> subway_child;
}
