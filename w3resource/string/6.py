# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
#  string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


def add_stuff(str):
    if len(str) > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else:
            str += 'ing'
    return str

print(add_stuff('abc'))
print(add_stuff('string'))
print(add_stuff('booty'))
print(add_stuff('ab'))
