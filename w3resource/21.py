# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an
# appropriate message to the user


def odd_even(n):
    if n % 2 == 0:
        return "{} is an even number".format(n)
    else:
        return "{} is an odd number".format(n)


print(odd_even(2))
print(odd_even(3))
