# 27. Write a Python program to concatenate all elements in a list into a string and return it.


def concatlst(lst):
    result = ""
    for i in lst:
        result = result + str(i)
    return result


print(concatlst(["hello", "goodbye"]))
print(concatlst(["a", "b", "c"]))
print(concatlst([1, 2, 4, 5]))
