# 26. Write a Python program to create a histogram from a given list of integers.


def histo(lst):
    for n in lst:
        result = ""
        how_many = n
        while (how_many > 0):
            result += '*'
            how_many -= 1
        print(result)


print(histo([1, 3, 4, 2, 6]))
