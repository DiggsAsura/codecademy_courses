# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 3. Simple Bar Chart II

'''
When we create a bar chart, we want each bar to be meaningful and correspond to
a category of data. In the drinks chart from the last exercise, we would see that 
sales were different for different drink items, but this wan't very helpful
to us, since we didn't know which bar corresponded to which drink.

In the previous lesson, we learned how to customize the tick marks on the
x-axis in three steps:

1. Create an axes object
   ax = plt.subplot()

2. Set the x-tick positions using a list of numbers
   ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])

3. Set the x-tick labels using a list of strings
   ax.set_xticklabels(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'])

4. If your labels are particulary long, you can use the rotation keyword to 
   rotate your labels by a specified number of degrees:
   ax.set_xticklabels(['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'], rotation=30)

Note: We have to set the x-ticks before we set the x-labels because the default
ticks won't necessarily be one tick per bar, especially if we're plotting a lot of 
bars. If we skip setting the x-ticks before the x-labels, we might end up with 
labels in the wrong place.

Remember from Lesson I that we can label the x-axis (plt.xlabel) and y-axis
(plt.ylabel) as well. Now, our graph is much easier to understand.

Let's add the appropriate labels for the chart you made in the last exercise
for the coffee shop, MatplotSip.

'''

from matplotlib import pyplot as plt

drinks = ['cappuccino', 'latte', 'chai', 'americano', 'mocha', 'espresso']
sales = [91, 76, 56, 66, 52, 27]

plt.bar(range(len(drinks)), sales)

ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)


plt.show()