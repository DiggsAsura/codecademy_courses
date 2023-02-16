# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 8. Violin Plots, Part II

'''
Violin Plots are a powerful graphing tool that allows you to compare multiple distributions
at once.

Let's look at how our original three data sets look like as violin plots:


sns.violinplot(data=df, x='label', y='value')
plt.show()


As we can see, violin plots allow us to graph and compare multiple distributions. It 
also retains the shape of the distributions, so we can easily tell that Dataset 1
is skewed left and the Dataset 3 is bimodal.

To plot a violin plot in Seaborn, use the method sns.violinplot().

There are several options for passing in relevant data to the x and y parameters:

- data - the dataset that we're plotting, such as a list, DataFrame or array
- x, y and hue - a one-dimensional set of data, such as a Series, lit, or array
- any of the parematers to the function sns.boxplot()

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

# Add your own shit:
sns.violinplot(data=df, x='label', y='value')
plt.show()