# Write your code below: 

# Write multiple parameters in a function, using commas
# def my_function(parameter1, parameter2, parameter3)

# When calling the function, we need to provide arguments for 
# all the parameters
# my_function(argument1, argument2, argument3)

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  print("Total cost of the trip:", car_rental_total + hotel_total + plane_ticket_price)

calculate_expenses(200, 100, 100, 5)
