# 3. Write a Python program to get the largest number from a list.


def largest(l):
    max = 0
    for n in l:
        if n > max:
            max = n
    return max


print(largest([1,2,-8,0]))
