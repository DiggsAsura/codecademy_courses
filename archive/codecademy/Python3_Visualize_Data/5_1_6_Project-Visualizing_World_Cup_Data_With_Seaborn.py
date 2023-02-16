# 5. Advanced Graphing in Python
# 1. Advanced Graphing with Seaborn
# 6. Project
# 1. Visualizing World Cup Data with Seaborn 

'''
For this project you will be exploring data from the Fifa World Cup from
1930-2014 to analyze trends and discover insights about the world's game, 
football!

This Fifa World Cup data is from Kaggle. Kaggle is a platform for data science
competitions that hosts many datasets online.

Using Seaborn you will create a series of plots that explore aggregates and
distribution across the goals scored in World Cup games.


A little primer on the Fifa World Cup:
-----

The FIFA World Cup, or simply the World Cup, is an international football competition
where 32 countries qualifie to send teams made up of the best players from that nation
to compete against each other for the World Cup championship.

The World Cup championship has been awarded every four years since the inaugural
tournement in 1930, except in 1942 and 1946 when it was not held because of the
Second World War.

The current format of the tournement involves 32 teams competing for the title at
venues within the host nation over a perioc of one month.


A note on datasets
-----

You may notice some typographical errors in the data as you view it. This is a 
large dataset, and errors are often a part of the process of generating large 
datasets. None of the errors should affect any of the steps of this project.

If you get stuck during this project or would like to see an experienced
developer work through it, click 'Get Unstuck' to see a project walktthrough 
video.

'''


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupData.csv')
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

# Checkpoint 6
sns.set_style('whitegrid')

# Checkpoint 7
sns.set_context('poster', font_scale=0.5)

# Checkpoint 8
f, ax = plt.subplots(figsize=(12,7))

# Checkpoint 9
ax = sns.barplot(data=df, x='Year', y='Total Goals')

# Checkpoint 10
plt.show()


# Checkpoint 11
ax.set_title('Average Number of Goals Scored In World Cup Matches By Year')

# Checkpoint 12
df_goals = pd.read_csv('goals.csv')

# Checkpoint 13
sns.set_context('notebook', font_scale=1.25)

# Checkpoint 14
f, ax2 = plt.subplots(figsize=(12,7))

# Checkpoint 15
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette='Spectral')

# Checkpoint 16
ax2.set_title('Meaningful goal title lol')

# Checkpoint 17
plt.show()

print(df_goals.head())