# 1. Introduction to Python
# 1. Introduction to Data Visualization
# 1. Why Data Vizualization
# 3. Formatting

'''
The first step in the data visualization process is cleaning and prepping the data.
This step is different depending on the type of data format or the file you are
visualizing.

Data are stored in different formats for different purposes. This path will 
explore multiple data formats:

- Python lists are a collection of items separated by commas and enclosed in
  square brackets, such as:
  ['item 1', 'item 2', 'item 3']

- CSVs are text-only spreadsheet files. CSV is an abbreviation for "Comma Separated
  Values". The file looks like a spreadsheet, but with commas separating each value
  in the cells.

- Pandas dataframes are a data structure from the Pandas Python Analysis library.
  We will learn more about them in the future. For now, note that dataframes make
  it easy to conduct powerful operations on your data.

We have chosen to work in these formats because they are popular, acccessible and
used in multiple industries.

'''

import pandas as pd

df = pd.read_csv('global_population-1_1_1_3.csv')
print(df)