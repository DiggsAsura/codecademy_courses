import matplotlib.pyplot as plt

temps = [-5, 29, 26, -7- 1, 18, 12, 31]
#temps_adj = [15, 49, 46, 13, 21, 38, 32, 51]

# list comprehension
temps_adj = [temp + 20 for temp in temps]
print(temps_adj)

# example two

rainfall_1 = [153, 156, 147, 149, 151]
rainfall_2 = [159, 156, 160, 161, 148]

#x_values_1 = range(5)
#x_values_2 = range(5)

#y_values_1 = rainfall_1
#y_values_2 = rainfall_2

# modified with list comprehension

x_values_1 = [x * 2 for x in range(5)]
x_values_2 = [x + 1 for x in x_values_1]

y_values_1 = [amount - 140 for amount in rainfall_1]
y_values_2 = [amount - 140 for amount in rainfall_2]

plt.bar(x_values_1, y_values_1, 0.8, 0)
plt.bar(x_values_2, y_values_2, 0.8, 0)
plt.show()
