# for i in range (10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# availableExits = ["east", "northeast", "south", ]
#
# chosenExit = ''
# while chosenExit not in availableExits:
#     chosenExit = input("Please choose a direction: ")
#     if chosenExit == "quit":
#         print("Game Over")
#         break
# else:
#     print("Aren't you glad you got out of there?")

import random

highest = 10
answer = random.randint(1, highest)

print("Please enter a number between 1 and {}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly. The answer was {}".format(answer))
else:
    print("You got it first try")
