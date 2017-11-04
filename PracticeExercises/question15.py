# Question 15
# Level 2
#
# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

x = input("Please enter a number: ")
n1 = int(x)
n2 = int("{}{}".format(x, x))
n3 = int("{}{}{}".format(x, x, x))
n4 = int("{}{}{}{}".format(x, x, x, x))

print(n1+n2+n3+n4)