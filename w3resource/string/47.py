# 47. Write a Python program to lowercase first n characters in a string. Go to the editor

def lower_first(n, s):
    return s[:n].lower() + s[n:]

print(lower_first(2, "THE SMALL RED FOX JUMPED OVER THE LAZY BROWN DOG."))