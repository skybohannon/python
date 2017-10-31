game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

def display_winner(player):
    if player == 0:
        print("Tie")
    else:
        print("Player " + str(player) + " wins!")


def switch_player(player):

    if player == 1:
        return 2
    else:
        return 1

def draw_line(width, edge, filling):
    print(filling.join([edge] * (width + 1)))


def display_game(game):
    d = {2: "O", 1: "X", 0: "_"}
    draw_line(3, " ", "_")
    for row_num in range(3):
        new_row = []
        for col_num in range(3):
            new_row.append(d[game[row_num][col_num]])
        print("|" + "|".join(new_row) + "|")

def add_piece(game, player, row, column):

    game[row][column] = player
    return game

def convert_input(user_input):
    # user will input 1-3, but lists start with 0
    # so subtract 1 from user input
    return user_input - 1

def check_space_empty(game, row, column):
    return game[row][column] == 0

def check_row_winner(row):
    """
    Return the player number that wins for that row.
    If there is no winner, return 0.
    """
    if row[0] == row[1] and row[1] == row[2]:
        return row[0]
    return 0


def get_col(game, col_number):
    return [game[x][col_number] for x in range(3)]

def get_row(game, row_number):
    return game[row_number]

def check_winner(game):
    game_slices = []
    for index in range(3):
        game_slices.append(get_row(game, index))
        game_slices.append(get_col(game, index))

    # check diagonals
    down_diagonal = [game[x][x] for x in range(3)]
    up_diagonal = [game[0][2], game[1][1], game[2][0]]
    game_slices.append(down_diagonal)
    game_slices.append(up_diagonal)

    for game_slice in game_slices:
        winner = check_row_winner(game_slice)
        if winner != 0:
            return winner

    return winner


if __name__ == '__main__':
    winner = 0
    player = 1

    while winner == 0:
        print("Player " + str(player) + ", it's your turn.")
        available = False
        while not available:
            row = convert_input(int(input("Which row? ")))
            column = convert_input(int(input("Which column? ")))
            available = check_space_empty(game, row, column)
        game = add_piece(game, player, row, column)
        display_game(game)
        player = switch_player(player)
        winner = check_winner(game)

    display_winner(winner)