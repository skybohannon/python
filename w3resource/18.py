# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then
# return thrice of their sum. Go to the editor



def sums(n1, n2, n3):
    if n1 == n2 == n3:
        return (n1+n2+n3) * 3
    else:
        return n1 + n2 + n3


print(sums(12, 12, 12))
print(sums(1, 3, 5))
