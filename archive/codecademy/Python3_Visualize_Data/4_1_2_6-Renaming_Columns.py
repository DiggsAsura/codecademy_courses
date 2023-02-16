# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 2. Modifying DataFrames
# 6. Renaming Columns

'''
When we get our data from other sources, we often want to change the column names.
For example, we might want all of the column names to follow variable name rules,
so that we can use df.column_name (which tab-completes) rather than df['column_name'] 
(which takes up extra space).

You can change all of the column names at once by setting the .columns property
to a different lists. This is great when you need to change all of the column 
names at once, but be careful! You can easily mislabel columns if you get the 
ordering wrong.

Here's an example of correctly renaming all columns at once:


df = pd.DataFrame({
  'name': ['John', 'Jane', 'Sue', 'Fred'],
  'age': [23, 29, 21, 18]
})

df.columns = ['First Name', 'Age']


This command edits the existing DataFrame so that df now looks like this:


First Name    Age
John          23
Jane          29
Sue           21
Fred          18

'''


import pandas as pd

df = pd.read_csv('imdb.csv')
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

print(df)