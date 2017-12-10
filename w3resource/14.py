# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
from datetime import date


date_1 = date(2014, 7, 2)
date_2 = date(2014, 7, 11)
date_diff = date_2 - date_1

print("There are {} days in between {} and {}".format(date_diff.days, date_1, date_2))
