# Chapter 12 - Python Code Challenges II
# 3. Dictionaries
# 3. Add Ten

# Let's loop through the keys again, but this time let's modify the values within the dictionary.
# Our function should add 10 to every value in the dictionary and return the modified
# dictionary. Here is what we need to do:
#
# 1. Define the function ao accept one parameter for our dictionary
# 2. Loop through every key in the dictionary
# 3. Retrieve the value using the key and add 10 to it. Make sure to re-save the new value
#    to the original key.
# 4. After the loop, return the modified dictionary
#
# Create a function named add_ten that takes a dictionary with integer values named 
# my_dictionary as parameter. The function should add 10 to every value in 
# my_dictionary and return my_dictionary

def add_ten(my_dictionary):  
  for value in my_dictionary.keys():
    my_dictionary[value] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))

# Ok it's like allmost on all these, but not quite. Slow learner.. bah.

# We use a for loop to iterate through each key and we access the value using the key. 
# After accessing it, we overwrite the value with the value + 10. Finally, we reutnr the 
# modified dictionary.