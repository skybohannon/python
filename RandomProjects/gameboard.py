def horiz_line():
    print(" ----" * boardSize)

def vert_line():
    print("|    " * (boardSize + 1))

try:
    boardSize = int(input("Using a single number, what size board would you like? "))

    print(range(boardSize))
    for i in range(boardSize):
        horiz_line()
        vert_line()
    horiz_line()

except ValueError:
    print("You did not enter a number.")
