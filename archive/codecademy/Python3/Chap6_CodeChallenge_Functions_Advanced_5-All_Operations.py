# Chapter 6 - Python Code Challenges
# Functions (Advanced) - 5
# All Operations

# For the final code challenge, we are going to perform multiple mathematichal operations on multiple inputs
# to the function. We will begin with adding the first two inputs, then we will subtract the third and fourth 
# inputs. After that, we will multiply the first result and the second result. In the end, we will return the 
# remainder of the previous result divided by the first input. We will also print each of the 
# steps. The steps needed to complete this are:

# 1. Define the function to accept four inputs, a, b, c and d
# 2. Print and store the result of a + b
# 3. Print and store the result of c - b
# 4. Print and store the first result times the second result
# 5. Return the previous result modulo a

# Hahahahaha. Ok lets go.

def lots_of_math(a, b, c, d):
	first = a + b
	second = c - d
	third = first * second
	print(first)
	print(second)
	print(third)
	return third % first
	
# Got it first try. Ok idk why some things just easy and other things is a major pain in the norwegian famous 
# rattatta. 

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
