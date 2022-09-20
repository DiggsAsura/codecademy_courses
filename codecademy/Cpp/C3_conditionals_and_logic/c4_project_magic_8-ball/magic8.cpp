#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
  cout << "Welcome to MAGIC 8-BALL!\n\n";

  string question;
  cout << "What is your question: ";
  cin >> question;

  // apparently this variable wont save the whole string..? 
  cout << "The answer to your question (" << question << "):\n";

  srand(time(NULL));
  int answer = rand() % 20;
  cout << answer << ": ";

  switch (answer) {
    case 0:
      cout << "It is certain.\n";
      break;
    case 1:
      cout << "It is decidedly so.\n";
      break;
    case 2:
      cout << "Without a doubt.\n";
      break;
    case 3:
      cout << "Yes - definetly.\n";
      break;
    case 4:
      cout << "You may rely on it.\n";
      break;
    case 5:
      cout << "As I see it, yes.\n";
      break;
    case 6:
      cout << "Most likely.\n";
      break;
    case 7:
      cout << "Outlook good.\n";
      break;
    case 8:
      cout << "Yes.\n";
      break;
    case 9:
      cout << "Signs point to yes.\n";
      break;
    case 10:
      cout << "Reply hazy, try again.\n";
      break;
    case 11:
      cout << "Ask again later.\n";
      break;
    case 12:
      cout << "Better not tell you now.\n";
      break;
    case 13:
      cout << "Cannot predict now.\n";
      break;
    case 14:
      cout << "Concentrate and ask again.\n";
      break;
    case 15:
      cout << "Don't count on it.\n";
      break;
    case 16:
      cout << "My reply is no.\n";
      break;
    case 17:
      cout << "My sources say no.\n";
      break;
    case 18:
      cout << "Outlook not so good.\n";
      break;
    case 19:
      cout << "Very doubtful.\n";
      break;
    case 20:
      cout << "No.\n";
      break;
    default:
      cout << "Value out of bounds";
      break;
  }
  cout << "\n";
}


