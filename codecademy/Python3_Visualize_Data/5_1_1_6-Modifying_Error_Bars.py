# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 1. Learn Seaborn Introduction
# 6. Modifying Error Bars

'''
By default, Seaborn will place error bars on each bar when you use the barplot()
function.

Error bars are the small lines that extend above and below the top of each bar. Errors
bars visually indicate the range of values tha tmight be expected for that bar.


For example, in our assignment average example, an error bar might indicate what grade
we expect an average student to receive on this assignment.


There are several different calculations that are commonly used to determine error
bars.

By default, Seaborn uses something called a bootstarpped confidence interval. Roughly
speaking, this interval means that "based on this data, 95% of similar situations
would have an outcome within this range".

In our gradebook example, the confidence interval for the assignments means "if we gave
this assignment to many, many students, we're confident that the mean score on the
assignment would be within the range represented by the error bar".

The confidence interval is a nice error bar measurement because it is defined for 
different types of aggregate functions, such as medians and mode, in addition to means.

If you're calculating a mean and would prefer to use standard deviation for your error
bars, you can pass in the keyword argument ci='sd' to sns.barplot() which will 
represent one standard deviation. It would look like this:


sns.barplot(data=gradebook, x='name', y='grade', ci='sd')


'''

import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from matplotlib import pyplot as plt
import seaborn as sns

gradebook = pd.read_csv("5_1_1_6-gradebook.csv")

sns.barplot(data=gradebook, x="name", y="grade", ci='sd')
plt.show()