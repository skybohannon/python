# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.


def string_expand(s, n):
    result = ""
    for i in range(n):
        result = result + s
    return result


print(string_expand("booty", 3))
print(string_expand("corgi baby", 10))
