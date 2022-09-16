print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = input("What's your weight?\n")
planet = input("Which planet are you going to?\n")

weight = int(weight)
planet = float(planet)

# Write an if statement below:

if planet == 1:
  planet = "Venus"
  weight = weight * 0.91
elif planet == 2:
  planet = "Mars"
  weight = weight * 0.38
elif planet == 3:
  planet = "Jupiter"
  weight = weight * 2.34
elif planet == 4:
  planet = "Saturn"
  weight = weight * 1.06
elif planet == 5:
  planet = "Uranus"
  weight = weight * 0.92
elif planet == 6:
  planet = "Neptune"
  weight = weight * 1.19

print("Your weight on", planet, "is", weight)
