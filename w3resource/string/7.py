# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'


def bad_poor(str):
    nots = str.find('not')
    poors = str.find('poor')

    if poors > nots:
        str = str.replace(str[nots:(poors + 4)], 'good')
    return str


print(bad_poor("The lyrics is not that poor!"))
