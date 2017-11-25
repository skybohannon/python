# Given two strings, a and b, return the result of putting them together in the order abba,
# e.g. "Hi" and "Bye" returns "HiByeByeHi".
#
#
# make_abba('Hi', 'Bye') → 'HiByeByeHi'
# make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
# make_abba('What', 'Up') → 'WhatUpUpWhat'

word_1 = "Hi"
word_2 = "Bye"


def make_abba(s1, s2):
    new_string = word_1 + word_2 + word_2 + word_1
    return new_string


print(make_abba(word_1, word_2))
