# 1. Write a Python program to sum all the items in a list.


def sum_nums(l):
    total_of = 0
    for n in l:
        total_of += n
    return total_of


print(sum_nums([1, 2, 3, 4, 5, 6]))
