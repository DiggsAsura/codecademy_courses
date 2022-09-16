# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 16. Divide With Zip

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

quotients = [num1 / num2 for (num1, num2) in zip(b, a)]
print(quotients)

# actually i got the right output, but not exactly what the instructions
# was looking for...

quotients2 = [item2 / item1 for (item1, item2) in zip(a, b)]
print(quotients2)