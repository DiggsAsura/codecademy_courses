# Lists Challenges
# Challenge 15
# Combine Sort

# Finally, let's create a function that combines two different lists together and then
# sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here
# is what we need to do:

# 1. Define the function to accept two parameters, one for each list
# 2. Combine the two lists together
# 3. Sort the result
# 4. Return the sorted and combined list

# Okies. Hunch is i create a new list with .append or .insert, then use sort() or sorted()

def combine_sort(lst1, lst2):
	lst_combined = lst1 + lst2
	lst_combined.sort()
	return lst_combined
	
	
# BOOOOM! Got it first try!

# The lesson suggest using sorted though, to generate another new list. But it's not needed so got it this way too!

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
