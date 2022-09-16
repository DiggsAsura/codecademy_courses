# Chapter 12 - Python Code Challenges II
# 2. Strings Advanced
# 4. Make Spoonerism

# A Spoonerism is an error in speech when the first syllables of two words
# are switched. For example, a Spoonerism is made when someone says "Belly 
# Jeans" instead of "Jelly Beans". We are going to make a function that is 
# similar, but instead of using the first syllable, we are going to switch
# the first character of two words. Here is what we have to do:
#
# 1. Define the function to accept two parameters for our two words
# 2. Get the first character of the first word and the first character of
#    the second word
# 3. Get the remaining characters of the first word and the remaining chars 
#    of the second word
# 4. Append the first character of the second word to the remaining char
#    of the first word
# 5. Append a space character
# 6. Append the first character of the first word to the remaining char of 
#    the second word
# 7. Return the result
#
# Write a function called make_spoonerism that takes two string as parameters
# named word1 and word2. Finding the first syllable of a word is a 
# difficult task, so for our function, we're going to switch the first letters
# of each word. Return the two new words as a single string separated by a 
# space.

def make_spoonerism(word1, word2):
  return word2[0]+word1[1:len(word1)] + " " + word1[0]+word2[1:len(word2)]

print(make_spoonerism("Kenneth", "Bjerke"))

# BOOM, talking about oneshotting. Finally one :D

# We can accomplish the task in one line by appending and slicing at
# the same time. We can get the first index of our words by using word1[0] 
# and word2[0] which gets the letter at the first index. In order to get the 
# remaining letters we can use word1[1:] and word2[1:]. This returns all 
# characters in the strings starting with index 1 and on. We 
# concatenate everything together to get the result.