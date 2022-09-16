# Chapter 12 - Python Code Challenges II
# 1. Strings
# 4. Substring Between

# Here is a challenging problem. We need a function that is able to extract
# a portion of a string between two characters. The functionwill take three
# parameters where the first parameter is the string we are going to extract
# the substring from, the second input is the starting character of our 
# substring and the third character is the ending character of our substring.
# Here are the steps we can use:
#
# 1. Define the function to accept three parameters, one string and two 
#    characters
# 2. find the starting index of our substring using the second input parameter
# 3. find the ending index of our substring using the third input parameter
# 4. If neither of the indices are -1, return the portion of the first 
#    input parameter string between the starting and ending indicies (not 
#    including the starting and ending index)
# 5. If either of the indices are -1, that means the start or ending of the
#    substring didn't exist in our string. Return the original string in 
#    this case
#
# Write a function named substring_between_letters that takes a string named
# word, a single character named start, and another character named end. This
# function should return the substring between the first occurence of start
# and end in word. If start or end are not in word, the function should return
# word.
#
# For example, substring_between_letters("apple", "p", "e") should return "pl"

def substring_between_letters(word, start, end): 
  sub1 = word.find(start)
  sub2 = word.find(end)
  if sub1 != -1 and sub2 != -1:
    return word[sub1+1:sub2]
  else: 
    return word
  
  
print(substring_between_letters("apple", "p", "e"))

# Ok I pretty much got it correct, except I still bug out a bit because of 0/1
# still it seems. At first I wrote return word[sub1:sub2], where sub1 needs +1
# to get the expected output.

# Explained like this
# We provide the starting index plus one in order to not include the 
# starting character. We do not need to provide the end index plus one, 
# since the value on the right of the colon is excluded. This causes our 
# slicing to look like: word[start_ind+1:end_ind]).