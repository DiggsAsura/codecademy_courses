# Review after going through for, while, control loops (break continue), how to 
# avoid infinite loops and list comprehensions
#
# List comprehensions is still a bit difficult to me, but others is quite smooth. 

# Task 1 - Create a list called single_digits that consists of the numbers 0-9 (inclusive)
# Task 2 - Create a for loop that goes through the variable and prints out each one
# Task 3 - Before the loop, create a list called squares, and assign it to be empty to begin with
# Task 4 - Inside the loop that iterates through single_digits, append the squared value of 
# each element of single_digigts to the list squares. You can do this before and after printing the element
# Task 5 - After the for loop, print out squares
# Task 6 - Create the list cubes using a list comprehension of the single_digits list.
# Each element of cubes should be an element of single_digits taken to the third power (exponent)
# Task 7 - Print cubes

single_digits = range(0, 10)
squares = []

for digit in single_digits:
    print(digit)
    squares.append(digit * digit)
    digit += 1

print(squares)

# Task 6 - the hard one. List comprehension... 
#cubes = [single_digits ** 3 for cubes in single_digits] # nope
cubes = [cube ** 3 for cube in single_digits] # still dont really get this.. bah. 
print(cubes)

