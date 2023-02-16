# List Challenge
# Challenge 12
# Append Sum

# Let's create a function that calculates the sum of the last two elements of a list and append it to the end.
# After doing so, it will repeat this process two more times and return the result list. You can choose to use
# a loop or manually use three lines. Here are the steps we need:

# 1. Define the function to accept one parameter for our list of numbers
# 2. Add the last and second to last elements from our list together
# 3. Append the calculated value to the end of our list.
# 4. Repeat steps 2 and 3 two more times
# 5. Return the modified list


# Ok this one seems a bit distant. Probably have to look up hint. I mean, for the loop at least. Ofc
# thats what I want, sounds way more effective even for such small function. I'll try the manual first though

#def append_sum(lst):
#	lst.append(lst[-1] + lst[-2])
#	lst.append(lst[-1] + lst[-2])
#	lst.append(lst[-1] + lst[-2])
#	return lst

# The good part, I got the manual one easy peasy, first try. 
# The sad pard, I'm not sure how to do this with a loop and make it stop at 3 times! 

def append_sum(lst):
	for i in range(3):
		lst.append(lst[-1] + lst[-2])
	return lst

# GOT IT! Did not watch hint but like a PRO programmer i used google to find out how to use the for loop only X 
# amount of times. I do remember += 1, but that would made it endless... so yea. for i in range(3)! Gdi so easy! 

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
