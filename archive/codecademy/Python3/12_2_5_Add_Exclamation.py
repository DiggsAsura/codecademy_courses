# Chapter 12 - Python Code Challenges II
# 2. Strings Advanced
# 5. Add Exclamation

# Let's say we are writing a program that displays a large message on a 
# blimp and we need to fill in any missing space if a short phrase is 
# provided. Our function will accept a string and if the size is less 
# than 20, it will fill in the remaining space with exclamation marks
# until the size reaches 20. If the provided string already has a 
# length greater than 20, then we will simply return the original string.
# Here are the steps:
#
# 1. Define the function to accept one parameter for our string
# 2. Loop while the length of our input string is less than 20
# 3. Inside the loop, append an exclamation mark
# 4. Once done, return the result
#
# Create a function named add_exclamation that has one parameter named word.
# This function should add exclamation points to the end of word until word
# is 20 characters long. If word is already at least 20 characters long, just 
# return word. 

# Hint!
# Use a while loop to add exclamation points to word. The while loop should
# stop when the length of word is greater than or equal to 20. 

def add_exclamation(word):
  while len(word) < 20:
    word += "!"
  return word

print(add_exclamation("Kenneth"))

# Holy moly - the return of the while loop. I can count on one hand how many
# times this entire course have touched that. Freaking about time. I don't
# remember how to use it though... So gonna have to look up for sure. 
#
# Ok this is probably why while loops is not been that much touched. It's
# quite few usecases maaaybe? At least for loops is way more useful?? 