# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 4. Comma Separated Variables (CSV)

'''
We now know hot to create our own DataFrame. However, most of the time, we'll be working
with datasets that already exist. One of the most common formats for big datasets is the
CSV.

CSV (comma separated values) is a text-only spreadsheet format. You can find CSVs in lots
of places:

- Online datasets (here's an example from data.gov)
  https://catalog.data.gov/dataset?res_format=CSV

- Export from Excel or Google Sheets

- Export from SQL

The first row of a CSV contains column headings. All subsequent rows contain values. Each
column heading and each variable is separated by a comma:

column1,column2,column3
value1,value2,value3

The example CSV represents the following table:

column1     column2     column3
value1      value2      value3

'''

# Task asking for writing a csv file. I'll try write it to a csv file through python

import csv

with open('4_1_1_4-csv.csv', 'w') as file:
  file.write('name,cake_flavor,frosting_flavor,topping\n')
  file.write('Chocolate Cake,chocolate,chocolate,chocolate shavings\n')
  file.write('Birthday Cake, vanilla,vanilla,rainbow sprinkles\n')
  file.write('Carrot Cake,carrot,cream cheese,almonds')
  file.close()