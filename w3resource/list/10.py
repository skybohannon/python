# 10. Write a Python program to find the list of words that are longer than n from a given list of words.


def find_longer(n, l):
    longer = []
    for x in l:
        if len(x) > n:
            longer.append(x)
    return "Words that are longer than {} characters: {}".format(n, longer)


print(find_longer(3, ['the', 'quick', 'red', 'fox', 'jumped', 'over', 'the', 'lazy', 'brown', 'doge']))
