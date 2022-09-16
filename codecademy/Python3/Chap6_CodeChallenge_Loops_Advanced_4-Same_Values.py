# Chapter 6 - Python Code Challenges
# Loops (Advanced) 4
# Same Values

# In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be
# iterating through both of them at the same time and compare the values, if the numbers are equal, then we 
# record the index. These are the steps we need to accomplish this: 

# 1. Define our function to accept two lists of numbers
# 2. Create a new list to store our matching indicies
# 3. Loop through each index to the end of either of our lists
# 4. Within the loop, check if our first list at the current index is equal to the second list
#    at the current index. If so, append the index where they matched
# 5. Return our list of indices


#def same_values(lst1, lst2):
	# I guess we are talking a while loop here. 
	# Changed it to for
	# Really thouch below would do it, but apparently not 
	#for i1 in lst1:
	#	for i2 in lst2:
	#		if i1 == i2:
	#			new_list = []
	#			new_list.append[i]
	#return new_list

# It was not too far, but not too close either. I'm giving up searching for the correct way a bit fast now, 
# need to change that? Hopefully something stick. I will go through another course after, and redo alot of it tho!
# Also, after a few more chapters, I'm gonna write alot more code on my own!

def same_values(lst1, lst2):
	new_lst = [] # I had this one, not same spot but dont think that matter. 
	for i in range(len(lst1)): # Did not use range(len()), don't really understand why
		if lst1[i] == lst2[i]: # This one is not too far off I guess, at least i understand it when reading
			new_lst.append(i) # I thought it would be .append[], but I guess that would give syntax error. 
	return new_lst
	
	
# Ok these does not go so smooth as I hoped. Hope it's not all lost!!! xD
# The more I learn, the less i know principle??? Just have to keep at it! :D	
	
	#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
