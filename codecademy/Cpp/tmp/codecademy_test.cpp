#include <iostream>

int age = 57;

int change_age() {
	int age = 25;
}

int main() {
	int age = 75;
	// ok so change_age() was the test. it wont overwrite age. 
	change_age();
	std::cout << "Value of age: " << age << "\n";
}
