# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math


def distance(p1, p2):
    dist = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    return "The distance between {} and {} is {}".format(p1, p2, dist)


print(distance([4, 0], [6, 6]))
