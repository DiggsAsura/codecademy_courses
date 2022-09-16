# Chapter 12 - Python Code Challenges II
# 4. Dictionaries Advanced
# 3. Unique Values

# Now let's try reading a dictionary as input and finding how many values are
# unique. The functions should return a number which is the count of all
# values from the dictionary without including duplicates. These are 
# the steps:
#
# 1. Define the function to accept one parameter for our dictionary
# 2. Create a new empty list
# 3. Loop through every value in our dictionary
# 4. Inside the loop, if the value is not already in our list, append the 
#    value to our list
# 5. After the loop, return the length of our list
#
# Create a function named unique_values that takes a dictionary named
# my_dictionary as a parameter. The function should return the number of
# unique values in the dictionary. 

def unique_values(my_dictionary):
  unique_lst = []
  for value in my_dictionary.values():
    if value not in unique_lst:
      unique_lst.append(value)  
  
  return len(unique_lst)


print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))


# Omg, i got this one! Good thing, i do remember how to check .keys() or 
# .values() in dictionaries now at least :D

# This function has a similar structure to thelast one except that the
# input has been changed to a dictionary. We iterate through eac of the 
# values and whenever we find one we have not added to our list already,
# we add it to the list. After the loop, we return the length of the 
# list since that contains all unique values from the dictionary.