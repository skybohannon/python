# 1. Write a Python function to convert a given string to all uppercase if it contains at least 2
# uppercase characters in the first 4 characters.


def conv_up(s):
    count = 0
    for c in s[:4]:
        if c.isupper():
            count += 1
    if count >= 2:
        return s.upper()
    return s


print(conv_up("ThE quick brown fox jumped over the lazy dog"))
print(conv_up("The quick brown fox jumped over the lazy dog"))
