# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# The area of circle is pi times the square of its radius.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

from math import pi

radius = float(input("Please enter the radius of your circle: "))
area = pi * (radius**2)
print("Radius: {}\nArea: {}".format(radius, area))