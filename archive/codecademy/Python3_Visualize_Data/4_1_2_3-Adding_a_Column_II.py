# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 2. Modifying DataFrames
# 3. Adding a Column II

'''
We can also add a new column that is the same for all rows in the DataFrame.
Let's return to our inventory example:

Product ID	Product Description	Cost to Manufacture	Price
1	3 inch screw	0.50	0.75
2	2 inch nail	0.10	0.25
3	hammer	3.00	5.50
4	screwdriver	2.50	3.00


Suppose we know that all of our products are currently in-stock. We can add a column
that says this:


df['In Stock?'] = True


Now all of the rows have a column called In Stock? with value True (scroll to the right
to see the entire table).

Product ID	Product Description	Cost to Manufacture	Price	In Stock?
1	3 inch screw	0.50	0.75	True
2	2 inch nail	0.10	0.25	True
3	hammer	3.00	5.50	True
4	screwdriver	2.50	3.00	True
'''


import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Add columns here 
# Notice, if the same value is going into all the rows, can write like this!
df['Is taxed?'] = 'Yes'



print(df)