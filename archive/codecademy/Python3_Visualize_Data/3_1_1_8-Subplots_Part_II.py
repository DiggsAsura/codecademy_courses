# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 8. Subplots Part II

'''
Sometimes, when we're putting multiple subplots together, some elements can
overlap and make the figure unreadable.

We can customize the spacing between our subplots to make sure that the figure 
we create is visible and easy to understand. To do this, we use the 
plt.subplots_adjust() command. .subplots_adjust() has some keyword arguments
that can move your plots within the figure:

- left - the left-side margin, with a default of 0.125. You can increase this
  number to make room for a y-axis label

- right - the right-side margin, with a default of 0.9. You can increase this 
  to make more room for the figure, or decrease it to make room for a legend.

- bottom - the bottom margin, with a default of 0.1. You can increase this to
  make room for tick mark labels or an x-axis label

- top - the top margin, with a default of 0.9

- wspace - the horizontal space between adjacent subplots, with a default of 
  0.2

- hspace - the vertical space between adjacent subplots, with a default of 0.2

For example, if we were adding space to the bottom of a graph by changing the
bottom margin of a graph by changing the bottom margin to 0.2 (insead of 0.1 
default), we would use the command:

plt.subplots_adjust(bottom=0.2)

We can also use multiple keyword arguments, if we need to adjust multiple
margins. For instance, we could adjust both the top and the hspace:

plt.subplots_adjust(top=0.95, hspace=0.25)

Let's use wspace to fix the figure above (not included here in this file)


# Left Plot
plt.subplot(1, 2, 1)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Right Plot
plt.subplot(1, 2, 2)
plt.plot([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])

# Subplot Adjust
plt.subplots_adjust(wspace=0.35) # margin between the graphs

'''

from matplotlib import pyplot as plt

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.25)

plt.show()