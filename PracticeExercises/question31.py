# 2.10
#
# Question:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20
# (both included) and the values are square of keys. The function should just print the keys only.
#
# Hints:
#
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


def printsquares(a, b):
    d = {}
    for i in range (a, b + 1):
        d[i] = i ** 2

    for (k, v) in d.items():
        print(k, end=' ')


printsquares(1, 40)