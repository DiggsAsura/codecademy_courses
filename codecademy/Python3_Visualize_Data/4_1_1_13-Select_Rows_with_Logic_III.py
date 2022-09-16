# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 13. Select Rows with Logic III

'''
Suppose we want to select the rows where the customer's name is either 'Martha Jones',
'Rose Tyler' or 'Amy Pond'.

name	address	phone	age
Martha Jones	123 Main St.	234-567-8910	28
Rose Tyler	456 Maple Ave.	212-867-5309	22
Donna Noble	789 Broadway	949-123-4567	35
Amy Pond	98 West End Ave.	646-555-1234	29
Clara Oswald	54 Columbus Ave.	714-225-1957	31
…	…	…	…


We could use the isin command to check that df.name is one of a list of values:


df[df.name.isin(['Martha Jones', 'Rose Tyle', 'Amy Pond'])]
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

jan_feb_mar = df[df.month.isin(['January', 'February', 'March'])]

print(jan_feb_mar)