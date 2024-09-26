# Date: A date in Python is not a data type of its own, but we can import a module named
# datetime to work with dates as date objects.

import datetime
x = datetime.datetime.now()
print(x)

# Creating date object: To create a date, we can use the datetime() class (constructor) of the
# datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.

import datetime

x = datetime.datetime(2021, 5, 17)

print(x)


# The strftime() method: The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the
# returned string:

import datetime
x = datetime.datetime(2027, 5, 17)
print(x.strftime("%B"))





