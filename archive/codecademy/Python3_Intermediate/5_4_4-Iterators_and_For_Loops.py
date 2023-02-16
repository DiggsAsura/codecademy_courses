# Learn Intermediate Python 3
# 5. Unit Testing
# 4. Iterators and Generators
# 4. Iterators and For Loops

# Now that we understand how iterators work under the hood, we have all the
# pieces to put the big picture together. Let's look back at the following
# dog_foods dictionary and the for loop that performs the iteration:

dog_foods = {
  "Great Dane Foods": 4,
  "Min Pip Pup Foods": 10,
  "Pawsome Pet Foods": 8
}

for food_brand in dog_foods:
  print(f'{food_brand} has {dog_foods[food_brand]} bags')

# To summarize, the three main steps here are:
#
#   1. The for loop will first retrieve an iterator object for the dog_foods
#      dictionary using iter()
#
#   2. Then, next() is called on each iteration of the for loop to retrieve
#      the next value. This value is set to the for loop's variable, food_brand
#
#   3. On each for loop iteration, the print statement is executed, until
#      finally, the for loop executes a call to next() that raises the 
#      StopIteration exception. The for loop then exits and is finished
#      iterating.

# Let's review the process in a visual format, before moving on to learn
# about creating our very own custom iterators!

# Well I'm not gonna try make this again. It's pretty much the same as the one
# in the introduction.


