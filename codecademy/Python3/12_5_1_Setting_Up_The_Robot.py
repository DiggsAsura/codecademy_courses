# Chapter 12 - Python Code Challenges II
# 5. Classes
# 1. Setting Up Our Robot

# Let's begin by creating the class for our robot. We will begin by setting
# up the instance variables to keep track of important data related to 
# the robot. Here are the steps we need to do:
#
# 1. Create a new class called DriveBot
# 2. Set up a basic constructor (no parameters needed)
# 3. Initialize three instance variable within our constructor which all 
#    default to 0: motor_speed, direction, and sensor_range
#
# Create a python class called DriveBot. Within this class, create instance
# variables for motor_speed, sensor_range and direction. All of these should
# be initialized to 0 by default. After setting up the class, create an object
# from the class called robot_1. Set the motor_speed to 5, the direction 
# to 90 and the sensor_range to 10. Use the provided print
# statements to check your work!

class DriveBot:
  def __init__(self):
    self.motor_speed = 0
    self.sensor_range = 0
    self.direction = 0
    
robot_1 = DriveBot() # the Object
robot_1.direction = 90
robot_1.motor_speed = 5
robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

# Got the class correct, got a bit confused about the object. Turned out to be
# super easy, here it's me not just getting the task at hand correctly. 

# This shows the structure of a simple class which only contains instance 
# variables. The three instance variables are set to 0 for now, which means
# they can only be changed manually by accessing them from an object of the
# DriveBot class. 
