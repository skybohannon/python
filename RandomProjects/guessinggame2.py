import random

userNum = int(input("Please enter a number from 1-100: "))

while True:
    counter = 1
    guessedNum = random.randint(1, 100)
    if guessedNum == userNum:
        print("The number was {}! The computer guessed right the first time!".format(guessedNum))

    lowNumber = 1
    highNumber = 100

    while guessedNum != userNum:
        lowOrHigh = input(print("The counter guessed {}. Was this lower of higher?".format(guessedNum)))

        if lowOrHigh =="lower":
            lowNumber = guessedNum
            guessedNum = random.randint(lowNumber, highNumber)
            counter += 1
        else:
            highNumber = guessedNum
            guessedNum = random.randint(lowNumber, highNumber)
            counter += 1

    print("The number was {} and it took {} tries.".format(guessedNum, counter))

