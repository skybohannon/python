# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.


def summy(n1, n2):
    s = n1 + n2
    if s >= 15 and s <= 20:
        return 20
    else:
        return s


print(summy(10, 5))
print(summy(11, 12))
