# 30. Write a Python program that will accept the base and height of a triangle and compute the area.


def tri_area(b, h):
    return "The area of the triangle with a base of {} and height of {} is {}".format(b, h, 1/2 * (b * h))


print(tri_area(5, 3))
