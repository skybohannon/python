# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring
# upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower()
# returns the lowercase version of a string.
#
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
    if len(a) >= len(b):
        longest = a
        shortest = b
    else:
        longest = b
        shortest = a

    if longest.lower().endswith(shortest.lower()):
        return True


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
