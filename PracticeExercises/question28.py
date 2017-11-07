# Question:
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
#
# Hints:
#
# Use int() to convert a string to integer.

def str_sum(a, b):
    summed = int(a) + int(b)
    return summed

print(str_sum("45", "69"))