# Question 13
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

numbers = 0
letters = 0

userInput = input("LETTERS AND NUMBERS CALCULATOR!!\nPlease enter a sentence that also contains numbers: ")
for i in userInput:
    if i.isalpha() is True:
        letters += 1
    if i.isdigit() is True:
        numbers += 1

print("LETTERS: {}\nNUMBERS: {}".format(letters, numbers))