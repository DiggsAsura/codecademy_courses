# Chapter 12 - Python Code Challenges II
# 5. Classes
# 5. Identifying Robots

# In order to keep track of the robots we are creating, we want to be able to 
# assign an ID value to each robot when it is created. If we create five
# robots in a row, we want the IDs of each robot to be 1, 2, 3, 4 and 5
# respectively. This can be accomplished by using a class variable counter
# which increments and is assigned to an instance variable for the ID
# whenever the constructor is called. Here are the steps:
# 
# 1. Create a new class variable in the DriveBot class called robot_count
# 2. In the constructor, increment the robot_count by 1
# 3. After incrementing the value, assign the value of robot_count to a new
#    instance variable called id
#
# Within the DriveBot class, create an instance variable called id which 
# will be assigned to the robot when the object is created. Every time a 
# robot is created, increment a counter (stored as a class variable) so 
# that the next robot will have a different id. For example, if three
# robots were created: first_robot, next_robot, last_robot; first_robot 
# will have an id of 1, next_robot will have an id of 2 and last_robot will
# have an id of 3.

class DriveBot:
  robot_count = 0
  
  all_disabled = False
  latitude = -999999
  longitude = -999999
  
  def __init__(self, motor_speed=0, direction=180, sensor_range=10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range
    DriveBot.robot_count += 1
    self.id = DriveBot.robot_count
    

  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction
    
  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range

robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robot_3 = DriveBot(20, 60, 10)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)


# Ok this one I haven't seen, or at least can not remember it. It does
# make sense, but make it stick man! Make it STICK!
# self.id = DriveBot.robot_count - remember. remember.

# ..forgotten. Fuck.

# The final modifications to this class can be seen at the top of the class
# and in the constructior. We can use a class variable to keep track of the 
# total number of robots. This information is shared across all robots objects
# we create from the class. Every time a robot object is created, the 
# constructor is called and the count is incremented. Each robot has
# an instance variable for id which is local to that robot object. This 
# is assigned at the time of construction and stores what the count
# was at that time. 