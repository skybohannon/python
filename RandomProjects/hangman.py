import random

with open ('sowpods.txt', 'r') as sowpods:
    wordList = list(sowpods)
    chosenWord = random.choice(wordList).strip()
    chosenWordList = list(chosenWord)

running = True
userWordList = "_" * len(chosenWordList)
userWordList = list(userWordList)
guessedList = []
counter = 1

print("HANGMAN!\n" + " ".join(str(x) for x in userWordList))
userLetter = input("Please enter a letter to guess: ").upper()

while running:

    if userLetter in guessedList:
        userLetter = ''
        print("Already guessed!")
        counter += 1

    elif userLetter in chosenWordList:
        index = chosenWordList.index(userLetter)
        userWordList[index] = userLetter
        chosenWordList[index] = '_'
    else:
        if userLetter is not '':
            guessedList.append(userLetter.upper())
        print(" ".join(str(x) for x in userWordList))
        userLetter = input("Please guess another letter: ").upper()
        counter += 1

    if '_' not in userWordList:
        print("You guessed in {} tries! The word was {}".format(counter, chosenWord))
        running = False
