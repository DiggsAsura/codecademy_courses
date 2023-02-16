# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 2. Modifying DataFrames
# 4. Adding a Column III

'''
Finally, you can add a new column by performing an operation on the existing columns.

Maybe we want to add a column to our inventory table with the amount of sales tax that
we need to charge for each item. The following code multiples each Price by 0.75, the
sales tax for our state:


df['Sales Tax'] = df.Price * 0.75


Now our table has a column called Sales Tax


Product ID	Product Description	Cost to Manufacture	Price	Sales Tax
1	3 inch screw	0.50	0.75	0.06
2	2 inch nail	0.10	0.25	0.02
3	hammer	3.00	5.50	0.41
4	screwdriver	2.50	3.00	0.22
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
df['Revenue'] = df.Price - df['Cost to Manufacture']

print(df)

