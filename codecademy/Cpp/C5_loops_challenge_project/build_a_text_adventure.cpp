// Slightly different project ( more real world project?! ) 
//
// Instead of clear pointers what to do, the project has a couple
// requirements. In this case, it's a text based adventure. 
//
// 
// 1. Need to be familiar with C++ conditionals and control flow,
//    loops and setting variables using user input.
//
// 2. Requirements:
//     - Story (make up one)
//     - a beginning
//     - at least three possible endings
//
// 3. You story should contain at least three branch points,
//    where the user must make a choice about what to do next. 
//    At each branch point, the program should:
//      - give the user at least two choices
//      - accept user input
//
//    Note that not every story branch needs its own ending: it can
//    also add something and then reconnect with another storyline. 
//
// 4. You program should incorporate a least one kind of loop. 
//
//    Loops come in handy in a couple scenarios: 
//      - to validate user input (e.g check if the user entered something other than your listed choices and then list the choices again)
//      - to give the user multiple chances to choose a specific outcome (e.g, give a user three chances to pick an option that wont't get them killed)
//      - to continue the adventure until the user makes a particular choice
//
//    Note: On Codecademy's platform, if you plan to obtain user input within
//    a loop, we recomment sticking with a for loop. Due to the way our platform is set up,
//    a while loop that includes user input will trigger an infinite loop. 
//
// 5. Your program should handle user choices using conditional logic. 
//    We encourage you to use if/else if statements and switch statemetns 
//    where you see fit. 
//
//    Note: If your user has reached an ending, you can use return 0; to 
//    exit the main() function and end the program. 
//
// 6. Project Extensions & Solution
//
//    Great work! Visit our forums to compare your project to our 
//    sample solution code. You can also learn how to host your own 
//    solution on GitHub so you can share it with other learners!
//    Your text adventure will probably be coded a lot different from ours - 
//    and that's totally fine! The important thing is you built something
//    that works as expected and that you are proud of. There are multiple 
//    ways to solve these projects, and you'll learn more by seeing others' 
//    code. 
//
//    If you want to extend this project further, try adding more 
//    complexity by increasing the number of possible branches. Also,
//    if you already know C++ functions, you can refactor your program so
//    so that your code is cleaner and more modular. 
//
//    Optional: You can include ASCII art to add an extra illustrative 
//    flourish to the storyline. 
//

/////////////////
//
//  Project: Getting Home from Bar in one Piece
//
////////////////
//

#include <iostream>

int a, b;

int a_1() {
  std::cout << "Part II (A): Just one more... is fine right?\n";
  std::cout << "You choose (1/2/3): ";
  std::cin >> b;

  switch(b) {
    case 1:
      std::cout << "Good ending\n\n";
      break;
    case 2:
      std::cout << "Ok ending\n\n";
      break;
    case 3:
      std::cout << "Bad ending\n\n";
      break;
    default:
      std::cout << "Failed\n\n";
      break;
  }
}

int a_2() {
  std::cout << "Part II (B): Went home\n";
  std::cout << "You choose (1/2/3): ";
  std::cin >> b;

  switch(b) {
    case 1:
      std::cout << "Good ending\n\n";
      break;
    case 2:
      std::cout << "Ok ending\n\n";
      break;
    case 3:
      std::cout << "Bad ending\n\n";
      break;
    default:
      std::cout << "Failed\n\n";
      break;
  }
}

int beginning() {
  std::cout << "Welcome to\n";
  std::cout << "GET HOME FROM THE BAR!\n\n";

  // Intro - THE BAR
  std::cout << "You are sitting at the bar. It's getting late, and you are getting somewhat drunk.\n";
  std::cout << "Your buddies are as well, but everyone in good mood.\n";
  std::cout << "You see the time, its getting late, really late. You should go home.\n";
  std::cout << "When you are about to call it, Frank tries to stop you. 'Wait, one more round on me!'\n\n";

  // Intro --options
  std::cout << "1) Stay for one more round.. You get in trouble back home anyways.\n";
  std::cout << "2) Be persistent, call it a night, even though Frank will not let you go easily.\n";
  std::cout << "You choose: ";
  std::cin >> a;

  switch (a) {
    case 1:
      a_1();
      break;
    case 2:
      a_2();
      break;
    default:
      std::cout << "Try again\n\n";
  }

}


int main() {
  beginning();

}



