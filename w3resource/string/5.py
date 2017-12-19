# 5. Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


def mixup(a, b):
    n_a = b[:2] + a[2:]
    n_b = a[:2] + b[2:]
    return n_a + ' ' + n_b


print(mixup('abc', 'xyz'))
