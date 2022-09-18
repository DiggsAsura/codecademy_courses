/* Sept 16 2022
 * Tic-Tac-Toe
 *
 * Project C++
 * Codecademy
 *
 * ************
 *
 * So this is very much an open ended project. I feel it's quite early in the
 * learning phase of C++, but it's also cool to try this out. I guess I should
 * have enough knowledge to put it together. I'll give it a fair shot!
 *
 * Br Kenneth / DiggsAsura
 */


/* So need to find out quite a bit to get this done. 
 * It's not possible, well at least if i want to keep my sanity, to check every possible ways to fill the board,
 * which woudl be something like 9^9 
 *
 * Possible winning setups is probably the way to go
 *
 * if ("winning combination") {
 * 	grats
 * else {
 * 	nope
 * }
 *
 * Then it has to be two players X and O
 *
 *
 * And there need to be a while loop which keeps the game going until the board is filled. Alternating P1 and P2

#include <iostream>
#include "headers.hpp"


int main() {
	
	std::string player1 = "diggs";
	std::string player2 = "asura";

	grid();


}

