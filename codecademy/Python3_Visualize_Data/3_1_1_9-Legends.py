# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 9. Legends

'''
When we have multiple lines on a single graph we can label them by using the
command plt.legend().

The legend method takes a list with the labels to display. So, for example,
we can call:


plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
plt.legend(['parabola', 'cubic'])
plt.show()

which would display a legend on our graph, labeling each line.

plt.legend() can also take a keyword argument loc, which will position the
legend on the figure.

These are the position values loc accepts:

Number Code  String
0            best
1            upper right
2            upper left
3            lower left
4            lower right
5            right
6            center left
7            center right
8            lower center
9            upper center
10           center


Note: if you decide not to set a value for loc, it will default to choosing
the "best" location.

For example, we can call plt.legend() and set loc to 6:


plt.legend(['parabola', 'cubic'], loc=6)
plt.show()


which would move the legend to the left side of the graph.

Sometimes, it's easier to label each line as we create it. If we want, we can
use the keyword label inside of plt.plot(). If we choose to do this, we don't 
pass any labels into plt.legend(). For example:


plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16], label="parabola")
plt.plot([0, 2, 3, 4, 5], [0, 1, 8, 27, 64], label="cubic")
plt.legend() # Still need this command!
plt.show()

This will display a legend that looks just like what we had before. 


'''

from matplotlib import pyplot as plt

months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']
plt.legend(legend_labels, loc=8)

plt.show()
