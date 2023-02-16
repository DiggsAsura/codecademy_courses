# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 3. Basic Line Plot II

'''
We can also have multiple line plots displayed on the same set of axes. This can
be very useful if we want to compare two datasets with the same scale and axis 
categories. 

Matplotlib will automatically place the two lines on the same axes and give them
different colors if you call plt.plot() twice.

Let's look at the graph we made in the last exercise to track lunch spending,
where days is on the x-axis and spending on the y-axis:

<fig>

We could add a friend's lunch spending for comparison like this:


days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]
# friends monney spent
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]

plt.plot(days, money_spent)
plt.plot(days, money_spent_2)
plt.show()


We then get two lines on the same plot.

By default, the first line is always blue, and the second line is always orange.
In the next exercise, we'll learn how to customize these lines ourselves.

'''

from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

# if asked revenue vs time, time is always first in the plot
# costs vs time, time first

plt.plot(time, revenue)
plt.plot(time, costs)
plt.show()