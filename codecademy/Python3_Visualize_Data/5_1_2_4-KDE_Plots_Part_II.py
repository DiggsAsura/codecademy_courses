# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 4. KDE Plots, Part II

'''
To plot a KDE in Seaborn, we use the method sns.kdeplot().

A KDE plot takes the following arguments:

- data - the univariate dataset being visualized, like a Pandas DataFrame, Python List
  or NumPy array.

- shade - a boolean that determines wheter or not the space underneath the curve is 
  shaded

Let's examine the KDE plots of our three datasets:


sns.kdeplot(dataset1, shade=True)
sns.kdeplot(dataset2, shade=True)
sns.kdeplot(dataset3, shade=True)
plt.legend()
plt.show()


Notice that when using a KDE we need to plot each of the original datasets separately,
rather than using a combined dataframe like we did with the bar plot.

It looks like there are some big differences between the three datasets:

- Dataset 1 is skewed left
- Dataset 2 is normally distrubuted
- Dataset 3 is biomodal (it has two peaks)

So although all three datasets have roughly the same mean, the shapes of the KDE plots
demonstrate the differences in how the values are distributed.

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

# Creating a Pandas DataFrame:
n = 500
df = pd.DataFrame({
  'label': ['set_one'] * n + ['set_two'] * n + ['set_three'] * n + ['set_four'] * n,
  'value': np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles
sns.set_style('darkgrid')
sns.set_palette('pastel')

# Add your code below
sns.kdeplot(set_one, shade=True)
sns.kdeplot(set_two, shade=True)
sns.kdeplot(set_three, shade=True)
sns.kdeplot(set_four, shade=True)

plt.show()


