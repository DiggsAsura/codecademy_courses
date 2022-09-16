# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 7. Violin Plots, Part I

'''
As we saw in the previous exercises, while it's possible to plot multiple histograms,
it is not a great option for comparing distributions. Seaborn gives us another option 
for comparing distributions - a violin plot. Violoin plots provide more information
than box plots because instead of mapping each individual data point, we get an 
estimation of the dataset thanks to the KDE.

Violin plots are less familiar and trickier to read, so let's break down the 
different parts:

- There are two KDE plots that are symmetrical along the center line.

- A white dot represents the median.

- The thick black line in the center of each violin represents the interquartile range.

- The lines that extend from the center are the confidence intervals - just as we
  saw on the bar plots, a violin plot also displays the 95% confidence interval.
  

Examine the violoin plot. Notice how it also is able to show distributions, like the KDE
plot, as well as information about the median and interquartilie range, like the 
box plots.
'''

# See 5_1_2_7-viol.....svg

