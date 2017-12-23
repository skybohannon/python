# 23. Write a Python program to remove a newline in Python.


def remove_n(s):
    return s.replace("\n", "")


print(remove_n("The quick brown fox jumped over the lazy dog\nThe quick brown fox jumped over the lazy dog"))