# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 8. Aggregating by Multiple Columns

'''
Sometimes we'll want to aggregate our data by multiple columns to visualize nested 
categorial variables.

For example, consider our hostpital survey data. The mean satisfaction seems to depend
on Gender, but it might also depend on another column: Age Range.

We can compare both the Gender and Age Range factors at once by using the keyword
hue.


sns.barplot(data=df,x='Gender',y='Response', hue='Age Range')


We can compare both the Gender and Age Range factors at once by using the keyword 
hue.


sns.barplot(data=df, x='Gender', y='Response', hue='Age Range')


The hue parameter adds a nested categorical variable to the plot.

Visualizing survey results by gender with age range nested*. Notice that we keep
the same x-labels, but we now have different color bars representing each Age Range.
We can compare two bars of the same color to see how patients with the same Age Range,
but different Gender rated the survey.

'''


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('5_1_1_8-survey.csv')

sns.barplot(data=df, x='Age Range', y='Response', hue='Gender')

plt.show()