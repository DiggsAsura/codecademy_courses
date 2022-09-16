# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 7. Recreate Graphs using Matplotlib
# 4. Stacked Bars

'''
Now, we are going to look at the chart called stacked-bars.png. This graph 
displays the breakdown of students who got As, Bs, Cs, Ds and Fs in each unit.

The data you will need to recreate this chart is in the lists As, Bs, Cs, Ds, Fs
and unit_topics

Save your recreated chart to a file called my_stacked_bar.png
'''

from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

plt.figure(figsize=(10,8))

#ALWAYS remember, needs both X and Y (i forget what to put in lol)
plt.bar(x, As)
plt.bar(x, Bs, bottom=As)
plt.bar(x, Cs, bottom=c_bottom)
plt.bar(x, Ds, bottom=d_bottom)
plt.bar(x, Fs, bottom=f_bottom)

ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title('Grade distribution')
plt.legend(unit_topics)
plt.ylabel('Number of Students')
plt.xlabel('Unit')

plt.savefig('3_1_7_4-my_stacked_bar.png')

plt.show()