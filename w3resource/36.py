# 36. Write a Python program to add two objects if both objects are an integer type.


def addup(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return "Both objects must be integers"


print(addup(1, 2))
print(addup(1, "b"))