# Chap 8.1 - Modules
# Modules in Python
# 4. Modules Python Decimals

# Ok the saga continues! And it feels GREAT! I'm lagging a bit behind, becahse my trial over at 
# Codecademy ran out, and I was debating wether or not to buy a PRO plan for a year. I did, after
# they gave a 50% discount thingy. Hope it's worth it! 
# Started to fiddle with JavaScript in the meantime, but I really think it's better to get this course
# done first, then go on to do more projects on my own. 

# Modules Python Decimals
# Let's say you are writing software that handles monetary transactions. If you used Python's built-in
# floating-point arithmetic (link to Wikipedia) to calculate a sum, it would result in a weirdly formatted
# number. 

#cost_of_gum = 0.10
#cost_of_gumdrop = 0.35

#cost_of_transaction = cost_of_gum + cost_of_gumdrop
#print(cost_of_transaction) # Returns 0.44999999999999996

# Being familiar with rounding errors in floating-point arithmetic you want to use a data type that 
# performs decimal arithmetic more accurately. You could do the following: 

print("Example in the intro text")
from decimal import Decimal
cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')
cost_of_transaction = cost_of_gum + cost_of_gumdrop
print(cost_of_transaction)
print("=======\n")

### Note to self. Notice how Decimal work. Is this something new, or did I just forget stuff being 
### a couple days off?

# Above, we use the decimal module's Decimal data type to add 0.10 with 0.35. Since we used the Decimal
# type the arithmetic acts much more as expected.

# Usually, modules will provide functions or data types that we can then use to solve a general
# problem, allowing us more time to focus on the software that we are building to solve a more 
# specific problem. 

# Ready, set, fix some flaoting point math by using decimals! 

### Wonder if it's a Python problem, that arithmetical thingy, where adding the above numbers end up 
### with that decimal issue. Hmm. Cool this is a fix though, but still strange!

# Tasks
# 1. Run your code to see the wird floating point match that occurs
# 2. Import Decimal from the decimal module
# 3. Use Decimal to make two_decimal_points only have two decimal points, and four_decimal_points
#    to only have four decimal points.

# 2 - already imported above

two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points) # Ok got it, but why does this noe only print two decimals???

