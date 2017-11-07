game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1

def draw_line(width, edge, filling):
    print(filling.join([edge] * (width + 1)))


def display_game(game):
    d = { 2: "2", 1: "1", 0: "_"}
    draw_line(3, " ", "_")

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