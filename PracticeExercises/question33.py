# Question:
# Define a function which can generate a list where the values are square of numbers between
# 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
#
# Hints:
#
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list


def squarelist(a, b):
    s = []
    for i in range(a, b+1):
        s.append(i ** 2)
    print(s[0:5])


squarelist(1, 20)
