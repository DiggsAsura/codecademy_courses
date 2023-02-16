# Chapter 12 - Python Code Challenges II
# 4. Dictionaries Advanced
# 1. Word Length Dict

# Let's start by writing a function that creates a new dictionary based on a 
# list of strings. The keys of our dictionary will be every string in our list
# of strings, while the values will be the length of each of the words in 
# the string list. Here are the steps:
#
# 1. Define the function to accept one parameter for our list of strings
# 2. Create a new empty dictionary
# 3. Loop through every string in the list of strings
# 4. Inside the loop, add the string as a key and the length of the string
#    as value to the dictionary
# 5. After the loop, return the new dictionary
#
# Write a function named word_length_dictionary that takes a list of strings
# named words as a parameter. The function should return a dictionary of 
# key/value pairs where every key is a word in words and every value is
# the length of that word

def word_length_dictionary(word):
  final = {}
  for keyvalue in word:
    final[keyvalue] = len(keyvalue)
  return final

print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))

# What's happening inside the for-loop was the question. It makes sense, but
# could not come up with the exact one. Practice practice practice. The 
# hint was enough though, did not have to look at the solution :)

# To create a new dictionary we set a variable equal to {}. Whilte iterating
# through each string in our string list, we can add the key and value 
# to our dictionary using this syntax: 
# final[keyvalue] = len(keyvalue)