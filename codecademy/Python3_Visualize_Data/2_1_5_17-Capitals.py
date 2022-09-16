# 2. Python for Data Analysis
# 1. Python Lists
# 5. List Comprehension - Code Challenge
# 17. Capitals

capitals = ['Santiago', 'Paris', 'Copenhagen']
countries = ['Chile', 'France', 'Denmark']

locations = [f'{capital}, {country}' for (capital, country) in zip(capitals, countries)]
print(locations)