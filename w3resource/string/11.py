# 11. Write a Python program to remove the characters which have odd index values of a given string.


def remove_odds(str):
    new_str = ""
    for i in range(len(str)):
        if i % 2 == 0:
            new_str = new_str + str[i]

    return new_str


print(remove_odds("The quick brown fox jumped over the lazy dog"))
