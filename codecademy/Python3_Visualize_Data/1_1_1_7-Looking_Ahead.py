# 1. Introduction to Python
# 1. Introduction to Data Visualization
# 1. Why Data Vizualization
# 7. Looking Ahead

'''
Congratulations on completing your first lesson! You've gotten your hands dirty
by running some code and learning about the three steps of the data visualization
process. Before you know it, you'll be in the business of visualizing and interpreting
data.

As we look ahead, let's remember the three steps of the data visualization process:

- Formatting: Some files we will be using to store our data include CSVs, 
  Python Lists, and Data frames. We will be prepping our data so that we can use
  it with the Python libraries in this Intensive

- Visualizing: The two libraries we will be leveraging to map, plot, graph, 
  and chart our data are Matplotlib and Seaborn

- Styling: We will be learning how to design, copy, and color play to effectively
  communicate information
  
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