# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

cal_year = int(input("Please enter the year: "))
cal_month = int(input("Please enter the month (in digits): "))

print(calendar.month(cal_year, cal_month))