# Lists Challenge (Advanced)
# Challenge 16
# Every Three Numbers

# Let's start our challenging problems with a function that creates a list of numbers up to 100 in increments
# of 3 starting from a number that is passed to the cuntion as an input parameter.
# Here is what we need to do:

# 1. Define the function to accept one parameter for our starting number
# 2. Calculate the number between the starting number and 100 while incrementing by 3
# 3. Store the number in a list
# 4. Return the list


# This one should be quite easy, however, not entirely sure.. i do remember how to do the numbers (10, 10, 3). 
# Let's try take it from there

#def every_three_nums(start):
#	 if start < 100:
#	 	return (start, 100, 3)
#	 else:
#	 	return []

# Ok above was not correct. It was somewhat close, but it didn't print every 3rd in a list. it literally just
# printed start number and the two other integers.

def every_three_nums(start):
	return list(range(start, 101, 3))
	
#Uncomment the line below when your function is done
print(every_three_nums(91))
