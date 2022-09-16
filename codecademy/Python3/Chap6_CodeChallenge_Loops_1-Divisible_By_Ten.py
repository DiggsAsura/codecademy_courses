# Chapter 6 - Python Code Challenges
# Loops 1
# Divisible By Ten

# Let's start our code challenges with a function that counts how many numbers are divisible by ten from 
# a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check
# each of the numbers in the list. Every time a number is divislbe by 10, a counter will be incremented and the 
# final count will b returned. These are the steps we need to complete this: 

# 1. Define the function to accept one input parameter called nums
# 2. Initialize a counter to 0
# 3. Loop through every number in nums
# 4. Within the loop, if any of the numbers are divisible by 10, increment our counter
# 5. Return the final counter value

# Ok a bit afraid, not gonna lie!!! For, while and list comprehensions.. Can I remember the differences and 
# how to do them? Let's go see..

def divisible_by_ten(nums):
	count = 0
	for i in nums:
		if i % 10 == 0:
			count += 1
	return count

# ok looked at hint, hope above is correct. Might not be enough, but it should be close.
# HOLY moly, it is 99% correct, forgot to return count...

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
