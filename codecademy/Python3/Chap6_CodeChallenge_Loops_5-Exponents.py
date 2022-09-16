# Chapter 6 - Python Code Challenges
# Loops 5
# Exponents

# In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a
# list of other numbers. What this means is that for every number in the first list, we will raise that number to
# the power of every number in the second list. If you provide the first list with 2 elements and the second list
# with 3 numbers, then there will be 6 final answers. Let's look at the steps we need:

# 1. Define the function to accept two lists of numbers, bases and powers
# 2. Create a new list that will contain our answers
# 3. Create a loop that iterates through every base in bases
# 4. Within that loop, create another loop that iterates through every power in power
# 5. Within that nested loop, append the result of the current base raise to the power of the
#    current power.
# 6. After all iterations of both loops are complete, return the list of answer

# OK! Even with my slow head today, this one sounds like a fun challenge! Idk why I like nested loops. Let's go!

def exponents(bases, powers):
	lst = []
	for base in bases:
		for power in powers:
			#lst.append([base ** power])
			lst.append(base ** power)
	return lst
			
# Holy moly! This was extremly close! I got all the right numbers output, but it was listed as two dimensional list. 
# OK so just easy change from ([base ** power]) to (base ** power) boomtown!

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
