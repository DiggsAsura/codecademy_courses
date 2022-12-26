#include <iostream>
#include <chrono>

using namespace std::chrono;

int main() {
    auto start = high_resolution_clock::now();

    for (unsigned long long i = 0, j = 5; i < 5000000; i++, j++) {
        std::cout << "c++: " << j*i << std::endl;
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);

    std::cout << duration.count() << std::endl;
}
