# 1. Introduction to Python
# 1. Introduction to Data Visualization
# 1. Why Data Vizualization
# 6. Data Responsibility

'''
Great job! Before we wrap up this lesson, let's briefly pause to think about data
responsibility.

In the data analytics industry, it's easy to default to the question:

"What do the numbers tell us?"

In this path, we urge to instead ask:

"How do we interpret the numbers?"

This approach assumes responsibility in data interpreation. When crafting a data
visualization, it's important to be aware of all the assumptations that went
into generating the data.

For example, in the 1950s, when a team was designing car airbags, they exclusively
tested their prototype using a male mannequin. Consequently, the data they 
collected about how the airbags performed was biased to an adult male. The
result was that the original airbag fatally malfunctioned when used with woman
and children. 

This is an example of poor data collection and interpretation. Assumptations present
in data collection and their resulting datasets often go overlooked and lead to 
poor decision making.

Another common misconception in data interpretation is thinking correlation implies
causation. Correlation measure the relationship or connection between two or more
variables, and causation implies one led to the other. You may plot two variables
that show a strong correlation, but one variable does not necessarily cause the
other to happen.
'''

'''
To illustrate that correlation is not causation we have graphed two un-related
datasets against each other. From the year 1999 to 2009, we graphed the number
of letters in a winning word at the Spelling Bee. The second dataset charts the
deaths by a venomous spider bite in the US. There is a clear correlation between 
the two datasets, each follows a similar pattern. However, one does not cause the
other to happen.

Data interpretation requires responsibility. Keep these examples in mind, and 
avoid jumping to any data conclusions. 
'''

from matplotlib import pyplot as plt

deaths_venomous_spider = [6, 5, 5, 10, 8, 14, 10, 4, 8, 5, 6]
letters_spelling_bee = [9, 8, 11, 12, 11, 13, 12, 9, 9, 7, 9]

years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.xlabel("Year")
plt.ylabel("Total Count")

plt.plot(years, letters_spelling_bee)
plt.plot(years, deaths_venomous_spider)
plt.title("Letters in the Winning Spelling Bee Word vs Deaths by Venomous Spider")
legend_labels = ["Letters in Winning Word", "Deaths by Venomous Spider"]
plt.legend(legend_labels, loc=8)
plt.show()