// Harry Potter Sorting Hat Quiz
//
// Write a sortinghat.cpp program that asks the user some
// questions and places them into one of the four Houses based on 
// their answers!

#include <iostream>
using namespace std;

int main() {
  int gryffindor = 0, hufflepuff = 0, ravenclaw = 0, slytherin = 0;
  int answer1, answer2, answer3, answer4;

  cout << "The Sorting Hat Quiz! \n\n";

  // QUESTION 1
  cout << "Q1) When I'm dead, I want people to remember me as: \n\n";
  cout << "1) The Good\n";
  cout << "2) The Great\n";
  cout << "3) The Wise\n";
  cout << "4) The Bold\n\n";

  cout << "You choose: ";
  cin >> answer1;
  switch (answer1) {
    case 1:
      hufflepuff++;
      break;
    case 2:
      slytherin++;
      break;
    case 3:
      ravenclaw++;
      break;
    case 4:
      gryffindor++;
      break;
    default:
      cout << "Invalid input.\n";
  }

  // QUESTION 2
  cout << "\n\n";
  cout << "Q2) Dawn or Dusk? \n\n";
  cout << "1) Dawn\n";
  cout << "2) Dusk\n\n";

  cout << "You choose: ";
  cin >> answer2;
  switch (answer2) {
    case 1:
      gryffindor++;
      ravenclaw++;
      break;
    case 2:
      hufflepuff++;
      slytherin++;
      break;
    default:
      cout << "Invalid input.\n";
  }

  // QUESTION 3
  cout << "\n\n";
  cout << "Q3) Which kind of instrument most pleases your ear?\n\n";
  cout << "1) The violin\n";
  cout << "2) The trumpet\n";
  cout << "3) The piano\n";
  cout << "4) The drum\n\n";

  cout << "You choose: ";
  cin >> answer3;
  switch (answer3) {
    case 1:
      slytherin++;
      break;
    case 2:
      hufflepuff++;
      break;
    case 3:
      ravenclaw++;
      break;
    case 4:
      gryffindor++;
      break;
    default:
      cout << "Invalid input.\n";
  }

  // QUESTION 4
  cout << "\n\n";
  cout << "Q4) Which road tempts you most? \n\n";
  cout << "1) The wide, sunny grassy lane\n";
  cout << "2) The narrow, dark, lantern-lit alley\n";
  cout << "3) The twisting, leaf-strewn path through woods\n";
  cout << "4) The cobbled street lined (ancient buildings)\n\n";

  cout << "You choose: ";
  cin >> answer4;
  switch (answer4) {
    case 1:
      hufflepuff++;
      break;
    case 2:
      slytherin++;
      break;
    case 3:
      gryffindor++;
      break;
    case 4:
      ravenclaw++;
      break;
    default:
      cout << "Invalid output.\n";
  }

  cout << "\n\n";

  // The answer
  int max = 0;
  string house;

  if (gryffindor > max) {
    max = gryffindor;
    house = "Gryffindor";
  }
  
  if (hufflepuff > max) {
    max = hufflepuff;
    house = "Hufflepuff";
  }

  if (ravenclaw > max) {
    max = ravenclaw;
    house = "Ravenclaw";
  }

  if (slytherin > max) {
    max = slytherin;
    house = "Slytherin";
  }

  cout << house << "!\n\n";
}
