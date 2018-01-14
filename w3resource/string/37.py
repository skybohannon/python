# 37. Write a Python program to display a number in left, right and center aligned of width 10

x = 22

print("Original number: {}\nLeft aligned, width 10:   {:<10d}".format(x, x))
print("Original number: {}\nRight aligned, width 10:  {:10d}".format(x, x))
print("Original number: {}\nCenter aligned, width 10: {:^10d}".format(x, x))
