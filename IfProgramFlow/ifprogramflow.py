# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# else :
#     print("Please come back in {0} years".format(18-age))

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess <5:
        print("Please guess a higher number")
    else: #must be greater than 5
        print("Please guess a lower number")

    guess = int(input())
    if guess == 5:
        print("Well done, you've guessed it, you crazy bastard!")
    else:
        print("Sorry, you have not guessed correctly after two guesses, dingus.")

else:
    print("YEAH SON! You've guessed it first try!")