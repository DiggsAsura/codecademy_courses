python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# Your code below:

# Task 1 - Make a variable to keep track of the length of python_topics
length = len(python_topics)

# Task 2 - Make a variable, index, to compare against length
index = 0

# Task 3 - Make the while loop. It should print a string + one element from the list. 
# Failed ALOT here sadly, but it made sense after a while. Could not understand why my code didn't go through 
# with print(length[index]) even though the intepreter told me time and time again I could not use an int.. lol. 
# Hopefully it makes sense going forward. Had to call the original variable ofc, which includes the strings.
# Lesson learned...? Hopefully
while index < length:
	print("I am learning about", python_topics[index])
	index += 1