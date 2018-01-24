# 49. Write a Python program to count and display the vowels of a given text.


def count_vowels(s):
    vowels = "aeiouAEIOU"
    vcount = len([letter for letter in s if letter in vowels])
    vlist = [letter for letter in s if letter in vowels]
    print(vcount)
    print(vlist)


count_vowels("The quick brown fox jumped over the lazy red doge.")
