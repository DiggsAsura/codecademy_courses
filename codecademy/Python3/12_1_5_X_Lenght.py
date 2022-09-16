# Chapter 12 - Python Code Challenges II
# 1. Strings
# 5. X Lenght

# Let's use the split method in a different way. We need a few new function
# that is able to accept two inputs: one for a sentence and another for 
# a number. The function returns True if every single word in the sentence has
# a length greater than or equal to the number provided. These are the steps:
#
# 1. Define the function to accept two parameters, one string, and one number
# 2. Split the sentence into an array of words
# 3. Loop through the words. If the lengh of any of the words is less than
#    the number provided, return False
# 4. If we made it through the loop without returning False, return True. 
#
# Create a function called x_length_words that takes a string named 
# sentence and an integer named x as parameters. This function should 
# return True if every word in sentence has a length greater than or 
# equal to x. 

def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words: 
    if len(word) < x:
      return False
  return True

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

# We can use the split function with the space character provided in 
# order to get an array of all of the words in the sentence. Next, we 
# use the in keyword in order to loop through every element in our array 
# of words. We check the length of each word and compare it against x to 
# see if it is shorter. If any of the words in the array are shorter then 
# we immediately return False and end the function. If we make through all 
# of the words without returning False, we know we should return True since 
# all of the word’s lengths were longer than x. 