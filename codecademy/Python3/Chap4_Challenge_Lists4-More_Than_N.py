# Lists challenge
# Challenge 14
# More Than N

# Our factory produces a variety of different flavored snacks and we want to check the number of instances
# of a certain type. We have a conveyor belt full of different types of snacks represented by different numbers.
# Our function will accept a list of numbers (representing the type of snack), a number for the second parameter
# (the type of snack we are looking for), and another number as the third parameter (the maximum number
# of that type of snack on the conveyor belt). The function will return True if the snak we are searching for 
# appears more times than we provided as our third parameter. These are the steps we need:

# 1. Define the function to accept three parameters, a list of numbers, a number to look for, and a number
# for the numbers of intances
# 2. Count the number of occurances of item (the second parameter) in lst (the first parameter)
# 3. If the number of occurences is greater than n (the third parameter), return True, otherwise False

# Oookay. First impression is this seems alot, but it's probably not really. I'm still too fresh to this, so it
# isnt much that is needed for me to feel overwhelmed haha. 

# So.. How to count one particular item in the list with the second parameter

#def more_than_n(lst, item, n):
#	i = len(lst[item])
#	if i > n:
#		return True
#	else:
#		return False

# I feeeeeel kinda close, but it's probably not len! 
# TypeError: object of type 'int' has no len()

# checked the hint. i forgot the method(or built-in function??) count! 

def more_than_n(lst, item, n):
	if lst.count(item) > n:
		return True
	else:
		return False
		
# Close but no cigar this time then!


#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
