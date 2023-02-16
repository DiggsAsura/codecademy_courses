# 4. Data Manipulation in Python
# 1. Data Manipulation with Pandas
# 1. Creating, Loading and Selecting Data with Pandas
# 10. Select Multiple Rows

'''
You can also select multiple rows from a DataFrame.

Here are a few more rows from ShoeFly.com's orders DataFrame:

id	first_name	last_name	email	shoe_type	shoe_material	shoe_color
54791	Rebecca	Lindsay	RebeccaLindsay57@hotmail.com	clogs	faux-leather	black
53450	Emily	Joyce	EmilyJoyce25@gmail.com	ballet flats	faux-leather	navy
91987	Joyce	Waller	Joyce.Waller@gmail.com	sandals	fabric	black
14437	Justin	Erickson	Justin.Erickson@outlook.com	clogs	faux-leather	red
79357	Andrew	Banks	AB4318@gmail.com	boots	leather	brown
52386	Julie	Marsh	JulieMarsh59@gmail.com	sandals	fabric	black
20487	Thomas	Jensen	TJ5470@gmail.com	clogs	fabric	navy
76971	Janice	Hicks	Janice.Hicks@gmail.com	clogs	faux-leather	navy
21586	Gabriel	Porter	GabrielPorter24@gmail.com	clogs	leather	brown


Here are some different ways of selecting multiple rows:

- orders.iloc[3:7] would select all rows starting at the 3rd row and up to but not 
  including the 7th row (i.e the 3rd row, 4th row, 5th and 6th row)


id	first_name	last_name	email	shoe_type	shoe_material	shoe_color
14437	Justin	Erickson	Justin.Erickson@outlook.com	clogs	faux-leather	red
79357	Andrew	Banks	AB4318@gmail.com	boots	leather	brown
52386	Julie	Marsh	JulieMarsh59@gmail.com	sandals	fabric	black
20487	Thomas	Jensen	TJ5470@gmail.com	clogs	fabric	navy


- order.iloc[:4] would select all rows up to, but not including the 4th row (ie 0th, 1st
2nd and 3rd rows)

- orders.iloc[-3:] would select the rows starting at the 3rd to last row and up to and
  including the final row


'''

import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

april_may_june = df.iloc[-3:]
print(april_may_june)