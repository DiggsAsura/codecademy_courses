# Chapter 12 - Python Code Challenges II
# 3. Dictionaries
# 5. Largest Value

# For the last challenge, we are going to create a function that is able to find the 
# maximum value in the dictionary and return the associated key. This is a twist on 
# the max algorithm since it is using a dictionary rather than a list. These are the steps:
#
# 1. Define the function ao accept one parameter for our dictionary
# 2. Initialize the starting key to a very low number
# 3. Initialize the starting value to a very low number
# 4. Iterate through the dictionary's key/value pairs
# 5. Inside the loop, if the current value is larger than the current largest value, 
#    replace the largest key and largest value with the current ones you are looking at
# 6. Once you are done iterating through all key/value pairs, return the key which 
#    has the largest value
#
# Write a function named max_key that takes a dictionary named my_dictionary as a parameter.
# The function should return the key associated with the largest value in the dictionary.

def max_key(my_dictionary):
  s_key = float("-inf") # could be 0, but this also work, also better!
  s_value = float("-inf") # yea same as above
  for key, value in my_dictionary.items():
    if value > s_value:
      s_key = key
      s_value = value 
  return s_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))


# remember for key, value in something.items() .items() .items() .items()
# This was literally the only thing. I tried with .values... 
# Balls, so close!

# In order to program the max algorithm using dictionaries, we need to keep track of the max
# value and the key which is used to access it. We start by using float("-inf") in order to 
# initialize them to the lowest possible value. To retrieve the key and value at the same time,
# we use the items() function. (.item .item .item .item, remember gdi). Inside our loop, we 
# overwrite the current largest value and the key used to access whenever we find a larger 
# value. We return the largest valu's key once we have iterated through the entire dictionary.