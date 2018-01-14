# 33. Write a Python program to print the following integers with zeros on the left of specified width.

x= 3
y = 123

print("Original number: {}\nFormatted number (left padding, width 2): {:0>2d}".format(x, x))
print("Original number: {}\nFormatted number (left padding, width 6): {:0>6d}".format(y, y))