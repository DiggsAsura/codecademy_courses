# Chapter 12 - Python Code Challenges II
# 2. Strings Advanced
# 3. Reverse

# This one is similar to the last challenge. Instead of selecting every other
# letter, we want to reverse the entire string. This can be performed in a 
# similar manner, but we will need to modify the range we are using. Here
# is what we have to do:
#
# 1. Define the function to accept one parameter for the string
# 2. Create a new empty string to hold the reversed string
# 3. Loop through the input string by starting at the end, and working 
#    towards the beginning
# 4. Inside the loop, append the character at the current locationto the new
#    string we initialized earlier
# 5. Return the result
#
# Write a function named reverse_string that has a string named word as a 
# parameter. The function should return word in reverse. 

def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1): # I had to look it up.. fml. 
    reverse += word[i]
  return reverse

print(reverse_string("Kenneth"))

# Bah. It all makes sense when I read the summary, but I'm a bit off on 
# oneshotting these now. Balls balls balls. 

# This is similar to the last solution, but our range has been modified 
# in order to start at the last index of the string (length of the string 
# minus one) up to the first index. Since the parameter for the ending 
# index is exclusive we need to provide the index of one more iteration 
# than what we want to stop at. We want to stop at 0, and since we are 
# incrementing by -1, we will set the ending index to -1. Finally, make 
# sure to add the third parameter of -1. This makes us increment by -1 at 
# each step.