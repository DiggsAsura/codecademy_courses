# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 2. Simple Bar Chart

'''
The plt.bar function allows you to create simple bar charts to compare multiple
categories of data.

Some possible data that would be displayed with a bar chart:

- x-axis: famous buildings, y-axis: heights

- x-axis: different planets, y-axis: number of days in the year

- x-axis: programming languages, y-axis: lines of code written by you

You call plt.bar with two arguments:

- the x-values: a list of x-positions for each bar

- the y-values - a list of heights for each bar

In most cases, we will want our x-values to be a list that looks like
[0, 1, 2, 3, ...] and has the same number of elements as our y-values list.
We can create that list manually, but we can also use the following code:


heights = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
x_values = range(len(heights))


The range function creates a list of consecutive integers (i.e., [0, 1, 2, 3...]).
It needs an argument to tell it how many numbers should be in the list. For 
instance, range(5) would make a list with 5 numbers. We want our list to be as 
long as our bar heights (heights in this example). len(heights) tell us how 
many elements are in the list heights.

Here is an example of how to make a bar chart using plt.bar to compare the 
number of days in a year on the different planets:


days_in_year = [88, 225, 365, 687, 4333, 10756, 30687, 60190, 90553]
plt.bar(range(len(days_in_year)), days_in_year)
plt.show()


At this point, it's hard to tell what this represents, because it's unclearly
labeled. We'll fix that in later sections!

In the instructions below, we'll use plt.bar to create a chart for a fake
cafe called MatplotSip. We will be comparing the sales of different beverages
on a given day.
'''

from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)
plt.show()