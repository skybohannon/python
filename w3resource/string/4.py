# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


def replace_chars(str):
    first_char = str[0]
    new_str = ""
    for char in str[1:]:
        if char == first_char:
            char = '$'
        new_str = new_str + char
    return first_char + new_str


print(replace_chars('restart'))
