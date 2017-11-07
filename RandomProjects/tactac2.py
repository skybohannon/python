game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1

def draw_line():
    print(" _ _ _ ")


def display_game(game):
    d = {2: "O", 1: "X", 0: "_"}
    draw_line()
    for row_num in range(3):
        new_rows = []
        for col_num in range(3):
            new_rows.append(d[game[row_num][col_num]])
        print("|" + "|".join(new_rows) + "|")

def convert_input(user_input):
    return user_input - 1


def add_piece(game, player, row, column):
    game[row][column] = player
    return game

def check_availability(game, row, column):
    return game[row][column] == 0



winner = 0
player = 1

while winner == 0:
    print("Player {}, it's your move.".format(str(player)))

    available = False
    while not available:
        row = convert_input(int(input("Which row? ")))
        column = convert_input(int(input("Which column? ")))
        available = check_availability(game, row, column)

    game = add_piece(game, player, row, column)
    display_game(game)
    player = switch_player(player)