import random

passChars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&**()"

try:
    passLength = int(input("How many characters do you want your password to be? "))
    finalPass = "".join(random.sample(passChars, passLength))
    print(finalPass)

except ValueError:
    print("You did not enter a number")
