# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 14. Setting indices

'''
When we select a subset of a DataFrame using logic, we end up with non-consecutive
indices. This is inelegant and makes it hard to use .iloc()

We can fix this using the method .reset_index(). For example, here is a DataFrame
called df with non-consecutive indices:


   First Name       Last Name
0  John             Smith
4. Jane             Doe
7. Joe              Schemo


If we use the command df.reset_index(), we get a new DataFrame with a new set of 
indices:


   index    First Name     Last Name
0  0        John           Smith
1  4        Jane           Doe
2  7        Joe            Schemo


Note that the old indicices have been moved into a new column called index. Unless
you need those values for something special, it's probably better to use the keyword
drop=True so that you don't end up with that extra column. If we run the command
df.reset_index(drop=True), we get a new DataFrame that looks like this:


  First Name    Last Name
0 John          Smith
1 Jane          Doe
2 Joe           Schmo


Using .reset_index() will return a new DataFrame, but we usually just want to modify
our existing DataFrame. If we use the keyword inplace=True we can just modify our
existing DataFrame.
'''

import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

df2 = df.loc[[1, 3, 5]]
print(df2)

df3 = df2.reset_index(drop=True)
print(df3)