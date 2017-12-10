# 22. Write a Python program to count the number 4 in a given list.


def count4(lst):
    count = 0
    for i in lst:
        if i == 4:
            count += 1
    return "There were {} occurances of 4 in your list".format(count)


print(count4([1, 2, 3, 4]))
print(count4([4, 4, 2]))
print(count4([2, 4, 6, 4, 8]))
