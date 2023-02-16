product_1_name = "iPhone 11 Pro Max"
product_1_price = 8000

product_2_name = "MacBook Pro 2015"
product_2_price = 5000

bundle_off_total = 0.90
bundle_off = 0.10

customer_one_items = ""
customer_one_total = 0


customer_one_items += product_1_name + ", " + product_2_name

customer_one_total += product_1_price + product_2_price

print("Customer One items:")
print(customer_one_items)

print("Bundle 10% off: " + str(customer_one_total * bundle_off))
print("Customer One total: " + str(customer_one_total * bundle_off_total))



