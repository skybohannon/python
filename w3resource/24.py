# 24. Write a Python program to test whether a passed letter is a vowel or not.


def isvowel(s):
    vowels = 'aeiou'
    if s in vowels:
        return "{} is a vowel".format(s)
    else:
        return "{} is not a vowel".format(s)


print(isvowel('a'))
print(isvowel('b'))
