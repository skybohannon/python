# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#
#
# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'


def first_half(s):
    return s[:int(len(s) / 2)]


print(first_half('HelloThere'))