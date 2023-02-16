# The final review for functions chapter
# TripPlanner V1.0 they call it.. :P 

def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0", name)

trip_planner_welcome("Kenneth")


def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

# Failed again because missed the detail to create a variable - not just call it directly
#estimated_time_rounded(2.5)

estimate = estimated_time_rounded(1000.4)

def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print("Your trip starts off in", origin)
  print("And you are traveling to", destination)
  print("You will be travelling by", mode_of_transport)
  print("It will take approximately", str(estimated_time), "hours")
  #return origin, destination, estimated_time, mode_of_transport

# forgot the whole estimate variable i made, so took abit time here
destination_setup("Kongsberg", "Oslo", estimate)



