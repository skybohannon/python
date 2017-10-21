import random

roll = random.randint(1, 6)
tries = 1

while (tries <= 6):
    try:
        guess = int(input("You have 6 guesses. You're on guess " + str(tries) + ".\nPlease enter a number between 1 and 6: ").format(tries))

        while (guess > 6):
            print("Your guess was too high. Try again.")
            guess = int(input("Please enter a number between 1 and 6: "))

        tries += 1

        if guess < roll:
            print("Your guess was too low. Try again.")
        elif guess > roll:
            print("Your guess was too high. Try again.")
        else:
            break
        if guess == roll:
            print("You guessed right! " + str(roll) + " was the right number!")

    except ValueError:
        print("Not a number. You don't deserve this. We're finished here!")
        break


