# Chap 8.1 - Modules
# Modules in Python
# 3. Namespaces

# Nice, this explains about aliasing (similar to Bash i guess). In Python aliasing is "as"
# import module_name as name_you_pick_for_the_module

# Tasks
# 1. Below import codecademylib3_seaborn, import pyplot from the module matplotlib with alias plt
# 2. Import random below the other import statements. It's best to keep all imports at the top of your file.
# 3. Create a variable numbers_a and set it equal to the range of numbers 1 through 12 (inclusive)
# 4. Create a variable numbers_b and set it equal to a random sample of twelve numbers within range(1000)
# 5. Now let's plot these number sets against each other using plt. Call plt.plot() with your two variables
#    as it's arbuments
# 6. Now call plt.show() and run your code!

from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)
print(numbers_b)

plt.plot(numbers_a, numbers_b)
plt.show()

# Cool, first thing outside terminal :D


