# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 12. Product

'''
When using list comprehension, sometimes the items in the list that you're 
iterating through will be lists themselves! In these cases, you can access
multiple items in those sub-lists by using the following syntax:

original_list = [[1, 2], [3, 4], [5, 6]]
new_list = [item1 + item 2 for (item1, item2) in original_list]

new_list will now contain the sum of each sub-list.
'''

# Ok this is great, something "new", or at least something i didn't think of.
# Not too bad idea to do some of the beginner lines again to refresh and get 
# better understanding of even the basics.

nested_lists = [[4, 8], [5, 16], [23, 42]]
product = [item1 * item2 for (item1, item2) in nested_lists]

print(product)