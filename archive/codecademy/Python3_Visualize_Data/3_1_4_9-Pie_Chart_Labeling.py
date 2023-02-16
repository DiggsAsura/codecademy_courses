# 3. Graphing in Python
# 1. Graphing in Python: Matplotlib
# 4. Different Plot Types
# 9. Pie Chart Labeling

'''
We also want to be able to understand what each slice of the pie represents. To
do this, we can either:

1. use a legend to label each color
2. put labels on the chart itself


Method 1

budget_data = [500, 1000, 750, 300, 100]
budget_categories = ['marketing', 'payroll', 'engineering', 'design', 'misc']

plt.pie(budget_data)
plt.legend(budget_categories)

Puts up a legend box


Method 2

plt.pie(budget_data, labels=budget_categories)

This puts the category names into labels next to each corresponding slice.


One other useful labeling tool for pie charts is adding the percentage of the
total that each slice occupies. Matplotlib can add this automatically with the 
keyword autopct. We pass in string formatting instructions to format the labels
how we want. Some common formats are:

- '%0.2f' - 2 decimal places, like 4.08

- '%0.2f%%' - 2 decimal places, but with a percent sign at the end, like 4.08%.
  You need to consecutive percent signs because the first one acts as an escape
  character, so that the second one gets displayed on the chart.

- '%d%%' - rounded to the nearest int and with a percentage sign at the end,
  like 4%

So, a full call to plt.pie might look like:


plt.pie(budget_data, labels=budget_categories, autopct='%0.1f%%')

'''

# Ok gotta admit, the '%.1f%' was the most handy here! I mean, it was a bit aha!
# Does this replace .rjust? 

from matplotlib import pyplot as plt

payment_method_names = ['Card Swipe', 'Cash', 'Apple Pay', 'Other']
payment_method_freqs = [270, 77, 32, 11]

plt.pie(payment_method_freqs, autopct='%.1f%%')
plt.legend(payment_method_names)
plt.axis('equal')


plt.show()