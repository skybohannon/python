# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("What is your name? ")
age = int(input("What is your age? "))

if (age >= 18 and age < 31):
    print("You are {0}, and in the correct age bracket for this trip, {1}.\nEnjoy your trip!".format(age,name))
elif (age < 18):
    print("Sorry, you are {0} and too young for this trip, {1}".format(age,name))
else:
    print("Sorry, you are {0} and too old for this trip, {1}".format(age,name))