# 12. Write a Python program to count the occurrences of each word in a given sentence.


def count_occurances(str):
    wordcount = {}
    words = str.split()

    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

    return wordcount


print(count_occurances("This this is a test sentence sentence one two three"))
