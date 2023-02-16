# Chap 8.1 - Modules
# Modules in Python
# 5. Files and Scope

# You may remember the concept of scope when you were learning about functions
# in Python. If a variable is defined inside of a function, it will not be accessible
# outside of the function.
#
# Scope also applies to classes and to the files you are working within.
#
# Files have scope? You may be wondering.
#
# Yes. Even files inside the same directory do not have access to each other's 
# variables, functions, classes, or any other code. So if I have a file
# sandwiches.py and another files hungry_people.py, how do I give my hungry
# people access to all the sandwiches I defined? 
#
# Well, files are actually modules, so you can give a file access to another
# file's content using that glorious import statement.
#
# With a single line of from sandwiches import sandwiches at the top of 
# hungry_people.py, the hungry people will have all the sandwiches they could
# ever want. 

# WELL, what can I say, this topic comes in hot at the perfect time! This is
# something I look to learn more on, as I kinda want to make a little project for 
# myself, where I easily see that it will be handy to make it over several files
# to keep code cleaner (yea, a little turned based terminal RPG, Final Fantasy
# inspired, haha let's see how THAT goes but yea)

# Tasks
# 1. Tab over to library.py (a second file!) and define a function always_three()
#    with no parameters that returns 3.
#
# 2. Call your always_three() function in script.py (main file). Check out that
#    error message you get in the output terminal and the consequences of the file
#    scope. 
#
# 3. Resolve the error with an import statement at the top of script.py (main file)
#    that imports your function from library. Run your code and watch
#    import do its magic!
# 
# Oh and also, I write all of these to try internalize as much as possible - even 
# if it's not just the code! 

from library import always_three
print(always_three())