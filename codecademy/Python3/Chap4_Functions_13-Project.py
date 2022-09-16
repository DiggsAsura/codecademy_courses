# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

# The Functions Project, last stop of the chapter

# First try - checked hint, looks promising. 
# (wrote it before checking!)
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

# big a-ha moment about return application!!!
f100_in_celsius = f_to_c(100)

# why the hell is this wrong
# because it's not. had the calculation wrong! 
# ok im learning to really go over the details
print(f100_in_celsius)


# Task 3, make the same function just vica versa
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_farenheit = c_to_f(0)

print(c0_in_farenheit)
# boom!


# Task 5, next part of the lesson - Use the Force
# ok first try, on thin ice here. Not sure if this is correct.
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)
# forgot at first there was commented part of the code at the top!
# seems correct at first try, no hint! boomtown!

print("The GE train supplies", train_force, "Newtons of force")

# Looks like i got this one too
def get_energy(mass, c=3*10**8):
  return mass * c

# hmmm did i? the hint (checked after), asks for a much bigger number
bomb_energy = get_energy(bomb_mass)

print("A 1kg bomb supplies", bomb_energy, "Joules")


# Task 11 - Do the Work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance
# had to check the hint, think i did right, ecept didnt call on the parameters in get_force()

train_work = get_work(train_mass, train_acceleration, train_distance)

# did it work????
print("The GE train does", str(train_work), "Joules of work over", str(train_distance), "meters.")

# it did, but the hint says remember to use str() on train_work and train_distance. It worked without too so hmm. 95%!


