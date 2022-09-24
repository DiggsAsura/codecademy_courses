#include <iostream>
#include <vector>

int main() {
	std::vector<std::string> a;
	a.push_back("Hello");
	a.push_back("World");

	int i = 1;

	while (i <= 3) {
		std::cout << a[0] << " " << a[1] << "\n";
		i++;
	}
}
