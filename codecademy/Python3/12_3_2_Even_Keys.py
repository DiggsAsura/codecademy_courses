# Chapter 12 - Python Code Challenges II
# 3. Dictionaries
# 2. Even Keys

# Next, we are going to do something similar, but we are going to use the keys in order to 
# retrieve the values. Additionally, we are going to only look at every even key within
# the dictionary. Here are the steps:
#
# 1. Define the function to accept one parameter for our dictionary
# 2. Create a variable to keep track of our sum
# 3. Loop through every key in the dictionary
# 4. Inside the loop, if the key is even, add the value from the even key
# 5. After the loop, return the sum.
#
# Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all
# integer keys and values, as parameters. This function should return the sum of the values
# of all even keys. 

def sum_even_keys(my_dictionary):
  sum = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      sum += my_dictionary[key]
  return sum

print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

# I'm so close on these, but i failed on sum += my_dictionary[key]. Tried with like key[value] etc.
# Not really sure why it count the value here, but maybe thats just how dictionaries work? Let's 
# read the explanation:

# Simiar to the previous problem, we are iterating through our dictionary, except this time we are
# iterating through the keys instead of the values. In order to get the keys we use keys() function
# and to get the value of a key we can use brackets (<<--- remember that this returns the value of
# the key!!!). To test if the key is even we use the modulus operator and test if the remainder is 
# 0 when dividing by 2.