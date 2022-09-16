# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 1. Line Graphts in Matplotlib
# 10. Modify Ticks

'''
In all our previous exercises, our commands have started with plt. In order
to modify tick marks, we'll have to try something a little bit different.

Because our plots can have multiple subplots, we have to specify which one
we want to modify. In order to do that, we can call plt.subplot() in a 
different way.


ax = plt.subplot(1, 1, 1)


ax is an axes object, and it let us modify the axes belonging to specific subplot.
Even if we only have one subplot, when we want to modify the ticks, we'll need
to start by calling either ax = plt.subplot(1, 1, 1) or ax = plt.subplot()
in orther to get our axes object.

Suppose we wanted to set our x-ticks to be at 1, 2 and 4. We would use the 
following code:

ax = plt.subplot()
plt.plot([0, 1, 2, 3, 4], [0, 1, 4, 9, 16])
plt.plot([0, 1, 2, 3, 4], [0, 1, 8, 27, 64])
ax.set_xticks([1, 2, 4])

We can also modify the y-ticks by using ax.set_yticks().

When we change the x-ticks, their labels automatically change to match. But, if
we want special labels (such as strings), we can use the command ax.set_xticklabels()
or ax.set_yticklabels(). For example, we might want to have a y-axis with ticks
at 0.1, 0.6, and 0.8, but label them 10%, 60% and 80% respectively. To do this,
we use the following commands:


ax = plt.subplot()
plt.plot([1, 3, 3.5], [0.1, 0.6, 0.8], 'o')
ax.set_yticks([0.1, 0.6, 0.8])
ax.set_yticklabels(['10%', '60%', '80%'])

'''

from matplotlib import pyplot as plt

month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel('Months')
plt.ylabel('Conversion')
plt.plot(months, conversion)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(['10%', '25%', '50%', '75%'])

plt.show()