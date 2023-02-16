# Lists Challenge (Advanced)
# Challenge 19
# Double Index

# Our next function will double a value at a given position. We will provide a list and an index to double.
# This will create a new list by replacing the value at the index provided with double the original value. If the
# index is invalid then we should return the original list. Here is what we need to do:

# 1. Define the function to accept two parameters, one for the list and another for the index of the value we 
#    are going to double
# 2. Test if the index is invalid. If its invalid then return the original list
# 3. If the list is valid then get all values up to the index and store it as a new list
# 4. Append the value at the index times 2 to the new list
# 5. Add the rest of the list from the index onto the new list
# 6. Return the new list

def double_index(lst, index):
	#return lst.count(index[:index]) + (index * 2) + lst.count(index[index:])
	# Wanted to see if I could do it in just line, but nope. 
	# TypeError: 'int' object is not subscriptable
	
	#double = index * 2
	#first = lst[:index]
	#last = lst[index:]
	#new_lst = lst.append(first, double, last)
	# TypeError: append() takes exactly one argument (3 given)
	# Hmm hmm
	# Checked hint again... Not sure if the task really explain WHAT makes the list valid or not. Don't really
	# understand why its checking up against lenght. 
	
	if  index >= len(lst):
		return lst
	else:
		# Gets the original list up to index. Does it really have to include 0:? Tested, do not need the 0. :index will
		# default to 0. 
		new_lst = lst[:index]
	new_lst.append(lst[index]*2)
	new_lst = new_lst + lst[index+1:]
	return new_lst
	
# Ok this one was a bit messy imo. Don't think the if statement was really defined in the task. Also how else
# will only return half the new lst, then the two next had to be unindented. To me this looks messy..


#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
	

