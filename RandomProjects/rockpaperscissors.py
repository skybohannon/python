print("Rock, Paper, Scissors")

newGame = "Y"

while newGame == "Y":
    player1 = input("Player 1, please enter your move: ").upper()
    player2 = input("Player 2, please enter your move: ").upper()

    if player1 == player2:
        print("Tie. Both of you had the same move.")
        break

    elif player1 == "SCISSORS":
        if player2 == "ROCK":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")

    elif player1 == "PAPER":
        if player2 == "ROCK":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

    elif player1 == "ROCK":
        if player2 == "PAPER":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")

    else:
        print("Not a valid input")
        break

    newGame = input("Would you like to play again? y/n ").upper()
