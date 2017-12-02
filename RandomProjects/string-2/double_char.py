# Given a string, return a string where for every char in the original, there are two chars.
#
#
# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'


def double_char(s):
    new_string = ""
    for char in s:
        new_string += char*2
    return new_string


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
