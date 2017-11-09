# Return the first vowel in each word of a string.
import re

sentence = "The sky's booty the limit"

def first_vowels(s):
    regex = re.findall(r"\b\w*?([aeiouAEIOU])", s)
    print(regex)
    joined_str = ", ".join(regex)
    return joined_str

print(first_vowels(sentence))