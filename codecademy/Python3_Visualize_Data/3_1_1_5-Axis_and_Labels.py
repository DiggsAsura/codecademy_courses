# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 5. Axis and Labels

'''
Sometimes, it can be helpful to zoom in or out of the plot, especially if there 
is some detail we want to address. To zom, we can use plt.axis(). We use
plt.axis() by feeding it a list as input. The list should contain:

1. The minimum x-value displayed
2. The maximum x-value displayed
3. The minumum y-value displayed
4. The maximum y-value-displayed

For example, if we want to display a plot from x=0 to x=3 and from y=2 to y=5,
we would call plt.axis([0, 3, 2, 5])

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]
plt.plot(x, y)
plt.axis([0, 3, 2, 5])
plt.show()

'''

from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]
plt.plot(x, y)

#your code here
plt.axis([0, 12, 2850, 3150])

plt.show()

