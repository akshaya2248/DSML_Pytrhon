##Write a script to subtract 5 days from current date

# Import the date class and the timedelta class from the datetime module
from datetime import date, timedelta

# Calculate the date 5 days before today's date
dt = date.today() - timedelta(5)

# Print the current date using date.today()
print('Current Date :', date.today())

# Print the date calculated 5 days before the current date
print('5 days before Current Date :', dt)

##SECOND METHORD

from datetime import date, timedelta
dt = date.today() - timedelta(3)
print("Current Date :",date.today())
print("Three days before Current Date :",dt)
