# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 2. Modifying DataFrames
# 5. Performin Column Operations

'''
In the previous exercise, we learned how to add columns to a DataFrame.

Often, the column that we want to add is related to existing colums, but requires
a calculation more complex than multiplication or addition.

For example, imagine that we have the following table of customers:


Name             Email
JOHN SMITH       john.smith@gmail.com
Jane Doe         jdoe@yahoo.com
Joe Schmo        joeschmo@hotmail.com


It's a little annoying that the capitalization is different for each row. Perhaps
we'd like to make it more consistent by making all of the letters uppercase.

We can use the apply function to apply a function to every value in a particular
column. For example, this code overwrites the existing Name columns by applying a 
function uppercase() to every row in Name.


def uppercase(my_string):
  return my_string.upper()

df['Name'] = df['Name'].apply(uppercase)


The result


Name            Email
JOHN SMITH      john.smith@gmail.com
JANE DOE        jdoe@yahoo.com
JOE SCHMO       joeschmo@hotmail.com


'''

import pandas as pd

def lowercase(my_string):
  return my_string.lower()

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
  columns=['Name', 'Email']
)


# Add new colum with lowercase names
df['Lowercase Name'] = df['Name'].apply(lowercase)

print(df)