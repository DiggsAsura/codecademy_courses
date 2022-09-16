# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 3. Create a DataFrame II

'''
You can also add data using lists.

For example, you can pass in a list of lists, where each one represents a row of data.
Use the keyword argument columns to pass a list of column names.


df2 = pd.DataFrame([
  ['John Smith', '123 Main St.', 34],
  ['Jane Doe', '456 Maple Ave', 28],
  ['Joe Schmo', '789 Broadway', 51]
  ],
  columns=['name', 'address', 'age'])


This command produces a DataFrame df2 that looks like this:


name           address             age
John Smith     123 Main St.        34
Jane Doe       456 Maple Ave.      28
Joe Schmo      789 Broadway        51


In this example, we were able to control the ordering of the columns because we used
lists.

'''


import pandas as pd 

df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]],
  columns=[
    'Store ID', 'Location', 'Number of Employees'
  ])

print(df2)
