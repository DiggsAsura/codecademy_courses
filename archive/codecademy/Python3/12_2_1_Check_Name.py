# Chapter 12 - Python Code Challenges II
# 2. Strings Advanced
# 1. Check Name

# You are creating an app that allows users to interact and share their
# coding project ideas online. The first step is to provide your name
# inthe application and a greeting for other people to see which contains
# your name. Let's create a function that is able to check if a user's 
# name is located within their greeting. We need a function that 
# accepts two parameters, a string for our sentence and a string
# for a name. The function should return True if the name exists within 
# the string (ignoring any differences in capitalization). Here is what
# we need to do:
# 
# 1. Define the function to accept two parameters, one string for the sentence
#    and one string for the name
# 2. Convert all of the strings to the same case so we don't have to worry about
#    differences in capitalization
# 3. Check if the name is within the sentence. If so, then return True. Otherwise
#    return False. 
#
# Write a function called check_for_name that takes two strings as parameters
# named sentence and name. The function should return True if name appears in 
# sentence in all lowercase letters, all uppercase letters, or with any mix of 
# uppercase and lowercase letters. The function should return False otherwise.
#
# For example, the following three calls should all return True:
# check_for_name("My name is Jamie", "Jamie")
# check_for_name("My name is jamie", "Jamie")
# check_for_name("My name is JAMIE", "Jamie")

from tabnanny import check


def check_for_name(sentence, name): 
  #if name.lower() in sentence.lower():
  #  return True
  #return False
  return name.lower() in sentence.lower()

print(check_for_name("My name is Kenneth", "Kenneth"))
print(check_for_name("My name is kenneth", "KENNETH"))
print(check_for_name("bla bla bla, Kayi", "kenneth"))