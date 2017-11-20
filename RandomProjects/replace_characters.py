# # Replacing multiple characters in a string
#
#
# def replace(text, old_chars, new_chars):
#     """ Return text with old chars replaced with new chars.
#
#     >>> replace('heWlXo theYreZ', 'WXYZ', 'YZWX')
#     >>> 'heYlZo theWreX'
#     """
#
#     # your code here

hello_there = "hewlXo theYreZ"
oldchars = "WXYZ"
newchars = "YZWX"


def replace(string, old_chars, new_chars):
    _tab = str.maketrans(dict(zip(old_chars, new_chars)))
    return string.translate(_tab)


print(replace(hello_there, oldchars, newchars))
