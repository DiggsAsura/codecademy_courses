# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 2. Create a DataFrame I

''' 
A DataFrame is an object that stores data as rows and columns. You can think of a 
DataFrame as a spreadsheet or as a SQL table. You can manually create a DataFrame or fill
it with data from a CSV, an Excel spreadsheet, or a SQL query.

DataFrames have rows and columns. Each column has a name, which is a string. Each row has
index, which is an integer. DataFrames can contain many different data types: strings,
ints, floats, tuples, etc.

You can pass in a dictionary to pd.DataFrame(). Each key is a colun name and each value is
a list of column values. The columns must all be the same lenghts or you will get an error. 
Here's an example:


df1 = pd.DataFrame({
  'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
  'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
  'age': [34, 28, 51]
})


This command creates a DataFrame called df1 that looks like this:


address              age   name
123 Main St.         34    John Smith
456 Maple Ave.       28    Jane Doe
789 Broadway         51    Joe Schmo


Note that the columns will appear in alphabetical order because dictionaries don't have
any inherent order for columns.

'''

import pandas as pd

df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
  
})

print(df1)