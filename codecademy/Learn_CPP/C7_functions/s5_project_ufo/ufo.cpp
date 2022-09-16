/* Learn C++
 * Project: UFO
 *
 * It's game time! And by that we mean, it's time for you to roll up your
 * sleeves and build r game: UFO.
 *
 * The premise:
 * Invaders from outer space have arrived and are abducting humans using
 * tractor beams. Players must crack the codeword to stop the abduction!
 *
 * Ok, we'll admit it's quite a bit like that class game, "Hangman", but
 * with better premise. Plus, building this command-line game was the 
 * Codecademy 2019 Software Engineer Internship Backend Programming Challenge!
 *
 * Note: This is a more involved project, so please feel free to take breaks 
 * as needed.
 *
 */

// Section 1: Probing the enviroment

#include <iostream>
#include "ufo_functions.hpp"

int main() {
	greet();
	
	std::string codeword = "codecademy";
	std::string answer = "__________";
	int misses = 0;
	std::vector<char> incorrect;
	bool guess = false;
	char letter;
	
	while (answer != codeword && misses < 7) {
		display_misses(misses);
		display_status(incorrect, answer);

		std::cout << "\nPlease enter your guess: ";
		std::cin >> letter;

		for (int i = 0; i < codeword.length(); i++) {
			if (letter == codeword[i]) {
				answer[i] = letter;
				guess = true;
			}
		}

		if (guess == true) {
			std::cout << "\nCorrect!\n";
		}
		else {
			std::cout << "\nIncorrect! The tractor beam pulls the person in furter...\n";
			misses++;
		}
	}
	guess = false;

	end_game(answer, codeword);
}
	

