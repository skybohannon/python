# 22.Write a Python program to sort a string lexicographically.
# Click me to see the sample solution


def sort_lex(s):
    return sorted(sorted(s), key=str.upper)


print(sort_lex("Test sentence"))