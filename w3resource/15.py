# 15. Write a Python program to get the volume of a sphere with radius 6.

from math import pi

user_radius = float(input("Find the volume of a radius\n---------------------\nPlease enter a radius: "))
sphere_volume = (4/3) * pi * user_radius**3
print(sphere_volume)