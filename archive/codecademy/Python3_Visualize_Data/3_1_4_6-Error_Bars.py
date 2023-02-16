# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 6. Error Bars

'''
In the previous exercise, you learned to represent data as bars of different
heights. Sometimes, we need to visually communicate some sort of uncertainty
in the heights of those bars. Here are some examples:

- The average number of students in a 3rd grade classroom is 30, but some
  classes have as few as 18 and others have as many as 35 students.

- We measured that the weight of a certain fruit was 35g, but we know that our
  scale isn't very precise, so the true weight of the fruit might be as much
  as 40g or as little as 30g.

- The average price of a soda is $1.00, but we also want to communicate that the
  standard deviation is $0.20.

To display error visually in a bar chart, we often use error bars to show where
each bar could be, taking errors into account.

Each of the black lines is called an error bar. The taller the bar is, the more
uncertain we are about the height of the blue bar. The horizontal lines at the
top and bottom are called caps. They make it easier to read the error bars.

If we wanted to show an error of +/- 2, we would add the keyword yerr=2 to our
plt.bar() command. To make the caps wide and easy to read, we would add the
keyword capsize=10:


values = [10, 13, 11, 15, 20]
yerr = 2
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()


If we want a different amount of error for each bar, we can make yerr equal to
a list rather than a single number:


values = [10, 13, 11, 15, 20]
yerr = [1, 3, 0.5, 2, 4]
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()


This code result in error bars of different sizes.

Like the list of x-axis labels, Matplotlib reads this in the same order as the
list of y-values. So, the first index of your error list should correspond to the
first index of your y-values list, the second of your error list should correspond
to the second index of your y-values list, and so on.

'''

from matplotlib import pyplot as plt

drinks = ['cappuccino', 'latte', 'chai', 'americano', 'mocha', 'espresso']
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

plt.bar(range(len(drinks)), ounces_of_milk, yerr=error, capsize=5)


plt.show()
