# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 14. First Only

nested_lists = [[4, 8], [16, 15], [23, 42]]

first_only = [num1 for (num1, num2) in nested_lists]
print(first_only)