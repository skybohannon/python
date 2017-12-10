# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def in_between(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


print(in_between(1000))
print(in_between(1500))
print(in_between(2100))
