# Question 29
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.


def printsquares(a, b):
    d = {}
    for i in range (a, b + 1):
        d[i] = i ** 2
    print(d)


printsquares(1, 30)
