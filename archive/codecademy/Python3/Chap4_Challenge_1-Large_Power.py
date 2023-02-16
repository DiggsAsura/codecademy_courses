# Challenge 1
# The task is to make a method that tests if the result of taking the power of one number
# provides an answer greater than 5000. We gonna use a conditional statement to return True if
# the result is greater than 5000, or False if it's not. 

# To do so, we need to
# 1. Define the function to accept two input parameters called base and exponent
# 2. Calculate the result of base to the power of exponent
# 3. Use an if statement to test if the result is greater than 5000, If it is then return True, otherwise False


def large_power(base, exponent):
	if base ** exponent > 5000:
		return True
	else:
		return False
		
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False


# OK, got it right. This challenges is listed as potential challanging, while the BigProject prior to this
# was not. Weeeelll, this is cakewalk compared to the "easy" BigProject lol



