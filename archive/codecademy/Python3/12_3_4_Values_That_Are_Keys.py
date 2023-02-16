# Chapter 12 - Python Code Challenges II
# 3. Dictionaries
# 4. Values That are Keys

# We are making a program that will create a family tree. Using a dictionary, we want to return
# a list of all the children who are also parents of other children. Using dictionaries
# we can consider those people to be values which are also keys in our dictionary of family
# data. Here is what we need to do:
#
# (hmmm, didn't we learn we can not change keys???)
#
# 1. Define the function to accept one parameter for our dictionary
# 2. Create an empty list to hold the values we find
# 3. Loop through every value in the dictionary
# 4. Inside the loop, test if the current value is a key in the dictionary. If it is then
#    append it to the list of values we found
# 5. After the loop, return the list of values which are also keys
#
# Create a function named values_that_are_keys that takes a dictionary named my_dictionary
# as a parameter. This function should return a list of values in the dictionary that 
# are also keys. 
#
# (oook, seems like it's not what I thought at first. we're not modifying the actual keys)

def values_that_are_keys(my_dictionary): 
  lst = []
  for thing in my_dictionary.values():
    if thing in my_dictionary:
      lst.append(thing)
  return lst

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

# close but not quite cigar this time either. This is hard! Have to work alot with it all.
# The good thing, I think i'm through all of the different aspects of Python programming language,
# so now it's more a matter of doing everything alot more, to get more consistent and secure
# about how to write stuff.

# For this solution, we iterate through every value within the dictionary. In order
# to check if it is also a key, we can use the in keyword. This checks the value against
# all of the keys in the dictionary to see if it exists as a key as well. If it does, 
# then we append it to our list of values which are also keys.