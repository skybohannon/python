# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first
# half values in one line and the last half values in one line.
#
# Hints:
#
# Use [n1:n2] notation to get a slice from a tuple.

s = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

firstHalf = s[:5]
lastHalf = s[5:]

print(firstHalf)
print(lastHalf)