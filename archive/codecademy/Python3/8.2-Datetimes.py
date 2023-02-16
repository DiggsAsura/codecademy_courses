# Trying to follow along a video in Codecademy. 
# Datetimes

# 1. Import the 'datetime' module
# 2. Create a date using year, month, day as arguments
# 3. Create a date using datetime.now()
# 4. Parse a date using strptime
# 5. Render a date as a string using strftime

from datetime import datetime

birthday = datetime(1984, 5, 12, 5, 30) #year, month, day, hours, mins, etc

print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.weekday()) # 0 = monday
print(datetime.now())
print(datetime(2022, 2, 18) - datetime(1984, 5, 12))
print(datetime.now() - datetime(1984, 5, 12)) 

# 4
parsed_date = datetime.strptime('May 12, 2022', '%b %d, %Y')
print(parsed_date)
print(parsed_date.month)
print(parsed_date.year)

# Theres a bunch of good documentation on more %'s fx over at the official docs!

# 5 - strftime (f stands for format) Create a string
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)


# Ok this is cool stuff. I think this is very useful, but the big takeaway
# looks like the official Python docs!
# Great stuff. 
