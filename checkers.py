''' Bare-Bones Checkers Game '''

board = [[" " for _ in range(8)] for _ in range(8)]

for row in range(8):
    if row % 2 == 0:
        start_col = 1
    else:
        start_col = 0

    for col in range(start_col, 8, 2):
        if row < 3:
            board[row][col] = "R"
        elif row > 4:
            board[row][col] = "B"

def display_board():
    for row in board:
        print(" ".join(row))

def make_move(board, start_row, start_col, dest_row, dest_col):
    board[dest_row][dest_col] = board[start_row][start_col]
    board[start_row][start_col] = " "

    if abs(dest_row - start_row) == 2:
        captured_row = (start_row + dest_row) // 2
        captured_col = (start_col + dest_col) // 2
        board[captured_row][captured_col] = " "

def has_pieces_remaining():
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == player:
                game = False
                return game

player = "R"
game = True
while game:
    display_board()
    print(f"It's Player {player}'s turn now.")

    start_row = int(input("Enter starting row: ")) - 1
    start_col = int(input("Enter staring column: ")) - 1
    dest_row = int(input("Enter destined row: ")) - 1
    dest_col = int(input("Enter destined column: ")) - 1

    make_move(board, start_row, start_col, dest_row, dest_col)
    
    player = "B" if player == "R" else "R"

    if not has_pieces_remaining():
        print(f"Player {player} won the game!")
        break

print("Thank you for playing.")
