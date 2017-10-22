# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import pytz
import datetime

locations = {'1': "US/Pacific",
           '2': "US/Mountain",
           '3': "US/Central",
           '4': "US/Eastern",
           '5': "Europe/London",
           '6': "Europe/Moscow",
           '7': "Europe/Oslo",
           '8': "Europe/Paris",
           '9': "Europe/Amsterdam"}

print("Please choose a time zone (or 0 to quit): ")

for place in sorted(locations):
    print("\t{}. {}".format(place, locations[place]))

while True:
    choice = input()

    if choice == '0':
        break

    if choice in locations.keys():
        tz_to_display = pytz.timezone(locations[place])
        worldTime = datetime.datetime.now(tz=tz_to_display)
        print("Current time in {} is {}".format(locations[place], worldTime.strftime('%A %x %X')))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))


