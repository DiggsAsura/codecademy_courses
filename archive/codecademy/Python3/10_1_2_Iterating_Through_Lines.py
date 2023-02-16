# Chap 10 - Files
# 1. Learn Python: Files
# 2. Iterating Through Lines

# When we read a file, we might want to grab the whole document in a single string, 
# like .read() would return. But what if we wanted to store each line in a 
# variable? We can use the .readlines() function to read a text file line by line
# instead of having the whole thing. 
# Suppose we have a file:
#
# keats_sonnet.txt
# 
with open("keats_sonnet.txt") as keats_sonnet:
	for line in keats_sonnet.readlines():
		print(line)
#
# The above script creates a temporary file object called keats_sonnet that points
# to the file keats_sonnet.txt. It then iterates over each line in the document
# and prints the entire file out. 

# Tasks
# 1. Using a with statement, create a file object pointing to the file
#    how_many_lines.txt Store that file object in the variable lines_doc
#
# 2. Iterate through each of the lines in lines_doc.readlines() using a for loop.
# 
#    Inside the for loop print out each line of how_many_lines.txt

with open("how_many_lines.txt") as lines_doc:
	for line in lines_doc.readlines():
		print(line)
		
# On the forums theres a discussion about .readlines(), as its the same output
# without the method. No clear answer.. 
