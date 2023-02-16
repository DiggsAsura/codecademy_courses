# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 15. Review

'''
You've completed the lesson! You've just learned the basics of working with a single
table in Pandas, including:

- Create a table from scratch

- Loading data from another file

- Selecting certain rows or columns of a table

Let's practice what you've learned

'''

import pandas as pd

orders = pd.read_csv('shoefly.csv')

#print(orders.head(5))

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]
print(frances_palmer)

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]
#print(comfy_shoes)