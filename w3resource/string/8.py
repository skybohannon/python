# 8. Write a Python function that takes a list of words and returns the length of the longest one.


def find_longest(lst):
    len_list = []
    for word in lst:
        len_list.append((len(word), word))
    len_list.sort()
    return len_list[-1][1]


print(find_longest(['one', 'two', 'three', 'four']))
