# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.


def summy(a, b, c):
    s = a + b + c
    if a == b or a == c or b == c:
        return 0
    else:
        return s


print(summy(2, 1, 2))
print(summy(3, 2, 2))
print(summy(2, 2, 2))
print(summy(1, 2, 3))
