# Challenge 2 - Over Budget

# We want to save some money and we are watching our budget. We need to make sure that the result of our spending
# is less than the total amount we have allocated for each of the categories. Our function will accept a parameter
# called budget which describes our spending limit. The four parameters describe what we are spending our
# money on. We need to sum all of our spendings and compare it to the budget. If we have gone over budget, return
# true, otherwise False. 

# Steps
# 1. Define the function to accept five parameter starting with budget, food_bill, electricity_bill, internet_bill
# and rent
# 2. Calculate the sum of the last four parameters
# 3. Use if and else statements to test if the budget is less than the sum
# 4. If the condition is true, return True, otherwise return False. 


def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
	expense = food_bill + electricity_bill + internet_bill + rent
	if expense > budget:
		return True
	else: 
		return False
 
 
 # Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True


# Second challenge very easy too! 

