# Chap 8.1 - Modules
# Modules in Python
# 6. Review

# Modules in Python Review
#
#  You've learned:
# * what modules are and how they can be useful
# * how to use a few of the most commonly used Python libraries
# * what namespaces are and how to avoid polluting your local namespace
# * how scope works for files in Python
#
# Programmers can do great things if they are not forced to constantly reinvent 
# tools that have already been built. With the power of modules, we can import
# any code that someone else has shared publicly. 
#
# In this lesson, we covered some of the Python Standard Library, but you can 
# explore all the modules that come packaged with every installation of Python
# at the Python Standard Library documentation.
#
# This is just the beginning. Using a package manager (like conda or pip3), you 
# can install any modules available on the Python Package Index. 
#
# The sky's the limit!
#
## ...and I'm actually pretty stoked :D While this is for me a slow and steady
## approach, like a marthon, not a sprint. I do start to see potential. 
## I'm gonna keep push on, a bit every day for 3-4 months. I hope that 
## should take me to a place where I can do some cool stuff. 


# This lesson was great. No tasks lol. 

import random

def yolo(swag):
    word = ""
    if swag == "cool":
        word = "Let's go!"
    else:
        word = "Still, let's go!"
    return word

lst = ["cool", "something else"]

long_drumroll = random.choice(lst)

print(yolo(long_drumroll))

# lol, lets go. 