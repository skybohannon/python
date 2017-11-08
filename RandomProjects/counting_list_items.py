userList = ['one', 'two', 'two', 'three', 'three', 'three']


def count_items(lst):
    d = dict.fromkeys(set(lst), 0)

    for i in userList:
        d[i] += 1

    return d


print(count_items(userList))
