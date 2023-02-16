# Chap 8.1 - Modules
# Modules in Python
# 2. Random

# Tasks
# 1. Import the random library
# 2. Create a variable random_list and set it equal to an empty list
# 3. Turn the empty list into a list comprehension that uses random.randint() to generate a random
#    integer between 1 and 100 (inclusive) for each number in range(101).
# 4. Create a new variable randomer_number and set it equal to random.choice() with random_list as an argument
# 5. Print randomer_number out to see what number was picked!

# So here, only list comprehension is the mindbug. In the Loops chapter, this was undoubtly the one we went through
# the least. Probably have to look up some hint here. 

import random

random_list = [random.randint(1, 101) for i in range(101)]  # hope we gonna go through this more. 

randomer_number = random.choice(random_list)
print(randomer_number)
