# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 7. Calculating Different Aggregates

'''
In most cases, we'll want to plot the mean of our data, but sometimes, we'll want 
something different:

- If our data has many outliers, we may want to plot the median

- If our data is categorical, we might want to count how many times each category 
  (such as in the case of survey responses).

Seaborn is flexible and can calculate any aggregate you want. To do so, you'll need to 
to use the keyword argumnet estimator, which accepts any function that works on a 
list. 

For example, to calculate the median, you can pass in np.median to the estimator
keyword:


sns.barplot(data=df, x='x-values', y='y-values', estimator=np.median)


Consider the data in results.csv. To calculate the number of times a particular number
of times a particular value appears in the Response column, we pass in len:


sns.barplot(data=df, x='Patient ID', y='Response', estimator=len)

'''

import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('5_1_1_7-survey.csv')
print(df)

sns.barplot(data=df, x='Gender', y='Response', estimator=len)
#sns.barplot(data=df, x='Gender', y='Response', estimator=np.median)
plt.show()
