# Chapter 6 - Python Code Challenges
# Functions (Advanced) - 2
# Tip

# Let's say we are going to a resturant and we decide to leave a tip. We can create a function to easily
# calculate the amount to tip based on the total cost of the food and a percentage.
# This function will accept both of those values as inputs and return the amount of monty to tip. In order
# to do this, we will need a few steps:

# 1. Define the function to accept the total cost of the food called total and the percentage to tip as percentage
# 2. Calculate the tip amount by multiplying the total and percentage and dividing by 100
# 3. Return the tip amount

# Advanced? I had way worse (knock on woods again)

def tip(total, percentage):
	#return = (total * percentage) / 100 # Dont's know if i understand why, but in () it fails. Syntax error on /
	return total * percentage / 100 # works however. 
	
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
