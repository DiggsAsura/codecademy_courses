# Chapter 12 - Python Code Challenges II
# 5. Classes
# 2. Adding Robot Logic

# Now we want to add some logic to our robot. It would be very useful to be
# able to control our robot, so we are going to create a control_bot 
# method which changes the speed and direction. We are also going to 
# create a method called adjust_sensor. This method is used to change the 
# range of our robot's sensors which are used to detect obstacles. Here
# are the steps:
# 
# 1. Define a function within the DriveBot class which accepts two additional
#    parameters: one for a new speed and one for a new direction
# 2. Replace the instance variables for speed and direction with the input
#    parameters
# 3. Define another function called adjust_sensor which accepts one additional
#    parameter
# 4. Replace the instance variable sensor_range with the input parameter
#
# In the DriveBot class, add a method called control_bot which accepts
# parameters: new_speed and new_direction. These should replace associated
# instance variables. Create another method called adjust_sensor which 
# accepts a parameter called new_sensor_range which replaces the sensor_range
# instance variable. Afterwards, use these methods to rotate the robot
# 180 degress at 10 miles per hour with a sensor range of 20 feet. Use the
# provided print statements to check your code!

class DriveBot:
  def __init__(self):
    self.motor_speed = 0
    self.direction = 0
    self.sensor_range = 0
  
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

# Fuck yea. Finally a code challenge without the need of any hint, or peak 
# at the solution. Cheers, me. lol

# These two methods were added inside of the DriveBot class. They are used
# to replace the instance variables with new values from the input
# parameters. We use self.variable_name to access a certain instance 
# variable within the class.

