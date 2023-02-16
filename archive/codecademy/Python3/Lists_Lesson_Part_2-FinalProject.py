# Task 1 - Create a list with pizzas
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#print(toppings)

# Task 2 - Create a list of prices (integers)
prices = [2, 6, 1, 3, 2, 7, 2]
#print(prices)

# Task 3 - Count how many 2's
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

# Task 4 - Lenght of toppings
num_pizzas = len(toppings)
#print(num_pizzas)

# Task 5 - Print a string with num pizzas
print("We sell", num_pizzas, "different kinds of pizza!")

# Task 6 - Make a two dimensional list of toppings and prices manually
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# Task 7 - Print the new two dimensional list
print(pizza_and_prices)

# Task 8 - Sort the two dimensional list
pizza_and_prices.sort()
#print(pizza_and_prices)

# Task 9 - Store the cheapest pizza in a new variable
cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

# Task 10 - Same for priciest pizza
priciest_pizza = pizza_and_prices[-1]
#print(priciest_pizza)

# Task 11 - Remove the last item
pizza_and_prices.pop()

# Task 12 - Insert a new pizza to the list, in the correct place
pizza_and_prices.insert(-2, [2.5, "peppers"])
#print(pizza_and_prices)

# Task 13 - Slice 3 cheapest (0:3 because UP TO three, but not included)
three_cheapest = pizza_and_prices[0:3]

# Task 14 - Print 3 cheapest...
print(three_cheapest)


