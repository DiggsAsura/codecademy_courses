# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 9. Review

'''
In this lesson you learned how to extend Matplotlib with Seaborn to create meaningful
visualizations from data in DataFrames.

You've also learned how Seaborn creates aggregated charts and how to change the way
aggregates and error bars are calculated.

Finally, you leanred how to agregate by multiple columns, and how the hue parameter 
adds a nested categorical variable to a visualization.



To review the seaborn workflow:

1. Ingest data from a CSV file to Pandas DataFrame
df = pd.read_csv('file_name.csv')

2. Set sns.barplot8) with desired values for x, y, and set data to equal your df
sns.barplot(data=df, x='X-Values', y='Y-Values')

3. Set desired values for estimator and hue parameters.
sns.barplot(data=df, x='X-Values', y='Y-Values', estimator=len, hue='Value')

4. Render the plot using plt.show()
plt.show() 

'''

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = pd.read_csv('5_1_1_9-survey.csv')

sns.barplot(data=df, x='Gender', y='Patient ID', hue='Age Range')

plt.show()