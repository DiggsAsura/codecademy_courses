# 7. Specialized Collections
# 2. Collections
# 7. ChainMap

print('\nChainMap\n-------------')

# There is another way to store dictionaries or other mappings in Python. We have
# looked at the defaultdict and OrderedDict so far and they handle a lot of situations
# so what else could we possible need?
#
# Well, the ChainMap container allows us to store many mappings in an ordered
# group, but lookups (accessing the value using a key) are repeated for every
# mapping inside of the ChainMap until something is found or the end is reached.
# If we try to modify the data in any way, then only the first mapping in the 
# ChainMap will receive the changes. When accessing data, one way to think of
# the ChainMap is that it treats all of the stored dictionaries as one large 
# dictionary, where if there are repeated keys, then the first found result is 
# returned. Let's see what this looks like with an example using a customer's
# clothing dimensions!
#
# First, we import the ChainMap container and set up our data.
from collections import ChainMap

customer_info = {
  'name': 'Dimitri Buyer',
  'age': '31',
  'address': '123 Python Lane',
  'phone_number': '5552930183'
}

shirt_dimensions = {
  'shoulder': 20,
  'chest': 42,
  'torso_length': 29
}

pants_dimensions = {
  'waist': 36,
  'leg_length': 42.5,
  'hip': 21.5,
  'thigh': 25,
  'bottom': 18
}

# Next, we initialize a ChainMap with the mappings which we want to use. In this
# case, the mappings are the dimensions dictionaries.
customer_data = ChainMap(customer_info, shirt_dimensions, pants_dimensions)

# Now we can access values from any of the stored mappings.
customer_leg_length = customer_data['leg_length']

# The parents property skips the first mapping and returns everything else (all
# of the parents of the first mapping)
customer_size_data = customer_data.parents

# We can directly modify the data only in the first dictionary.
customer_data['address'] = '456 ChainMap Drive'

# Note: In order to modify data from dictionaries which are deeper in the
# ChainMap, we will need to iterate through the dictionaries which are stored
# inside of it.
#
# As we can see in this example, we create a new ChainMap using three different
# dictionaries. This allows us to access any of the key:value pairs stored 
# inside.
#
# Another interesting concept that the ChainMap uses is the concept of a parent
# mappings. If we use the .parents property, all mappings except the first one
# will be returned. This is because those mappings are considered to be the
# parent mappings to the first one. You can add a new "child" mapping to the front
# of the list of mappings using the .new_child() method.
#
# To find out more about this container, check out the Python Documentation:
# https://docs.python.org/3/library/collections.html#collections.ChainMap
#
# Now let's use a ChainMap to keep track of our clothes business profits for the
# last 12 months!


print('\nTasks\n---------')

# 1. Our business has been doing well over the past year and we have been provided
#    with a list of dictionaries representing the amount of profit per month as
#    well as additional profit from holidays when applicable. We want an easy way
#    to monitor our profit over the most recent 12 month period. To do this, we
#    can use the ChainMap class. This will allow us to conserve historical data
#    while also allowing us to retrieve the most recent data. It will even allow
#    us to work with additional keys within dictionary updates.
#
#    First, remember to import ChainMap. Then create a new ChainMap called 
#    profit_map using the year_profit_data list. Remember that a ChainMap
#    accepts a variable number of arguments so we need to expand the list (*)
#    so the constructor will read them as individual arguments instead of
#    single argument.
#
# 2. For the next step, we need logic which will be able to calculate the normal
#    profits and the holiday profits separately. Create a function called 
#    get_profits which calculates the sum of the standard profits (keys not
#    containing 'holiday') and the holiday profits (keys containing 'holiday')
#    in two different variables. Make this function return the two variables:
#    the standard profit first and the holdicay profit second. Additionally,
#    call the function using the profit_map and store the results in variables
#    called last_year_standard_profit and last_year_holiday_profit.
#
# 3. It has been three months and our accountant has sent three more months
#    worth of profit data in the form of a list of dictionaries called
#    new_months_data. Add the new mappings to the profit_map so that the old
#    January - March months are still in the ChainMap, but accessing those keys 
#    will return data for the most recent three months. Call the get_profits
#    function on the profit_map again and store the results in current_year_standard_profit
#    and current_year_holiday_profit to calculate the sum of the most
#    recent 12 months of profit data.
#
# 4. Finally, we want to take a look at the difference in the last 12 month
#    period compared to the current 12 month period. Calculate the difference
#    for the standard and holiday profits and store them in variables
#    called year_diff_standard_profit and year_diff_holiday_profit. Print
#    out the results to see the difference in profit for the current 12 
#    month period.

year_profit_data = [
    {'jan_profit': 15492.30, 'jan_holiday_profit': 2589.12},
    {'feb_profit': 17018.05, 'feb_holiday_profit': 3701.88},
    {'mar_profit': 11849.13},
    {'apr_profit': 9870.68},
    {'may_profit': 13662.34},
    {'jun_profit': 12903.54},
    {'jul_profit': 16965.08, 'jul_holiday_profit': 4360.21},
    {'aug_profit': 17685.69},
    {'sep_profit': 9815.57},
    {'oct_profit': 10318.28},
    {'nov_profit': 23295.43, 'nov_holiday_profit': 9896.55},
    {'dec_profit': 21920.19, 'dec_holiday_profit': 8060.79}
]

new_months_data = [
    {'jan_profit': 13977.85, 'jan_holiday_profit': 2176.43},
    {'feb_profit': 16692.15, 'feb_holiday_profit': 3239.74},
    {'mar_profit': 17524.35, 'mar_holiday_profit': 4301.92}
]

#! from collections import ChainMap

profit_map = ChainMap(*year_profit_data)



def get_profits(profit_map):
  holiday_total = 0
  standard_total = 0
  
  for key in profit_map.keys():
    if 'holiday' in key:
      holiday_total += profit_map[key]
    else:
      standard_total += profit_map[key]
  
  return standard_total, holiday_total

last_year_standard_profit, last_year_holiday_profit = get_profits(profit_map)

print(f'Last year holiday profit: {last_year_holiday_profit}')
print(f'Last year standard profit: {last_year_standard_profit}')


for item in new_months_data:
  profit_map = profit_map.new_child(item)

current_year_standard_profit, current_year_holiday_profit = get_profits(profit_map)
print(f'Current year standard profit: {current_year_standard_profit}')
print(f'Current year holiday profit: {current_year_holiday_profit}')

year_diff_standard_profit = current_year_standard_profit - last_year_standard_profit
year_diff_holiday_profit = current_year_holiday_profit - last_year_holiday_profit

print(f'Year difference, standard profit: {year_diff_standard_profit}')
print(f'Year difference, holiday profit: {year_diff_holiday_profit}')


# Ok I gotta admit, these collections chapters are pretty hard in terms
# of keeping motivation up. Rough mentally to get through, hard to keep
# motivated. But I'll push on. It won't stick as good, but I do beleive
# that I have pushed to far before actually applying alot of what I have 
# learned prior. I do this mostly to have them in the back of my head, whenever
# I reach that point when I need them later on.

