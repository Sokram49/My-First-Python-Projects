''' Tic-Tac-Toe game with the help of ChatGPT
    I added replayability and total scores features '''

board = [[" " for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def make_move(board, player, row, col):
    if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == ' ':
        board[row - 1][col -1] = player
        return True
    else:
        return False

current_player = 'X'
x_score = 0
o_score = 0
while True:
    display_board(board)
    print(f"Player {current_player}'s turn.")

    row = int(input("Enter row (1, 2, or 3): "))
    col = int(input("Enter column (1, 2, or 3): "))

    if make_move(board, current_player, row, col):
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            if current_player == "X":
                x_score += 1
            else:
                o_score += 1
            replay = input("Would you like to play again? (y/n): ")
            if replay.lower() == "y":
                board = [[" " for _ in range(3)] for _ in range(3)]
                continue
            else:
                print(f"Thank you for playing! Player X's total score: {x_score} | Player O's total score: {o_score}")
                break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            replay = input("Would you like to play again? (y/n): ")
            if replay.lower() == "y":
                board = [[" " for _ in range(3)] for _ in range(3)]
                continue
            else:
                print(f"Thank you for playing! Player X's total score: {x_score} | Player O's total score: {o_score}")
                break
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        print("Invalid move. Try again.")
