# Chap 7 - Strings
# 7. Strings are Immutable

# Summarizing we are creating new strings when slizing, selecting characters and concatenating strings. This is 
# because strings are immutable. We can use it to make other strings, but not change one string.

# This property, generally, is known as mutability. Data types that are mutable can be changed, and data types, 
# like strings, that are immutable cannot be changed. 

# 1. Try changing the first character of first_name by running
#       first_name[0] = "R"
# 2. Ups, didnt work right, strings are immutable. Delete code from step 1. Then concatenate the string "R" with a 
#    slice of first_name that included everything but the first character, "B", and save it to a new string
#    called fixed_first_name

first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R"
# TypeError: 'str' object does not support item assignment

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name, last_name)

# Got it
