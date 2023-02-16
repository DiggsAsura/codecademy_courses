# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 2. Bar Charts Hide Information

'''
Before we dive into these new charts, we need to understand why we'd want to use them.
To best illustrate this idea, we need to revisit bar charts.

We previously learned that Seaborn can quickly aggregate data to plot bar charts using
the mean.

Here is a bar chart that uses three different randomly generated sets of data:


sns.barplot(data=df, x='label', y='value')
plt.show()


These three datasets look identical! As far as we can tell, they each have the same
mean and a similar confidence intervals.

We can get a lot of information from these bar charts, but we can't get everything.
For example, what are the minimum and maximum values of these datasets? How spread
out is this data?

While we may not see this information in our bar chart, these differences might be 
significant and worth understanding better.


'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt('5_1_2_2-dataset1.csv', delimiter=',')
set_two = np.genfromtxt('5_1_2_2-dataset2.csv', delimiter=',')
set_three = np.genfromtxt('5_1_2_2-dataset3.csv', delimiter=',')
set_four = np.genfromtxt('5_1_2_2-dataset4.csv', delimiter=',')

# Creating a Pandas DataFrame
n = 500 # not quite sure what this is used for
df = pd.DataFrame({
  'label': ['set_one'] * n + ['set_two'] * n + ['set_three'] * n + ['set_four'] * n,
  'value': np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style('darkgrid')
sns.set_palette('pastel')

# Add your code below:
sns.barplot(data=df, x='label', y='value')
plt.show()


