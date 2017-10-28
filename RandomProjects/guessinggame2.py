import random

userNum = int(input("Please enter a number from 1-100: "))
lowNumber = 1
highNumber = 100
running = True
guessedNum = random.randint(lowNumber, highNumber)

while running:
    counter = 1

    if guessedNum == userNum:
        print("The number was {}! The computer guessed right the first time!".format(guessedNum))

    while guessedNum != userNum:
        lowOrHigh = input("The computer guessed {}. Was this lower of higher? ".format(guessedNum))

        if lowOrHigh.lower() == "lower":
            lowNumber = guessedNum
            guessedNum = random.randint(lowNumber, highNumber)
        elif lowOrHigh.lower() == "higher":
            highNumber = guessedNum
            guessedNum = random.randint(lowNumber, highNumber)
        counter += 1

    print("The number was {} and it took {} tries.".format(guessedNum, counter))
    running = False
