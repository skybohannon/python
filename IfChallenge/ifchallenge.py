# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.


name = input("What is your name? ")
age = int(input("What is your age? "))

if (age >= 18 and age < 31):
    print("Hello, {0} You are {1} years old and eligable for the holiday".format(name, age))

elif (age < 18):
    print("Hello, {0} You are {1} years old and too young for the holiday".format(name, age))

else:
    print("Hello, {0} You are {1} years old and too old for the holiday".format(name, age))