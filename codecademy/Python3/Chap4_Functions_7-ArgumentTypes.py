# Write your code below:

# Three types of arguments
# Positional arguments: called by their position in the function
# Keyword arguments: called by their name
# Default arguments: arguments that are given a default value

# Positional we already used in the previous lesson
# def calculate_taxi_price(miles_to_travel, rate, discount):

# Keyword argument
# calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)

# Default argument
# def calculate_taxi_price(miles_to_travel, rate, discount = 10)

# Can overwrite default argument
# Using the default value of 10 for discount.
#calculate_taxi_price(10, 0.5)
 
# Overwriting the default value of 10 with 20
#calculate_taxi_price(10, 0.5, 20)


def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in", first_destination, ", then", second_destination, ", and lastly", final_destination)

trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")

trip_planner("Brooklyn", "Queens")
