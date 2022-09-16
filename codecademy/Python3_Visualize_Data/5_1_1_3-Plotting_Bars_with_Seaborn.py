# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 3. Plotting Bars with Seaborn

'''
Take a look at the file called results.csv. You'll plot that data soon, but before you
plot it, take a minute to understand the context behind that data, which is based on
hypotethical situation we have created:

Suppose we are analyzing data from a survey: we asked 1000 partients at a hospital how
satisfied they were with their experience. Their reponse was measured on a scale of 1-10,
with 1 being extremly unsatisfied, and 10 being extremly satisfied. We have summarized
that data in a CSV file called resulsts.csv

To plot this data using Matplotlib, you would write the following:

df = pd.read_csv('resulsts.csv')
ax = plt.subplot()
plt.bar(range(len(df)), df['Mean Satisfaction'])
ax.set_xticks(range(len(df)))
ax.set_xticklabels(df.Gender)
plt.xlabel('Gender')
plt.ylabel('Mean Satisfaction')


That's a lot of work for a simple bar chart! Seaborn gives us a much simpler option. With
Seaborn, you can use the sns.barplot() command to do the same thing.

The Seaborn function sns.barplot(), takes at least three keyword arguments:

- data: a Pandas DataFrame that contains the data (in this example, data=df)

- x: a string that tells Seaborn which column in the DataFrame contains other
  x-labels (in this case, x='Gender')

- y: a string that tells Seaborn which column in the DataFrame contains the heights we
  want to plot for each bar (in this case y='Mean Satisfaction')

By default, Seaborn will aggregate and plot the mean of each category. In the 
next exercise you will learn more about aggregation and how Seaborn handles it.

'''

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('5_1_1_3-results.csv')
print(df)

sns.barplot(
  data=df,
  x='Gender',
  y='Mean Satisfaction'
)

plt.show()