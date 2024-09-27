# 1.
import datetime

first_date = datetime.datetime(year=2024, month=1, day=1)
second_date = datetime.datetime(year=2024, month=5, day=27)
interval = second_date - first_date
print(interval)

# 2.
# Timedelta function demonstration

from datetime import datetime, timedelta

# creating datetime objects
date1 = datetime(2020, 1, 3)
date2 = datetime(2020, 2, 3)

# difference between dates
diff = date2 - date1
print("Difference in dates:", diff)

# Adding days to date1
date1 += timedelta(days = 4)
print("Date1 after 4 days:", date1)

# Subtracting days from date1
date1 -= timedelta(15)
print("Date1 before 15 days:", date1)
