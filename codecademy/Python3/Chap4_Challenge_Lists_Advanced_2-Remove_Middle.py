# Lists Challenge (Advanced)
# Challenge 17
# Remove Middle

# Our next function will remove all elements from a list with an index within a certain range. The function will 
# accept a list, a starting index, and an ending index. All elements with an index between the starting and ending
# index should be removed from the list. Here are the steps:

# 1. Define the function to accept three parameters: the list, the starting index and the ending index
# 2. Get all elements before the starting index
# 3. Get all elements after the ending index
# 4. Combind the two partial lists into the result
# 5. Return the result

# Again, I have a hunch, but I don't see it clear as day. I'm thinking about slicing. 

def remove_middle(lst, start, end):
	new_lst = lst[:start] + lst[end+1:]	
	return new_lst
	
# HOLY MOLY it worked! I do have to admit, this was guesswork, and did not expect it to work out. I still a bit
# unsure where to place the : in the slicing. like [:start] and [end+1]
# But, hopefully it will get into my small nut somehow lol. At least it makes more sense when reading over it all
# a couple times. 

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))



# Note, this could be done even easier. Did not have to make a new variable inside the function!
# return lst[:start] + lst[end+1]
