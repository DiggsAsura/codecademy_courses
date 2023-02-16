# Chap 7.2 - Strings
# String Methods
# 1. Introduction

"""
Introduction

Do you have a gigantic string that you need to parse for information? Do you need to sanitize a users input to work in a function? Do you need to be able to generate outputs with variable values? All of these things can be accomplished with string methods!

Python comes with built-in string methods that gives you the power to perform complicated tasks on strings very quickly and efficiently. These string methods allow you to change the case of a string, split a string into many smaller strings, join many small strings together into a larger string, and allow you to neatly combine changing variables with string outputs.

In the previous lesson, you worked with len(), which was a function that determined the number of characters in a string. This, while similar, was NOT a string method. String methods all have the same syntax:

string_name.string_method(arguments)

Unlike len(), which is called with a string as its argument, a string method is called at the end of a string and each one has its own method specific arguments.
"""

# Ok so finally learned the difference between functions and .methods() :D
# Oh and we can also use several methods in a row. 

# Bunch of examples, as this is just the introductions theres no task.

print('Hello world'.upper())
print('Hello world'.lower())
print('Hello world'.title())
print('Hello world'.split())
print(' '.join(['Hello', 'world']))
print(''.join(['Hello', 'world']))
print('Hello world'.replace('H', 'J'))
print('   Hello world   '.strip())
print('{} {}'.format("Hello", "world"))

# Cool stuff :D
