# Chapter 12 - Python Code Challenges II
# 5. Classes
# 3. Enhanced Constructor

# It can be tedious manually setting the values for each instance variable
# after we have created an object from the DriveBot class. We can enhance our
# constructor to automatically assign the values we provide to the instance
# variables. Instead of taking zero parameters, we are going to make the 
# constructor take three parameters. Here is what we need to do:
# 
# 1. Modify the constructor to take three parameters (in addion to self):
#    one for motor_speed, one for direction, and one for sensor_range
# 2. For the first parameter, make the default value 0
# 3. For the second parameter, make the default value 180
# 4. For the third parameter, make the default 10
# 5. Within the constructor, replace the instance variables with the variables
#    from the input parameters. 
#
# Upgrade the constructor in the DriveBot class in order to accept three 
# optional parameters. The constructor can accept motor_speed (which defaults 
# to 0 if not provided), direction (which defaults to 180 if not provided), 
# and sensor_range (which defaults to 10 if not provided). These parameters
# should replace the associated insteance variables. Test out the 
# upgraded constructor by initializing a new robot called robot_2 with a 
# speed for 35, a direction of 75 and a sensor range at 25.

class DriveBot:
  def __init__(self, motor_speed=0, direction=180, sensor_range=10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range
  
  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction
    
  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_2 = DriveBot(35, 75, 25)
print(robot_2.motor_speed)
print(robot_2.direction)
print(robot_2.sensor_range)


# Got this too without hint! Woop!

# The upgraded constructor includes input parameters as well as default 
# values for those parameters. This means that if no value is provided for 
# those parameters, then the value they are set equal to will be used.
