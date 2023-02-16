# Chapter 6 - Python Code Challenges
# Functions 4
# Average

# Let's create a function which takes the average of two numbers. These two numbers will be the input of the 
# function and the output will be the average of the two. In order to do this, we need do to a few steps:

# 1. Define the function with two input parameters, num1 and num2
# 2. Calculate the sum of the two numbers
# 3. Divide the sum by the number of inputs to the function
# 4. Return the answer

# Ok add together then divide by 2. But should I divide by two with len? Is that possible? 

def average(num1, num2):
	#return (num1 + num2) / len(average) # functions has no len() - ok try something else
	#total = [num1 + num2]
	#length = len(total)
	#return total / length # TypeError: unsupported operand type(s) for /: 'list' and 'int'
	# Ok giving up len(), might not be correct, was just curious. Just do it the easy way
	return (num1 + num2) / 2  # yea spot on. 
	
	
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
	
	
