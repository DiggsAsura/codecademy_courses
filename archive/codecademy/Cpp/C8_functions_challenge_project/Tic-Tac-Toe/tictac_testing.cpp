#include <iostream>
#include <vector>

static std::vector<std::string> moves;
static std::vector<std::string> x_moves;
static std::vector<std::string> y_moves;

std::string x;
std::string y;

int main() {
	std::cout << "Welcome to Tic Tac Toe! \n\n";

	while (moves.size() < 9) {
		if (moves.size() % 2 == 0) {
			std::cout << "X: ";
			std::cin >>  x;
			moves.push_back(x);
			x_moves.push_back(x);
		}
		else {
			std::cout << "Y: ";
			std::cin >> y;
			moves.push_back(y);
			y_moves.push_back(y);
		}
	}

	for (std::string move : moves) {
		std::cout << move << "\n";
	}

	std::cout << "\n\nX moves: \n";
	for (std::string xm : x_moves) {
		std::cout << xm << "\n";
	}

	std::cout << "\n\nY moves: \n";
	for (std::string ym : y_moves) {
		std::cout << ym << "\n";
	}
}
