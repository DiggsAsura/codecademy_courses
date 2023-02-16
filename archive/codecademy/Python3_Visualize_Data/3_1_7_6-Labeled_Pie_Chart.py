# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 7. Recreate Graphs using Matplotlib
# 6. Labeled Pie Chart

'''
Now, we are going to look at the chart called pie.png. This displays what 
students think the hardest topic covered throughout your match course is.

The data you will need to recreate this chart is the list unit_topics and 
num_hardest_reported.

Save your recreated chart to a file called my_pie_chart.png
'''

from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]


plt.figure(figsize=(10, 8))
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%1d%%')
plt.axis('equal')
plt.title('Hardest Topics')

plt.savefig('3_1_7_6-my_pie_chart.png')

plt.show()