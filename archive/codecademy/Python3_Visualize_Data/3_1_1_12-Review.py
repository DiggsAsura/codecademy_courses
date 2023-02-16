# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 12. Review

'''
Now you've played around with several two-dimensional line plots in Matplotlib.
You've seen how you can create simple, readable plots with few commands. You've
also learned some commands to style and label your plots better. These are the
concepts you've seen in Matplotlib so far:

- Creating a line graph from data

- Changing the appearance of the line

- Zooming in on different parts of the axis

- Putting labels on titles and axes

- Creating a more complex figure layout

- Adding legends to graphs

- Changing tick labels and positions

- Saving what you've made

Moving on, we'll learn how to make different kinds of plots (beyon line graphts!)
in Matplotlib and how to choose between those plots when displaying data.

Let's do a final round of practice with all the cool plotting concepts you've
learned so far!
'''

from matplotlib import pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
y1 = [0.4, 0.2, 0.7, 0.2, 0.9, 0.1, 0.5, 0.2, 0.1, 1.2, 1.3]
y2 = [7, 12, 17, 21, 23, 30, 32, 41, 64, 100, 57]

plt.plot(x, y1, color='purple', marker='*')
plt.plot(x, y2, color='green', marker='*')

plt.title('Two Lines on One Graph')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')

plt.legend(['Label 1, Label 2'], loc=4)

plt.show()