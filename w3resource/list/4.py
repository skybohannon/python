# 4. Write a Python program to get the smallest number from a list.


def smallest(l):
    smallest = 0
    for n in l:
        if n < smallest:
            smallest = n

    return smallest


print(smallest([0,-2,5,-8,-16,9]))
