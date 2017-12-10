# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.


def copies(str, n):
    result = ""
    if len(str) < 2:
        for i in range(n):
            result = str + str
    else:
        for i in range(n):
            result = result + str[:2]
    return result


print(copies("Yo dogg", 3))
print(copies("po", 6))
