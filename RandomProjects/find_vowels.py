# Define a function that takes a word as an argument, returns a list of
# truth values i.e., True for a vowel in the word, False for a non-vowel.
#
# def find_vowels(word):
#     Return a list containing a True for a vowel in the word,
#     a False for a non-vowel.
#
#     >>> find_vowels('detestable')
#     >>> [False, True, False, True, False, False, True, False, False, True]

import re

boolList = []
userWord = input("Please enter a single word: ")


def find_vowels(user_word):
    for char in user_word:
        found = re.search(r'[aeiou]', char.lower())
        if found:
            boolList.append(True)
        else:
            boolList.append(False)
    return boolList


print("Vowels list for " + userWord + "\n" + str(find_vowels(userWord)))
