# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 9. Review

'''
In this lesson, we examined how Seaborn has several plots that can visualize distributions.
While bar plots can display basic aggregates, KDE plots, dist plots, box plots and violin
plots can show us distributions and other information.

- KDE plot - Kernel density estimator; shows a smoothed version of dataset. Use
  sns.boxplot()

- Box plot - A classical statistical model that shows the median, interquartile range,
  and outliers. Use sns.boxplot().

- Violin plot - A combination of a KDE and a box plot. Good for showing multiple 
  distributions at a time. Use sns.violinplot().


'''

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Take in the data from the CSVs as NumPy arrays:
set_one = np.genfromtxt("5_1_2_2-dataset1.csv", delimiter=",")
set_two = np.genfromtxt("5_1_2_2-dataset2.csv", delimiter=",")
set_three = np.genfromtxt("5_1_2_2-dataset3.csv", delimiter=",")
set_four = np.genfromtxt("5_1_2_2-dataset4.csv", delimiter=",")

# Creating a Pandas DataFrame:
n=500
df = pd.DataFrame({
    "label": ["set_one"] * n + ["set_two"] * n + ["set_three"] * n + ["set_four"] * n,
    "value": np.concatenate([set_one, set_two, set_three, set_four])
})

# Setting styles:
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Add your code below:
sns.violinplot(data=df, x='label', y='value')
plt.show()