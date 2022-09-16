# Chap 7 - Strings
# 9. Iterating through Strings

# Refresher on for and while loops! 
# Reminder: Because STRINGS ARE LISTS, that means we can iterate through a string using for and while loops. 
# This opens up a whole range of possibilities of ways we can manipulate and analyze strings. 

# 1. Let's replicate a function you are already familiar with, len()
#    Write a new function called get_length() that takes a string as an input and returns the number of 
#    characters in that string. Do this by iterating through the string, dont cheat and use len()!

# Ok imo this was a quite horrible task. I had to make this def take a parameter which does not exist. Easy
# enough when I look it back, but it kinda screwed a bit with my covid head. 

def get_length(word):
	counter = 0
	for i in word: 
		counter += 1
	return counter

word = "This one tricked me a bit"
	
print(get_length(word))
