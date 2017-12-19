# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


def new_str(str):
    if len(str) < 2:
        return ''
    else:
        return str[0:2] + str[-2:]


print(new_str('w3resource'))
print(new_str('w3'))
print(new_str('w'))
