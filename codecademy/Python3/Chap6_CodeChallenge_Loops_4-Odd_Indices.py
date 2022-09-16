# Chapter 6 - Python Code Challenges
# Loops 4
# Odd Indices

# This next function will give us the values from a list at every odd index. We will need to accept
# a list of numbers as an input paramter and loop through the odd indices instead of the elements. 
# Here are the steps needed.

# 1. Define the function header to accept one input which will be our list of numbers
# 2. Create a new list which will hold our values to return
# 3. Iterate through every odd index until the end of the list
# 4. Within the loop, get the element at the current odd index and append it to our new list
# 5. Return the list of elements which we got from the odd indices

# Not sure if this is just a bad day (it very much seems so tbh, lol, nothing gone the right way!), or if I'm 
# just super tired and slow. These loop challenges been hard!

# Just realise they ask for every other number in the list, not the odd numbers. I can't rembmer we touched on this
# earlier, but Chap 3 is a while ago. 

# Reading the Hint, and we have rouched upon something similar actually. The intervalls! range(x, x, interval)

def odd_indices(lst):
	odd = []
	for i in range(1, len(lst), 2):
		#odd.append(lst(i))
		odd.append(lst[i])
	return odd
	
# TypeError: 'list' object is not callable
# OH OHOH i actually got it, but [i] needs to be inside [] ofc!! gdi! so close..

	
	#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
