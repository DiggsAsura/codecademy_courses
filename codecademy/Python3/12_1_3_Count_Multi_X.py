# Chapter 12 - Python Code Challenges II
# 1. Strings
# 3. Count Multi X

# Now let's change our function to compare against an entire string instead
# of a single character. This function should accept a string and a substring
# to compare against. The number of occurrences of the second parameter within
# the first parameter string are returned. What this means is that we are 
# checking the number of occurrences of the shorter string (second parameter)
# within the longer string (first parameter). One way to accomplish this is 
# using the split function. Here is how to do that:
# 
# 1. Define the function to accept two parameters. word for the input string
#    and x for the second string we are searthing for
# 2. Split the string into substrings based on the second input parameter
# 3. Count the number of instances the substring appeared in the first
#    input string based on the split string
# 4. Return the result
#
# Write a function named count_multi_char_x that takes a string named word 
# and a string named x. This function should do the same thing as the 
# count_char_x function you just wrote - it should return the number of 
# times x appears in word. However, this time, make sure your function works
# when x is multiple characters long.
#
# For example, count_multi_char_x("Mississippi", "iss") should return 2

def count_multi_char_x(word, x):
  count = 0
  substring = word.split(x)
  for sub in substring:
    count += 1
  
  return count -1


print(count_multi_char_x("Mississippi", "iss"))
print(count_multi_char_x("Apple", "pp"))

# Can't really understand why to subtract 1 - besides the return of 
# substring would be "m", "", "ippi", and we then have to remove the ""??

# In our function, we split the first input string using the second input 
# string. What this does is cut the first string into an array of smaller 
# substrings containing the parts not equal to our second parameter x. 
# For example, when splitting "mississippi" with the string "iss", the 
# resulting array will be [“m”, “”, “ippi”]. This includes the characters 
# before "iss" was found, the empty space between the two instances of 
# "iss" and the characters after the last"iss". Be careful! In order to get 
# the correct result we need to return one less then the total number of 
# split sections — in this example, "iss" was in the string twice, 
# resulting in 3 sections. So we should return 3 - 1.
