# 34. Write a Python program to print the following integers with '*' on the right of specified width.
x = 3
y = 123

print("Original number: {}\nFormatted number (right padding, width 2): {:*< 2d}".format(x, x))
print("Original number: {}\nFormatted number (right padding, width 6): {:*< 6d}".format(y, y))