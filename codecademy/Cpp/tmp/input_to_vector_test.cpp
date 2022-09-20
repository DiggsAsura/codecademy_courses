#include <iostream>
#include <vector>

std::vector<std::string> words = {"SARAH", "KENNETH", "KAYI"};
std::string word;

int main() {
//	std::cin >> word;
//	words.push_back(word);
//	std::cout << words << "\n";
	for (auto name: words) {
		std::cout << name << "\n";
	}
}

