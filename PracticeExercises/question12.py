# Question 12
# Level 2
#
# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

numberRange = range(1000, 3001)
numberRangeList = [str(i) for i in numberRange]
allDivisible = []

for x in numberRangeList:
    if int(x[0]) % 2 == 0 and int(x[1]) % 2 == 0 and int(x[2]) % 2 == 0 and int(x[3]) % 2 == 0:
        allDivisible.append(str(x))

print(", ".join(allDivisible))
