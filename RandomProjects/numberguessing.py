import random

generatedNumber = random.randint(1, 10)

userNum = 0
guessCount = 0
print("IT'S THE GUESSIN' GAME. YOU GOTTA GUESS A NUMBER BETWEEN ONE AND TEN!")

while userNum != generatedNumber and userNum != 'exit':
    userNum = input("Please enter a number between 1 and 10: ")

    if userNum == 'exit':
        break

    userNum = int(userNum)  # convert to int after check to see if user entered "exit"
    guessCount += 1  # increase guess count

    if userNum > generatedNumber:
        print("Your guess was too high.")
    elif userNum < generatedNumber:
        print("Your guess was too low.")
    else:
        print("You were right! The number was {} and it took you {} tries.".format(generatedNumber, guessCount))
        break
