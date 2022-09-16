# Challenge 3 - Twice As Large

# Make a def that will check if one number is twice as large as the second number
# I really don't get why Codecademy announce that these challenges might be hard, after
# that offplatform "BigProject". The BigProject was a royal pain in the butt while these are 
# a breeze. 

# 1. Define our function with two inputs num1 and num2
# 2. Multiply the second input by 2
# 3. Use an if statement to compare the result of the last calculation with the first input
# 4. If num1 is greater then return True otherwise return False

def twice_as_large(num1, num2):
	if num1 > 2 * num2:
		return True
	else:
		return False

# Write your twice_as_large function here:

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(2, 5))
# should print False
print(twice_as_large(11, 5))
# should print True
