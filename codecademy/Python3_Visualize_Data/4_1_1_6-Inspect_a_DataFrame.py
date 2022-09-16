# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 6. Inspect a DataFrame

'''
When we load a new DataFrame from a CSV, we want to know what it looks like.

If it's a small DataFrame, you can display it by typing print(df).

If it's a larger DataFrame, it's helpful to be able to inspect a few items without having
to look at the entire DataFrame.

The method .head() gives the first 5 rows of a DataFrame. If you want to see more rows,
you can pass in the positional argument n. For example, df.head(10) would show the first
10 rows.

The method df.info() gives some statistics for each column.
'''


import pandas as pd

df = pd.read_csv('imdb.csv')
print(df.info())