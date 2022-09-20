#include <iostream>

int main() {
	srand(time(NULL));

	int the_amazing_rng = rand() % 38;
	std::cout << the_amazing_rng << "\n";
}
