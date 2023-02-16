# Chapter 12 - Python Code Challenges II
# 3. Dictionaries
# 1. Sum Values

# For the first code challenge, we are going to look at only the values in a dictionary. This
# function should sum up all of the values from the key-value pairs in the dictionary. Here
# are the steps we need.

# 1. Define the function to accept one parameter for our dictionary
# 2. Create a variable to keep track of our sum
# 3. Loop through every value in the dictionary
# 4. Inside the loop, add each value to the sum
# 5. Return the sum
#
# Write a function names sum_values that takes a dictionary named my_dictionary as a parameter.
# The function should return the sum of the values of the dictionary

def sum_values(my_dictionary):
  total_value = 0
  for value in my_dictionary.values():
    total_value += value
  return total_value

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))

# Ok, allmost got it. I just have to remember that, for calling a dictionary's value, use .values()

# We start by creating a variable to keep track of the total. Next, we use the values() function
# in our for loop in order to iterate through each of the values in the dictionary. Using this, 
# we can access each value and add it to our total_value variable. At the end of our loop, 
# we return total_value. 