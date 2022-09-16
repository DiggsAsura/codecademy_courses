# Chapter 12 - Python Code Challenges II
# 4. Dictionaries Advanced
# 4. Count First Letter

# This function accepts a dictionary where the keys are last names and the values are
# lists of first names and people who have that last name. We need to calculate
# the number of people who have the same first letter in their last name. Here
# are the steps we need:
#
# 1. Define the function to accept one parameter for our dictionary
# 2. Create a new empty dictionary called letters
# 3. Loop through every key in our names dictionary
# 4. Inside the loop, get the first letter of the last name we are looking at.
#    If the first letter is not in our letter dictionary, add it as a key 
#    with a value of 0. Then, increment that key by the number of people 
#    that have that last name. 
# 5. After the loop, return the letters dictionary
#
# Create a function named count_first_letter that takes a dictionary named
# names as a parameter. names should be a dictionary where the key is a 
# last name and the value is a list of first names. For example, the dictionary
# might look like this:
#
# names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
#
# The function should return a new dictionary where each key is the first letter
# of a last name, and the value is the number of people whose last name 
# begins with that letter. 
#
# So in the example above, the function would return:
# 
# {"S" : 4, "L": 3}

def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))

# This one was tricky, and ended up not only looking at the hint, but actually the solution. 
# Turns out I was somewhat close, but still could not really nail it. 
# problems again was with pt 4. A bit insecure how to deal with adding as keys and values. 
# Might have to find some more dictionary tasks. 

# This function uses two dictionaries instead of one dictionary and one list.
# We iterate through each of the keys (which are the last names) and store the first
# letter of the last name in first_letter. We then use similar logic to what
# we have used before by testing if we have already seen that letter before. If
# we haven't seen that letter before, then we add it to our dictionary with a
# value of 0. Next, we are going to increment the value. Since we know that 
# some people share the last name (as seen by the list of first names in our
# names dictionary), we are going to increment the value in our letters 
# dictionary by the length of first names that share the last name for our 
# current iteration (key).

# thats a mouthful. 