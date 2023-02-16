# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 7. Recreate Graphs using Matplotlib
# 2. Bar Chart with Error

'''
First, we are going to look at the chart called bar_chart.png

<3_1_7_2-bar-chart.png>

The data you will need to recreate this chart is in the lists past_years_averages,
years, and error.

Save your recreated chart to a file called my_bar_chart.png

'''

from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]


plt.figure(figsize=(10,8))
plt.bar(range(len(past_years_averages)), past_years_averages, yerr=error, capsize=5)
plt.axis([-0.5, 6.5, 70, 95])
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test average')

plt.savefig('my_bar_chart.png')

plt.show()