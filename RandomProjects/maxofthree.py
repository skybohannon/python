def maxthree(a, b, c):
    maxOf = 0
    if a > b:
        if a > c:
            maxOf = a
        else:
            maxOf = c
    else:
        if b > c:
            maxOf = b
        else:
            maxOf = c

    print(maxOf)

maxthree(1, 4, 5)