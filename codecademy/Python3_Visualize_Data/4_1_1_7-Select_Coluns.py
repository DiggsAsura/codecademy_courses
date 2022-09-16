# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 7. Select Columns

'''
Now we know how to create and load data. Let's select parts of those datasets that are
interesting or important to our analyses.

Suppose you have the DataFrame called customers, which contains the ages of your customers:


name                   age
Rebecca Erikson        35
Thomas Roberson        28
Diane Ochoa            42
...                    ...


Perhaps you want to take the average or plot a histogram of the ages. In order to do either
of these tasks, you'd need to select the column.

There are two possible syntaxes for selecting all values from a column:

1. Select the column as if you were selecting a value from a dictionary using a key. In
   our example, we would type customers['age'] to select the ages.

2. If the name of a column follows all of the rules for a variable name (doesn't start
   with a number, doesn't contain spaces or special characters, etc.), then you can select
   it using the following notation:
   df.MySecondColumn. In our example, we would type customers.age

When we select a single column, the result is called a Series.

'''

import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east', 'clinic_north', 'clinic_south', 'clinic_west'])


clinic_north = df.clinic_north
print(type(clinic_north))