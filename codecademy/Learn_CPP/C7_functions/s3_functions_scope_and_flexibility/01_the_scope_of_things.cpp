// Pretty much an introduction to scope. I got a pretty good understanding of
// global and local scope from Python and Rust, so not gonna write a whole 
// lot of comments on it for now.

#include <iostream>

void enter_code(int passcode) {
	std::string secret_knowledge = "https://content.codecademy.com/courses/regex/onyourexcitingjourneylearningtocodeyouwillfindthis.gif";

	if (passcode == 0310) {
		std::cout << secret_knowledge << "\n";
	} else {
		std::cout << "Sorry, incorrect!\n";
	}
}

int main() {
	enter_code(0310);
}

