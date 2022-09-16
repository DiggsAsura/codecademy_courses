# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 13. Greater Than

nested_lists = [[4, 8], [16, 15], [23, 42]]

greater_than = [num1 > num2 for (num1, num2) in nested_lists]

print(greater_than)