# 10. Write a Python program to change a given string to a new string where the first and last chars h
# ave been exchanged.


def change_str(str):
    length = len(str)
    return str[-1:] + str[1:length-1] + str[0]


print(change_str("The quick brown fox jumped over the lazy dog"))
