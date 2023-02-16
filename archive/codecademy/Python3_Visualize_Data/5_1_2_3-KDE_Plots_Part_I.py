# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 2. Learn Seaborn: Distrubutions
# 3. KDE Plots, Part I

'''
Bar plots can tell us what the mean of our dataset is, but they don't give us any hints
as to the distribution of the dataset values. For all we know, the data could be clustered
around the mean or spread out evenly across the entire range.

To find out more about each of these datasets, we'll need to examine their distributions.
A common way of doing so is by plotting the data as a histogram, but histograms have their
drawback as well.

Seaborn offers another option for graphing distributions: KDE Plots.

KDE stands for Kernel Density Esimator. A KDE plot gives us the sense of a univariate
as a curve. A univariate dataset only has one variable and is also referred to as 
bing one-dimensional, as opposed to bivariate or two-dimensional datasets which have two 
variables.

KDE plots are preferable to histograms because depending on how you group the data into
bins and the width of the bins, you can draw widly different conclusion about the shape
of the data. Using a KDE plot can mitigate these issues, because they smooth the
datasets, allow us to generalize over the shape of our data, and aren't beholden to
specific data points. 

Examine the KDE plot to the right. Notice how it shows the distribution of a dataset
and has a smoother shape than a histogram.
'''

# see 5_1_2_3-fig.svg