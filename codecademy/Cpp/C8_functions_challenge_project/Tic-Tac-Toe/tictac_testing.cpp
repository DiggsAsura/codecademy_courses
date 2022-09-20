#include <iostream>
#include <vector>

std::vector<std::string> moves = {""};

std::string x = "";
std::string y = "";

int main() {
	while (moves_total.size() < 9) {
		if (moves_total() % 2 == 0) {
			std::cout << "X: ";
			std::cin >>  x;
			moves_total.push_back(x);
		}
		else {
			std::cout << "Y: ";
			std::cin >> y;
			moves_total.push_back(y);
		}
	}

	for (auto move : moves_total) {
		std::cout << move << "\n";
	}
}
