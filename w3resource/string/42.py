# 42. Write a python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
import collections

str1 = "thequickbrownfoxjumpsoverthelazydog"
d = collections.defaultdict(int)

for char in str1:
    d[char] += 1

for char in sorted(d, key=d.get, reverse=True):
    if d[char] > 1:
        print("{} {}".format(char, d[char]))
