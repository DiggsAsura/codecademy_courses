# Chapter 6 - Python Code Challenges
# Functions 5
# Remainder

# For the final challenge in this group, we are going to take the remainder of two numbers while performing
# other mathematichal operations on them. We are going to multiply the nuerator by 2 and divide the denominator
# by 2. After the two values have been modified, we will divide them and return the remainder. In order to do this
# we will need to:

# 1. Define the function to accept two parameters
# 2. Multiply the first input value by 2
# 3. Divide the second input value by 2
# 4. Calculate the remainder of the modified first input value divided by the modified second input value (modulus)
# 5. Return the answer

# Ok this looks like a lot of mumbo jumbo 

def remainder(num1, num2):
	#first = num1 * 2
	#second = num2 / 2
	#return first % second
	# above is correct, just want to do a single line version after seing the summary.
	return (num1 * 2) % (num2 / 2)
	
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0


