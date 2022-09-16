# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 1. Introduction

'''
In this lesson, we will explore how to use Seaborn to graph multiple statistical
distributions, including box plots and violin plots.

Seaborn is optimized to work with large datasets - from its ability to natively
interact with Pandas DataFrames, to automatically calculating and plotting aggregates.
One of the most powerful aspects of Seaborn is its ability to visualize and compare 
distrubutions. Distrubutions provide us with more information about our data - how
spread out it is, its range, etc.

Calculating and graphing distrubutions is integral to analyzing amssive amounts of
data. We'll look at how Seaborn allows us to move beyond the traditional distribution
graphs to plots that enable us to communicate important statistical information.
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

n = 500
dataset1 = np.genfromtxt('dataset1.csv', delimiter=',')
dataset2 = np.genfromtxt('dataset2.csv', delimiter=',')
dataset3 = np.genfromtxt('dataset3.csv', delimiter=',')

df = pd.DataFrame({
  'label': ['set_one'] * n + ['set_two'] * n + ['set_three'] * n,
  'value': np.concatenate([dataset1, dataset2, dataset3])
})

sns.set()

sns.barplot(data=df, x='label', y='value')
plt.show()

sns.kdeplot(dataset1, shade=True, label='dataset1')
sns.kdeplot(dataset2, shade=True, label='dataset2')
sns.kdeplot(dataset3, shade=True, label='dataset3')

plt.legend()
plt.show()

sns.boxplot(data=df, x='label', y='value')
plt.show()

sns.violinplot(data=df, x='label', y='value')
plt.show()
