# EXERCISE
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the
# user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly
# in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user
# makes throughout the game and tell the user at the end.
import random

generated = str(random.randint(1000, 9999))
generatedList = [x for x in generated]

running = True
counter = 0

while running:
    userGuess = input("Please guess a 4 digit number: ")
    userList = [x for x in userGuess]
    cows = 0
    bulls = 0

    for i in range(0, 4):
        if userList[i] == generatedList[i]:
            cows += 1
        else:
            bulls += 1

    print("{} cows and {} bulls".format(cows, bulls))
    counter += 1

    if userGuess == generated:
        print("You won! The number was {} and it took you {} tries.".format(userGuess, str(counter)))
        running = False
