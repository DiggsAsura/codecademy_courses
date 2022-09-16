# Chap 7.2 - Strings
# String Methods
# 3. Splitting Strings

# Intro text teach us about .split() which will create an entirly different object out of the strings: list
# I have to question though, as I read earlier that strings in fact are lists... however. Let's go with it for now. I do 
# understand what they mean :P

# .split() takes one argument and returns a list of substrings found between the given argument (which with .split() is known 
# as the "delimiter"). 
"""
string_name.split(delimiter)
"""
# If you do not provide an argument it will default to slitting at spaces.
# Goes on do demonstrate just that how it makes a list out of all the words in a string. BTW, i have been looking for 
# this, so this might be a solution for a word count thingy. 
# However it does not go on to demonstrate how its done with a delimiter/argument though. 

# 1. Use .split() to create a list called line_one_words that contains each word in this line of poetry

line_one = "The sky has given over"
line_one_words = line_one.split()

print(line_one_words)
