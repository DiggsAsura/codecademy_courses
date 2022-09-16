# Chapter 11 - Classes
# 1. Introduction to Classes
# 7. Methods with Arguments
#
# Methods can also take more arguments than just self:
class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
#
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
#
# Above we defined a DistanceConverter class, instantiated it, and used it to 
# convert 5 miles into kilometers. Notice again that even through how_many_kms takes
# two arguments in its definition, we only pass miles, because self is implicitly 
# passed (and refers to the object converter). 

# Tasks
# 1. It's March 14th (known in some places as Pi day) at Jan van High, and you're 
# 	 feeling awfully festive. You decide to create a program that calculates the 
# 	 area of a circle. 
# 
# 	 Create a Circle class with class variable pi. Set pi to be the approximation 
# 	 3.14
#
# 2. Give Circle an area method that takes two parameters: self and radius.
#
# 	 Return the area as given by this formula:
# 	 	area = pi * radius ** 2
#
# 3. Create an instance of Circle. Save it to the variable circle
# 
# 4. You go to measure several circles you happen to find around.
# 		- A medium pizza that is 12 inches across
#			- Your teaching table which is 36 inches across
# 		- The Round Room auditorium, which is 11,460 inches across
#
#		 You save the areas of these three things into pizza_area, teaching_table_area,
#		 and round_room_area
#
# 	 Remember that the radius of a circle is half the diamter. We gave three 
# 	 diameters here, so halve them before you calculate the given circle's area. 

class Circle:
	pi = 3.14
	def area(self, radius):
		area = Circle.pi * radius ** 2
		return area
		
circle = Circle()

pizza_area = circle.area(12/2)
print("Pizza area: " + str(pizza_area))

teaching_table_area = circle.area(36/2)
print("Teaching table area: " + str(teaching_table_area))

round_room_area = circle.area(11460/2)
print("Round room area: " + str(round_room_area))

# Remember to add the method! Kept forgetting to add circle.area :) 

