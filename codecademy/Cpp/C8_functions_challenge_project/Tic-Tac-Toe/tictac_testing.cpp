#include <iostream>
#include <vector>

std::vector<std::string> moves = {};

std::string x;
std::string y;

int main() {
	std::cout << "Welcome to Tic Tac Toe! \n\n";

	while (moves.size() < 9) {
		if (moves.size() % 2 == 0) {
			std::cout << "X: ";
			std::cin >>  x;
			moves.push_back(x);
		}
		else {
			std::cout << "Y: ";
			std::cin >> y;
			moves.push_back(y);
		}
	}

	for (std::string move : moves) {
		std::cout << move << "\n";
	}
}
