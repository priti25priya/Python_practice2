# Timezone is defined as a geographical area or region throughout which standard time is observed.
# It basically refers to the local time of a region or country. Most of the time zones are offset
# from Coordinated Universal Time (UTC), the world’s standard for time zone.
# In order to get the current time of different time zones, we will be using the pytz python library.
# 1.
import time


curr_time = time.localtime()
curr_clock = time.strftime("%H:%M:%S", curr_time)

print(curr_clock)

# 2.
from datetime import datetime
import pytz

# get the standard UTC time
UTC = pytz.utc

# it will get the time zone
# of the specified location
IST = pytz.timezone('Asia/Kolkata')

# print the date and time in
# standard format
print("UTC in Default Format : ",
	datetime.now(UTC))

print("IST in Default Format : ",
	datetime.now(IST))

# print the date and time in
# specified format
datetime_utc = datetime.now(UTC)
print("Date & Time in UTC : ",
	datetime_utc.strftime('%Y:%m:%d %H:%M:%S %Z %z'))

datetime_ist = datetime.now(IST)
print("Date & Time in IST : ",
	datetime_ist.strftime('%Y:%m:%d %H:%M:%S %Z %z'))
