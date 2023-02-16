# Chap 7 - Strings
# 11. Strings and Conditionals (Part Two)

# Ok this gets interesting. Getting introduced to boolean expressions letter in word. Gonna include this in my file as well.

print("blue" in "blueberry")
print("blb" in "blueberry") # this was just to check if it checked indiviual letters or a slice. it returns False, aka slice

# cool to see in can be used outside loops! thats one new thing today

# 1. Write a function called contains that takes two arguments, big_string and small_string and returns True if big_string
#    contains little_string
# 2. Write a function called common_letters that takes two arguments, string_one and string_two and returns a list with 
#    all of the letter they have in common

#def contains(big_string, small_string):
#	if small_string in big_string:
#		return True
#	return False
#	

def contains(big_string, small_string):
	return small_string in big_string

print(contains("strawberry", "berry"))


# Ok this second part was rougher indeed. Some of this might not have been described too much earlier. Had to look up the 
# forums, which did not write the code out, but gave a hint. First I ended with a lot of duplicate letters, so ended up adding
# another if statement, that said if i not allready in lst. Got it right, but this could probably been done way cleaner.

#def common_letters(string_one, string_two):
#	lst = []
#	for i in string_one:
#		if i in string_two:
#			if i not in lst:
#				lst.append(i)
#	return lst

# Gonna look up the solution actually. To see how the teacher would write it. 
# AND that was good. AND AND AND AND - can save a couple lines here. 
# Also, saw that i can write the first section cleaner. Scrolling up. 

def common_letters(string_one, string_two):
	lst = []
	for i in string_one:
		if (i in string_two) and not (i in lst):
			lst.append(i)
	return lst

print(common_letters("strawberry", "blueberry"))
