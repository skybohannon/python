# Question 14
# Level 2
#
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

cases = {"UPPERCASE": 0,
         "LOWERCASE": 0
         }
userInput = input("UPPER N' LOWER CASE CALCULATOR!\nPlease enter a sentence: ")

for char in userInput:
    if char.isupper():
        cases["UPPERCASE"] += 1
    if char.islower():
        cases["LOWERCASE"] += 1

print("\nUPPER CASE: {}\nLOWER CASE: {}".format(cases["UPPERCASE"], cases["LOWERCASE"]))