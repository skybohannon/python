# Question 11
# Level 2
#
# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
# whether they are divisible by 5 or not.  The numbers that are divisible by 5 are to be printed in a
# comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

userInput = input("Please enter a comma separated list of 4 digit binary numbers: ")
userInputList = [int(i) for i in userInput.split(",")]
divBy5 = []

for i in userInputList:
    if i % 5 == 0:
        divBy5.append(str(i))

print("Numbers divisible by 5: {}".format(", ".join(divBy5)))
