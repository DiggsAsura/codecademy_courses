# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 7. Fill Between

'''
We've learned to display errors on bar charts using error bars. Let's take a 
look at how we might do this in an aesthetically pleasing way on line graphs.
In Matplotlib, we can use plt.fill_between to shade errors. This function
takes three arguments:

1. x-values - this works just like the x-values of plt.plot

2. lower-bound for y-values - set the bottom of the shared area

3. upper-bound for y-values - set the top of the shared aread

Generally, we use fill_between to create a shaded error region, and then plot 
the actual line over it. We can set the alpha keyword to a value between 0 and
1 in the fill_between call for transparency so that we can see the line 
underneath. Here is an example of how we would display data with an error of 2:


x_values = range(10)
y_values = [10, 12, 13, 13, 15, 19, 20, 22, 23, 29]
y_lower = [8, 10, 11, 11, 13, 17, 18, 20, 21, 27]
y_upper = [12, 14, 15, 15, 17, 21, 22, 24, 25, 31]

plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) # this is the shaded error
plt.plot(x_values, y_values) # this is the line itself
plt.show()


Having to calculate y_lower and y_upper by hand is time-consuming. If we try to
just subtract from y_values, we will get an error.


TypeError: unsupported operand type(s)
for -: 'list' and 'int'


In order to correctly add or subtract from a list, we need to use list
comprehension:


y_lower = [i-2 for i in y_values]


This command looks at each element in y_values and calls the elemtn its currently
looking at i. For each new i, it subtracts 2. These operations create a new
list called y_lower.

If we wanted to add 2 to each element in y_values, we could use this code:


y_upper = [i+2 for i in y_values]
'''

from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

ax = plt.subplot()
plt.plot(months, revenue)
ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_lower = [0.9*i for i in revenue]
y_upper = [1.1*i for i in revenue]
plt.fill_between(months, y_lower, y_upper, alpha=0.2)

plt.show()