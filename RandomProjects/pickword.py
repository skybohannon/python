import random

with open ('sowpods.txt', 'r') as sowpods:
    randomWordLines = sowpods.read().splitlines()
    randomWord = random.choice(randomWordLines).strip()
    print("Your random word is: {}".format(randomWord))