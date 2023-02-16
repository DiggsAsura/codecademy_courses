# Chap 9.1 - Dictionaries
# Creating Dictionaries
# 3. Invalid Keys

# Invalid Keys
# We can have a list or a dictionary as a value of an item in a dictionary, but
# we cannot use these data types as keys of the dictionary. If we try to, we will get a 
# TypeError. 
# 
# For example
#powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# 
# This code will yield: 
# TypeError: unhashable type: 'list'
#
# The word "unhashable" in this context means that this 'list' is an object that
# can be changed. 
#
# Dictionaries in Python rely on each key having a hash value, a specific identifier
# for the key. If the key can change, that hash value would not be reliable. So the
# keys must always be unchangeable, hashable data types, like numbers or strings.

# Tasks
# 1. Run the code inside script.py (well the code in the browser window):
#    You should get an error: 
#		 TypeError: unhashable type
#
#    Make the code run without errors by flipping the items in the dictionary so that
#    the strings are the keys and the lists are the value

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

print(children)
