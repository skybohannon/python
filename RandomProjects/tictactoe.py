game = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

player1Input = "1,3".strip()
player1List = list(player1Input.split(","))

print(len(player1Input))
if len(player1Input) != 3:
    print("Input wrong length. Do not use spaces to separate.")

print(player1List)
player1First = int(player1List[0]) - 1
player1Second = int(player1List[1]) - 1

game[player1First][player1Second] = "O"
print(game)
