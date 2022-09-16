# Chapter 12 - Python Code Challenges II
# 1. Strings
# 1. Count Letters

# For the first code challenge, we are going to count the number of unique 
# letters in a string. This means that when we are looking at the word,
# any new letters should be counted and any duplicates should not be counted.
# There are a few ways to solve this, but we can use the provided alphabet
# string to ensure that duplicates are not counted. Here is what we need
# to do:
# 
# 1. Define the function to accept one parameter - the word whose letters
#    we are counting
# 2. Create a counter to keep track of unique letters
# 3. Loop through every letter in our alphabet string. If the current letter
#    was found in our word, increase our count
# 4. Return the count after looping through all letters.

# Write a function called unique_english_letters that takes the string
# word as a parameter. The function should return the total number of 
# unique letters in the string. Uppercase and lowercase letters should 
# be counted as different letters.
#
# We've given you a list of every uppercase and lowercase letter in the 
# English alphabet. It will be helpful to include that list in your 
# function.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  unique_letters = 0
  for letter in letters:
    if letter in word:
      unique_letters += 1
  
  return unique_letters
    

word = input("Count unique letters in this word: ")

print(unique_english_letters(word))


# THIS was embarrasing. I was back and forth a billiion times, as i thought
# this was cakewalk (and it really is lol). However got stuck on iterating
# the wrong thing first. I started by iterating the word, which gave
# the wrong answer. Changed to iterate the letters first, then it was ok. 
# Balls lol. 