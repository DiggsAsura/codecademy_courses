# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 6. Box Plots, Part II

'''
One advantage of the box plot over the KDE plot is that in Seaborn, it is easy to plot
multiples and compare distributions.

Let's look again at our three datasets, and how they look plotted as box plots:


sns.boxplot(data=df, x='label', y='value')
plt.show()


The box plot does a good job of showing certain differences, like those between Dataset 1
and Dataset 2; however it does not show that dataset 3 is bimodal.

To plot a box plot in Seaborn, we use the method sns.boxplot().

A box plot takes the following arguments:

- data - the dataset we're plotting, like a DataFrame, list or array
- x - a one-dimensional set of values, like a Series, list or array
- y - a second set of one-dimensional data

If you use Pandas Series for the x and y values, the Series will also generate the axis
labels. For example, if you use the value Series as your y value data, Seaborn will 
automatically apply that name as the y-axis label.

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
n = 500
df = pd.DataFrame({
  'label': ['set_one'] * n + ['set_two'] * n + ['set_three'] * n + ['set_four'] * n,
  'value': np.concatenate([set_one, set_two, set_three, set_four])  
})

# Setting styles
sns.set_style('darkgrid')
sns.set_palette('pastel')


# Add your code:
sns.boxplot(data=df, x='label', y='value')
plt.show()