# Chapter 12 - Python Code Challenges II
# 1. Strings
# 2. Count X

# Next, we are going to try something a bit different. This time
# we are going to count the number of occurences of a certain letter
# within the string. Our function will accept a parameter for a string
# and another for the character which we are going to count. For example,
# providing the word "mississippi" and the character 's' would 
# result in an answer of 4. These are the steps we need to take. 
#
# 1. Define the function to accept two parameters. word for the input string
#    and x for the single character. 
# 2. Create a counter to keep track of the occurences
# 3. Loop through every letter in the string. If the current letter is equal
#    to the input letter, increase our counter
# 4. Return the counter after looping through the entire string.
#
# Write a function named count_char_x that takes a string named word and a 
# single character named x as parameters. The function should return the 
# number of times x appears in word. 

def count_char_x(word, x):
    count = 0
    for letter in word:
        if letter == x:
            count += 1
    return count

word = input("Word: ")
x = input("Which char to count: ")

print(count_char_x(word, x))