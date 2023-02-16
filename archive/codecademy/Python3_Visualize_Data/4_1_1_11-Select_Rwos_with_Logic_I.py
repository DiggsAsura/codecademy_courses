# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 11. Select Rows with Logic I

'''
You can select a subset of a DataFrame by using logical statements:


df[df.MyColumnName == desired_column_name]


We have a large DataFrame with information about our customers. A few of the many rows
look like this:


name	address	phone	age
Martha Jones	123 Main St.	234-567-8910	28
Rose Tyler	456 Maple Ave.	212-867-5309	22
Donna Noble	789 Broadway	949-123-4567	35
Amy Pond	98 West End Ave.	646-555-1234	29
Clara Oswald	54 Columbus Ave.	714-225-1957	31
…	…	…	…


Suppose we want to select all rows where the customer's age is 30. We would use:


df[df.age == 30]


In Python, == is how we test if a value is exactly equal to another value.

We can use the other logical statements, such as:

- Greater than >
- Less than <
- Not equal !=

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
           'clinic_west'])


january = df[df.month == 'January']
print(january)