#include <iostream>
#include <vector>

std::vector<char> x;
std::vector<char> y;
std::vector<char> z;

char my_char;

int main() {
	std::cout << "Playing around with vectors a bit\n";

	std::cout << "x: ";
	std::cin >>  my_char;
	x.push_back(my_char);
	z.push_back(my_char);

	std::cout << "y: ";
	std::cin >>  my_char;
	y.push_back(my_char);
	z.push_back(my_char);

	for (char zzz : z) {
		std::cout << zzz;
		std::cout << "\n";
	}
}
