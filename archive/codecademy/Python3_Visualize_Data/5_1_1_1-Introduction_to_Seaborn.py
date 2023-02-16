# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 1. Introduction to Seaborn

'''
Introduction to Seaborn

In this lesson, you'll learn how to use Seaborn to create bar charts for statistical 
analysis.

Seaborn is a Python data visualization library that provides simple code to create 
elegant visualizations for statistical exploration and insight. Seaborn is based on 
Matplotlib in several ways:

- Seaborn provides a more visually appealing plotting style and concise syntax.

- Seaborn natively understands Pandas DataFrames, making it easier to plot data
  directly from CSVs.

- Seaborn can easily summerize Pandas DataFrames with many rows of data into aggregated
  charts.


If you're unfamiliar with Pandas, just know that Pandas is a data analysis library for
Python that provides easy-to-use data structures and allows you to organize and 
manipulate datasets so they can be visualized. To fully leverage the power of Seaborn,
it is best to prepare your data using Pandas.

Over the next few exercises, we will explain how Seaborn relates to Pandas and how we can
transform massive datasets into easily understandable graphics.
'''

import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('survey.csv')
sns.barplot(x='Age Range', y='Response', hue='Gender', data=df)
plt.show()