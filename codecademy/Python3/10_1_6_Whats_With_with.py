# Chap 10
# 1. Learn Python: Files
# 6. Whats's With "with"?

# What's With "with"?
#
# We've been opening these files with this with block so far, but it seems a little
# weird that we can only use our file variable in the indented block. Why is that?
# The with keyword invokes something called a context manager for the file that we're 
# calling open() on. This context manager takes care of opening the file when we call 
# open() and then closing the file after we leave the indented block. 
#
# Why is closing the file so complicated? Well, most other aspects of our code
# deal with things that Python itself controls. All the variables you create:
# integers, lists, dictionaries - these are all Python objects, and Python knowns
# how to clean them up when it's done with them. Since your file exist outside your
# Python script, we need to tell Python when we're done with them so that it can close
# the connection to that file. Leaving a file connection open unnecessarily can 
# affect performance or impact other programs on your computer that might
# be trying to access that file. 
#
# The with syntax replaces older ways to access files where you need to call .close()
# on the file object manually. We can still open a file and append to it with 
# the old syntax, as long as we remember to close the file connection afterwards.
#
#fun_cities_file = open('fun_cities', 'a')
#
# We can now append a line to "fun_cities"
#fun_cities_file.write("Montreal")
# But we need to remember to close the file
#fun_cities_file.close()
#
# In the above script we added "Montreal" as a new line in our file fun_cities.txt
# However, since we used the older-style syntax, we had to remember to close 
# the file afterwards. Since this is necessarily more verbose (requires a least
# one more line of code) without being any more expressive, using with is 
# preferred. 

# Tasks
# 1. In script.py there's a file object that doesn't get closed correctly. Let's
# 	 fix it by changing the syntax!
#
# 	 Remove this line:
#    close_this_file = open('fun_file.txt')
# 
#    And change it to use the with syntax from our previous exercises.
# 
#    Remember to indent the rest of the body so that we don't get an IndentError

#close_this_file = open('fun_file.txt')
with open("fun_file.txt") as close_this_file:
	setup = close_this_file.readline()
	punchline = close_this_file.readline()

print(setup)

