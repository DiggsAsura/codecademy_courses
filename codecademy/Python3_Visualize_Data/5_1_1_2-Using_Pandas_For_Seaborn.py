# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 2. Using Pandas for Seaborn

'''
Throughout this lesson, you'll use Seaborn to visualize a Pandas DataFrame.

DataFrames contain data structured into rows and columns. DataFrames look similar to
other data tables you may be familiar with, but they are designed specifically to be used 
with Python.

You can create a DataFrame from a local CSV file (CSV files store data in a tabular
format).

To create a DataFrame from a local CSV file you would use the syntax:


df = pd.read_csv('file_name.csv')


The code aboce creates a DataFrame saved to a variable named df. The data inside of the df
DataFrame comes from the data in the local CSV file named file_name.csv.

Once you have prepared and organized a Pandas DataFrame with your chosen dataset, you are
ready to plot with Seaborn!


'''

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


df = pd.read_csv('survey.csv')
print(df.head())
