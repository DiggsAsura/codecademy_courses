# Chapter 12 - Python Code Challenges II
# 4. Dictionaries Advanced
# 2. Frequency Count

# This next function is similar, but instead of counting the length of each
# string in the list of strings, we will be counting the frequency of each
# string. This function will also accept a list of strings as input
# and return a new dictionary. Here is what we have to do:
#
# 1. Define the function to accept one parameter for our list of strings
# 2. Create a new empty dictionary
# 3. Loop through every string in the list of strings
# 4. Inside the loop, if the string is not already in our dictionary, store
#    the string as a key with a value of 0 in our dictionary. Then, 
#    increment the value by 1
# 5. After the loop, return the new dictionary
#
# Write a function named frequency_dictionary that takes a list of elements
# named words as a parameter. Thie function should return a dictionary 
# containing the frequency of each element inwords. 

def frequency_dictionary(words):
  final = {}
  for word in words:
    if word not in final:
      final[word] = 0
    final[word] += 1
        
  return final


print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))


# Had to look at the solution, and yet again, very close but not quite. Looks
# like I tend to overcomplicate whats going into the loop a bit. 

# To create a new dictionary we set a variable equal to {}. We iterate through 
# each of the strings in the list of strings and check if it is already in our 
# dictionary using the "in" keyword. If it is not then we add it as a new
# key-value pair where the value is 0. Regardless of wheter the string was
# already in the dictionary, increase the value by 1. This will make it so
# all new entries will have a value of 1 and all existing entries will increase
# their old value by 1. 

