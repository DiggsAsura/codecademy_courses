# Task. Print the allowed heights (above 161) using conditionals and list comprehension
# This one was rough. Many failed attempts, because i placed the if at the wrong place. This
# one does not make entirly sense for me yet.  

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

#can_ride_coaster = [if height >= 161 for height in heights]

# wron returns (True, True, False...)
#can_ride_coaster = [i >= 161 for i in heights]

# wrong returns (False, True, False...)
#can_ride_coaster = [i > 161 for i in heights]

# syntax error
#can_ride_coaster = [if height > 161 for height in heights]

# syntax error - this one was close though!
#can_ride_coaster = [for height in heights if height > 161]

# looked at hint.
can_ride_coaster = [height for height in heights if height > 161]
# why does it matter where the if is coming? 
print(can_ride_coaster)