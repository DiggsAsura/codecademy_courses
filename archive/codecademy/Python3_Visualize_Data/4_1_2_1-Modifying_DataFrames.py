# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 2. Modifying DataFrames
# 1. Modifying DataFrames

'''
In previous lesson, you learned what a DataFrame is and how to select subsets of data
from one. In this lesson, you'll learn how to modify an existing DataFrame. Som of the
skills you'll learn include:

- Adding Columns to a DataFrame
- Renamin columns 

'''

import pandas as pd

df = pd.read_csv('shoefly.csv')

#print(df.head(10))

def titlecase(my_string):
  return my_string.title()

# Remember this. .apply
df['shoe_type'] = df.shoe_type.apply(titlecase)

print(df.head(10))