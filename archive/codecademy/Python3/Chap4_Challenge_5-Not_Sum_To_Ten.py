# Challenge 5 - Not Sum To Ten

# Finally, we are going to check if the summation of two inputs does not equal ten. 
# Our function will accept two inputs and add them together. If the two numbers added together are not
# equal to ten, then we will return True, otherwise, we will return False. Here is what we need to do:

# 1. Define the function to accept two parameters, num1 and num2
# 2. Add the two parameters together
# 3. Test if the result is not equal to 10
# 4. If the sum is not equal, return True, otherwise, return False

def not_sum_to_ten(num1, num2):
	if num1 + num2 != 10:
		return True
	else:
		return False

		
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
#print(not_sum_to_ten(5,5))
# should print False		
		
# This was super easy! I really like these small challenges, rather than BigProject... At least at this
# point! Great!
