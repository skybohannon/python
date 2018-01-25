# 8. Write a Python program to check a list is empty or not.


def check_empty(l):
    if not l:
        return "List is empty"
    else:
        return "List is populated"


print(check_empty([1,2,3]))
print(check_empty([]))