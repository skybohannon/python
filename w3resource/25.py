# 25. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


def in_values(i, lst):
    if i in lst:
        return True
    else:
        return False


print(in_values(3, [1, 5, 8, 3]))
print(in_values(-1, [1, 5, 8, 3]))
