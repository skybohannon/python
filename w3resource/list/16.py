# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are
# square of numbers between 1 and 30 (both included).


def squarezz():
    sq_list = []
    for i in range(1, 30):
        sq_list.append(i**2)
    print(sq_list[:5] + sq_list[-5:])


squarezz()
