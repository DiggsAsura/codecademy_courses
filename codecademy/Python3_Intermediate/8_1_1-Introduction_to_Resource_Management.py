# 8. Resource Management
# 1. Context Managers
# 1. Introduction to Resource Management

print('\nIntroduction to Resource Management\n')

# When we use a computer, we tend to interact with its various resources.
# Similar to how we need to manage resources in our daily lives like our time
# and energy, resources on a computer also need to be managed.
#
# For computers, the resources we manage usually come in the form of memory,
# storage, or power. Since all resources are limited, if they are not managed
# well, it can lead to the computer running out of memory, space, and even 
# causes crashes. So how do we manage these resources? Well, one of the 
# easiest ways (and one we already started to explore) is through the use
# of context managers.
#
# A context manager is an object that takes care of the assigning and releaseing
# of resources (files, database connections, etc). Learning to properly use
# context managers will give our software benefits such as:
#
#   - Preventing resources leaks
#
#   - Preventing crashes
#
#   - Decreasing the vulnerability of our data
#
#   - Preventing program slow-down.
#
# Before we dive into context managers, let's examine what happens when we don't
# manage our resources properly.

# Take a look at the with statement in the code editor! This is an example of a 
# context manager! It should look familiar from when we worked with files
# earlier. If not, it might be a good time to review the module in 
# Learn Python 3.
# https://www.codecademy.com/courses/learn-python-3/lessons/learn-python-files/exercises/review

with open("file_name.txt", "w") as file:
  file.write("How you gonna win when you ain't right within?")
#  print(file.read())
  
with open("file_name.txt") as file:
  print(file.read())