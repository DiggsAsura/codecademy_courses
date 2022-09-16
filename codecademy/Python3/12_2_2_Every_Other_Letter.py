# Chapter 12 - Python Code Challenges II
# 2. Strings Advanced
# 2. Every Other Letter

# For this function, we are going to create a function that extract every other
# letter from a string and returns the resulting string. There are a few different
# ways you can solve this problem. Here are the steps needed for one of the ways:
#
# 1. Define a function to accept one parameter for the string
# 2. Create a new empty string to hold every other letter from the input string
# 3. Loop through the input string while incrementing by two every time
# 4. Inside the loop, append the character at the current location to the new
#    string we initialized earlier
# 5. Return the new string
#
# Create a function named every_other_letter that takes a string named word
# as a parameter. The function should return a string containing every other 
# letter in word. 

def every_other_letter(word):
  new_string = ""
  for letter in range(0, len(word), 2):
    new_string += word[letter]    
  return new_string


print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))

# Ok this sucked a bit, I just could not remember how to iterate every other.
# Kinda makes sense when I read the solution but a bit disappointed really.

# In order to alternate which character is added to the every_other 
# string, we use a range of indices which starts at index 0 (the beginning 
# of our word) and ends at the end of our word. The third parameter in the 
# range function determines what value to increment by. In this case, we 
# want to increment by 2 in order to get every other letter.
#
# Another way to loop through all indices of our original string, 
# but only add the letters that correspond to an even index. As a 
# challenge, try solving this problem that way! (MODULO for sure)