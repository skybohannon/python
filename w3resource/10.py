# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

n = input("Please enter a number: ")
n1 = int(n)
n2 = int("{}{}".format(n, n))
n3 = int("{}{}{}".format(n, n, n))
print(n1 + n2 + n3)