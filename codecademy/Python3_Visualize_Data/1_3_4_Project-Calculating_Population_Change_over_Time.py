# 1. Introduction to Python
# 3. Python Functions
# 4. Project
# Calculating Population Change Over Time

'''
You work at the UN in urban planning and are interested in tracking population
growth across major metropolitan regions. You are hoping that by looking at
historical population numbers that you can predict future growth and help your
team make decisions about resourcing.

Use what you've learned about the basicas of Python to calculate the population
growth of Istanbul and pring out a short report.

'''

city_name = 'Istanbul, Turkey'
pop_1927 = 691000
pop_2017 = 15029231
pop_change = pop_2017 - pop_1927
percentage_gr = ((pop_2017 - pop_1927) / pop_1927) * 100
annual_gr = percentage_gr / (2017-1927)

def population_growth(year_one, year_two, population_one, population_two):
  pop_change = population_two - population_one
  percentage_gr = (pop_change / population_one) * 100
  growth_rate = percentage_gr / (year_two - year_one)
  return growth_rate

print(annual_gr)

set_one = population_growth(1927, 2017, pop_1927, pop_2017)
print(set_one)

set_two = population_growth(1950, 2000, 983000, 8831800)
print(set_two)

report = f'From the year 1927 ({pop_1927}) to 2017 ({pop_2017}), {city_name} had an astonoshing growth rate of {int(set_one)}%. Also from 1950 to 200 it had {int(set_two)}% growth rate alone.'

print(report)