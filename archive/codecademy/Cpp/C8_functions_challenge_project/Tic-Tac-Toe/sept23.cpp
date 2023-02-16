#include <iostream>
#include <vector>

std::vector<std::string> x_moves;
std::vector<std::string> y_moves;
//int total_moves = x_moves.size() + y_moves.size();

static std::vector<std::string> winning_1 = {"A1", "A2", "A3"};
static std::vector<std::string> winning_2 = {"B1", "B2", "B3"};
static std::vector<std::string> winning_3 = {"C1", "C2", "C3"};
static std::vector<std::string> winning_4 = {"A1", "B1", "C1"};
static std::vector<std::string> winning_5 = {"A2", "B2", "C2"};
static std::vector<std::string> winning_6 = {"A3", "B3", "C3"};
static std::vector<std::string> winning_7 = {"A1", "B2", "C3"};
static std::vector<std::string> winning_8 = {"A3", "B2", "C1"};

std::string move;

int main() {
    std::cout << "Tic Tac Toe\n\n";

//    while (total_moves < 9) {
//        std::cout << "testing";
//    }
}