# This function will print a hardcoded count of how many locations we have.

# Fix the code so both functions can access favorite_locations. 
# Problem is the code was insdie a def, which then is isolated to that function. 

favorite_locations = "Paris, Norway, Iceland"


def print_count_locations():
    #favorite_locations = "Paris, Norway, Iceland"
    print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()
