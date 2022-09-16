# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 6. Laveling the Axes

'''
Eventually, we will want to show these plots to other people to convince
them of important trends in our data. When we do that, we'll want to make our 
plots look as professional as possible.

The first step towards a professional-looking plot is adding labels to the
x- and y- axes by using plt.xlabel() and plt.ylabel(). The plot title can
be set by using plt.title().

All of these commands require a string, which is a set of characters in either 
singe (') or double (") quotes. 

For example, if someone has been keeping track of their happiness (on a scale 
out of 10) throughout the day and wants to display this information with
labeled axes, we can use the following commands:


hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
happiness = [9.8, 9.9, 9.2, 8.3, 9.0, 8.7, 9.1, 7.0, 6.4, 6.9, 7.5]

plt.plot(hours, happiness)
plt.xlabel('Time of day')
plt.ylabel('Happiness Rating (out of 10)')
plt.title('My Self-Reported Happiness While Awake')
plt.show()

Dude is only happy at work :P

'''

from matplotlib import pyplot as plt

x = range(12)
y = [3000, 3005, 3010, 2900, 2950, 3050, 3000, 3100, 2980, 2980, 2920, 3010]

plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel('Time')
plt.ylabel('Dollars spent on coffee')
plt.title('My Last Twelve Years of Coffee Drinking')

plt.show()