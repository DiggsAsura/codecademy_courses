# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 7. Subplots

'''
Sometimes, we want to display two lines side-by-side, rather than in the same
set of x- and y- axes. When we have multiple axes in the same picture, we call
each set of axes a subplot. The picture or object that contains all of the
subplots is called a figure.

We can have many different subplots in the same figure, and we can lay them out
in many different ways. We can think of our layouts as having rows and columns of
subplots. For instance, the following figure has six subplots split into 2 rows
and 3 columns:

<3_1_1_7-Subplots.png>

We can create subplots using .subplot().

The command plt.subplot() needs three arguments to be passed into it:

- The number of rows of subplots
- The number of columns of subplots
- The index of the subplot we want to create

For instance, the command plt.subplot(2, 3, 4) would create "Subplot 4" from 
the figure above. 

Any plt.plot() that comes after plt.subplot() will create a line plot in the 
specified subplot. For instance:


# Data sets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='green')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
plt.title('Second Subplot')

# Display both subplots
plt.show()

This would result in a figure with the two plats arranged.
'''

from matplotlib import pyplot as plt

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 2, 1)
plt.plot(months, temperature)

plt.subplot(1, 2, 2)
plt.plot(temperature, flights_to_hawaii)

plt.show()