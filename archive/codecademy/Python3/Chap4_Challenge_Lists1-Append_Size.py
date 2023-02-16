# Code Challenges: Lists
# Challenge 11
# Append Size

# For the first code challenge, we are going to calculate the length of a list and then append the value
# to the end of the list. Here is what we need to do: 

# 1. Define the function to accept one parameter for our list
# 2. Get the length of the list
# 3. Append the length of the list to the end of the list
# 4. Return the modified list


# Ok good to have a rerun on Lists. I think some of it is super easy, while other is still a bit alien. 
# This will combine lists and functions, which I want to get deeper into. Good!

# Lets go:

# Can it be this easy? I'm not entirely sure if the syntax and buildup here will be right. 

#def append_size(lst):
#	return lst + lst.append([len(lst)])
	
# ok, didn't work. TypeError: 
# TypeError: can only concatenate list (not "NoneType") to list

# Checked the hint, and i feel it's unfair, so close!! No??

def append_size(lst):
	lst.append(len(lst))
	return lst
	
# However, looking at it - I'm not sure why it's getting concatinated! I append to lst.. hmm I guess it understand
# append to type (list) or something..


#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))
