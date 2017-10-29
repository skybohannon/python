running = True
player = 1
counter = 0


def start_game():
    return [[0, 0, 0] for x in range(3)]


def horiz_line():
    print(" ----" * 3)


def vert_line():
    print("|    ")


def draw_line(width, edge, filling):
    print(filling.join([edge] * (width + 1)))


def draw_board(width, height):
    draw_line(width, " ", "__")
    for i in range(height):
        draw_line(width, "|", "__")
    print("\n")

def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1

while running:

    game = start_game()

    if game == [['O', 'O', 'O'],
               ['X', 'X', 'X'],
               [0, 0, 0]]:
        print("Player 1 won in {} turns!".format(counter))
        break

    if player == 1:
        player1Input = input("Player 1 please make a move: ").strip()
        if len(player1Input) != 3:
            print("Input wrong length. Do not use spaces to separate.")
        player1List = list(player1Input.split(","))
        player1First = int(player1List[0]) - 1
        player1Second = int(player1List[1]) - 1
        game[player1First][player1Second] = "O"
        print(", ".join(str(x) for x in game))
        player = switch_player(player)
        counter += 1
    else:
        player2Input = input("Player 2 please make a move: ").strip()
        if len(player2Input) != 3:
            print("Input wrong length. Do not use spaces to separate.")
        player2List = list(player2Input.split(","))
        player2First = int(player2List[0]) - 1
        player2Second = int(player2List[1]) - 1
        game[player2First][player2Second] = "X"
        print(", ".join(str(x) for x in game))
        player = switch_player(player)
        counter += 1
