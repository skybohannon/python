# 2. Write a Python program to multiplies all the items in a list.


def multiply_list(l):
    total = 1
    for n in l:
        total *= n
    return total


print(multiply_list([1,2,3,4,5,6]))
