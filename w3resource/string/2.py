# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}


def num_chars(s):
    dict = {}
    for char in s:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1

    return dict


print(num_chars('google.com'))
