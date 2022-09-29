#include <iostream>

const std::string yea = "not today";
const std::string off = "out of office";
const std::string bah = "school all day!";
const std::string grr = "valid excuse";

void str_one() {
	std::cout << yea << "\n";
}

void str_two() {
	std::cout << off << "\n";
}

void str_three() {
	std::cout << bah << "\n";
}

void str_four() {
	std::cout << grr << "\n";
}

int main() {
	str_one();
	str_two();
	str_three();
	str_four();
}
