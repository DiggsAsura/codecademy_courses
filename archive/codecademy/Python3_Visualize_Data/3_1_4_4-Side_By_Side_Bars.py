# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 4. Side-By-Side Bars

'''
We can use a bar chart to compare two sets of data with the same types of axis
values. To do this, we plot two sets of bars next to each other, so that the values
of each category can be compared. For example, here is a chart with side-byside 
bars for the populations of the United States and China over the age of 65 
(in percentages).

<fig not here>

Some examples of data that side-by-side bars could be useful for include:

- the populations of two countries over time

- prices for different foods at two different resturants

- enrollments in different classes for male and females

In the graph above, there are 7 sets of bars, with 2 bars in each set. Each 
bar has a width of 0.8 (the default width for all bars in Matplotlib).

- If our first blue bar is at x=0, then we want the next blue bar to be at x=2,
  and the next to be at x=4, etc.

- Our first orange bar should be at x=0.8 (so that it is touching the blue bar),
  and the next orange bar should be at x=2.8, etc.

This is a lot of math, but we can make Python do it for us by copying and pasting
this code:


# China Data (blue bars)
n = 1 # This is our first dataset out of 2
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
x_values1 = [t*element + w*n for element in range(d)]


That just generated the first set of x-values. To generate the second set, paste
the code again, but change n to 2, because this is the second dataset:


# US Data (orange bars)
n = 2 # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
x_values2 = [t*element + w*n for element in range(d)]


Let's examine our special code:


[t*element + w*n for element in range(d)]


This is called a list comprehension. It's a special way of generating a list from
a formula. You can learn more about it in this article:
https://www.codecademy.com/article/list-comprehension
For making side-by-side bar graphs, you'll never need to change this line; just
paste it into your code and make sure to define n, t, d, and w correctly.

In the instructions below, we'll experiment with side-by-side bars to compare
different locations of the MatplotSip coffee empire.

'''

from matplotlib import pyplot as plt

drinks = ['cappuccino', 'latte', 'chai', 'americano', 'mocha', 'espresso']
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]

# Blue bar
n = 1 # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)] # this one makes me smile haha
plt.bar(store1_x, sales1)

# Orange bar
n = 2 # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element in range(d)]
plt.bar(store2_x, sales2)

plt.show()