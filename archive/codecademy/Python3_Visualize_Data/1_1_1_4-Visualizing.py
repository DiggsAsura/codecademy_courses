# 1. Introduction to Python
# 1. Introduction to Data Visualization
# 1. Why Data Vizualization
# 4. Visualizing

'''
The second step in the process is visualizing data. We will learn how to select
different types of charts and graphs to convey specific relationships in the
data. There is an entire research field dedicated to graph literacy, or the 
readability of information in a visualization. We will be teaching you the 
basics.

To visualize our data, we will be using two of the most popular Data Visualization
libraries in Python. Libraries are reusable code someone wrote and published for
others to use. In this path, the two libraries we will use allow you to code 
several chart and graph types:

- Matplotlib is the most well-known Python module for plotting data.

- Seaborn is buil on Matplotlib and leverages statistics in visualizations.

'''

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style('whitegrid')
flights = sns.load_dataset('flights')
ax = sns.barplot(x='month', y='passengers', data=flights)
plt.xticks(rotation='vertical')

plt.show()