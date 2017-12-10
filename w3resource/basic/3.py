# 3. Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

import datetime

time_now = datetime.datetime.now()
print("Current date and time: \n" + time_now.strftime("%Y-%m-%d %H:%M:%S"))
