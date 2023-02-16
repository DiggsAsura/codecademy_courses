# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 5. Plotting Aggregates

'''
Recall our gradebook from the previous exercise.

Amy
Amy
Bob
Bo.....
..


Suppose this data is stored in a Pandas DataFrame called df.

The same Seaborn command that you previously learned 8sns.barplot()) will plot this 
data in a bar plot and automatically aggregate the data:


sns.barplot(data=df, x='student', y='grade')


In the example above, Seaborn will aggregate grades by student, and plot the average
grade for each student.
'''

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv('5_1_1_5-gradebook.csv')

sns.barplot(
  data=gradebook,
  x='assignment_name',
  y='grade'
)

plt.show()