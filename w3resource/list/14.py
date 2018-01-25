# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.


def remove_evens(l):
    new_list = [x for x in l if x%2 != 0]
    return new_list


print(remove_evens([1,2,3,4,5,6,7,8]))
