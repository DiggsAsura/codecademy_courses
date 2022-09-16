# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 1. Importing the Pandas Module

'''
Pandas is a Python module for working with tabular data (i.e data in a table with rows and
columns). Tabular data has a log of the same functionality as SQL or Excel, but Pandas adds
the power of Python.

In order to get access to the Pandas module, we'll need to install the module and then import
it into a Python file. To learn how to install Python for data analysiz on your personal
computer, please refer to the following resources.

- Introducing Jupyter Notebook
- Setting Up Jupyter Notebook
- Getting Started with Jupyter Notebook

Otherwise, let's move on! The pandas module is usually imported at the top of a Python file
under the alias pd.


import pandas as pd


If we need to access the pandas module, we can do so by operating on pd.

In this lesson, you'll learn the basicas of working with a single table in Pandas, such as:

- Creating a table from scratch
- Loading data from another file
- Selecting certain rows or columns of a table

Note: In order for Codecademy to properly display data from Pandas, we need to import another
special library (only for the browser thingy)


import codecademylib3


When you're on Codecademy.com, we'll always provide this import for you at the top of 
script.py. 

When you're not on Codecademy.com, you won't need it.

'''


import pandas as pd

df = pd.read_csv('shoefly_orders.csv') # file not included, writing for internalizing

df.head(10) # Get the 10 first rows!

# Select everyone who ordered black sandals!
df[(df.shoe_type == 'sandals') & (df.shoe_color == 'black')]

# Let's see what Susan Dennis ordered
df[(df.first_name == 'Susan') & (df.last_name == 'Dennis')]


