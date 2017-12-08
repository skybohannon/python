# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring
# upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower()
# returns the lowercase version of a string.
#
<<<<<<< HEAD
#
=======
>>>>>>> master
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
<<<<<<< HEAD
    if len(a) >= len(b):
        longest = a
        shortest = b
    else:
        longest = b
        shortest = a

    if longest.lower().endswith(shortest.lower()):
        return True
=======
    long_s, short_s = (a, b) if len(a) >= len(b) else (b, a)
    return long_s.lower().endswith(short_s.lower())
>>>>>>> master


print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
<<<<<<< HEAD
print(end_other('abc', 'abXabc'))
=======
print(end_other('abc', 'abXabc'))
>>>>>>> master
