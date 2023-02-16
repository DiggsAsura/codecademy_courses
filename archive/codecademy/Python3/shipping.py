# Task 1
weight = input("Package weight (lbs): ")
weight = float(weight)

ground_flat = 20
ground_premium_flat = 125
drone_flat = 0

# Ground/Drone shipping
if weight <= 2:
  cost_ground = weight * 1.50
  cost_drone = weight * 4.5
elif weight <= 6:
  cost_ground = weight * 3
  cost_drone = weight * 9
elif weight <= 10:
  cost_ground = weight * 4
  cost_drone = weight * 12
else:
  cost_ground = weight * 4.75
  cost_drone = weight * 14.25


print("Prices:")
print("Ground Shipping: " + str(cost_ground + ground_flat))
print("Ground Shipping Premium:", ground_premium_flat)
print("Drone Shipping:", cost_drone)

