# 48. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

def swappy(s):
    maketrans = s.maketrans
    return s.translate(maketrans(',.', '.,'))


print(swappy("13.337,83"))


def swappy2(s):
    intab = "aeiou"
    outtab = "12345"
    trantab = str.maketrans(intab, outtab)
    return s.translate(trantab)


print(swappy2("The quick red fox jumped over the lazy brown dog."))
