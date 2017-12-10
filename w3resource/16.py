# 16. Write a Python program to get the difference between a given number and 17, if the number is
# greater than 17 return double the absolute difference.


def absdiff(n):
    if n >= 17:
        return n - 17
    else:
        return "Number was not greater or equal to 17"


print(absdiff(18))
print(absdiff(22))
print(absdiff(15))
