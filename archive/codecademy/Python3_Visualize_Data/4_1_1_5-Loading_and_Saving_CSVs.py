# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 5. Loading and Saving CSVs

'''
When you have data in a CSV, you can load it into a DataFrame in Pandas using .read_csv():


pd.read_csv('my_csv-file.csv')


In the example above, the .read_csv() method is called. the CSV file called my_csv-file is
passed in as an argument.

We can also save data to a CSV, using .to_csv().


df.to_csv('new_scv-file.csv')


In the example above, the .to_csv() method is called on df (which represents a DataFrame
object). The name of the CSV file is passed in as an argument (new_csv-file.csv). By default,
this method will save th CSV file in your current directory.
'''

import pandas as pd

df = pd.read_csv('sample.csv')
print(df)