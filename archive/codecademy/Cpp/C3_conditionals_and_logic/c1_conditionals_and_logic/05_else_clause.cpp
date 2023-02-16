// If condition is true, statement1 is executed. Then the program skips statement2 and executes any code statements following the if/else clause
//
// If contidion is false, statement1 is skipped and statement2 is executed. After statement2 completes, the program executes any code statements following the if/else clause.

#include <iostream>
int main() {
  int grade = 59;
  if (grade > 60) {
    std::cout << "Pass\n";
  }
  else {
    std::cout << "Fail\n";
  }
}
