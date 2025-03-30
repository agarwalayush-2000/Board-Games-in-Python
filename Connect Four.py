connect_four = [["." for _ in range(7)] for _ in range(6)]

def print_board(connect_four):
    print("1 2 3 4 5 6 7")
    for row in connect_four:
        print(" ".join(row))

def update_board(connect_four, row_tracker, move, player):
    row = row_tracker[move]
    column = move
    piece = "X" if player == 1 else "O"
    connect_four[row][column] = piece
    row_tracker[move] -= 1

def check_winner(board, piece):
    for r in range(6):
        for c in range(7 - 3):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
    
    for r in range(6 - 3):
        for c in range(7):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
    
    for r in range(6 - 3):
        for c in range(7 - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
    
    for r in range(3, 6):
        for c in range(7 - 3):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True
    
    return False

def get_valid_move(row_tracker):
    while True:
        try:
            move = int(input("Enter column (1-7): ")) - 1
            if 0 <= move < 7 and row_tracker[move] >= 0:
                return move
            else:
                print("Invalid move. Column full or out of bounds. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 7.")

row_tracker = [5 for _ in range(7)]

for i in range(1, 43):
    player = 1 if i % 2 else 2
    print_board(connect_four)
    move = get_valid_move(row_tracker)
    update_board(connect_four, row_tracker, move, player)
    
    if check_winner(connect_four, "X" if player == 1 else "O"):
        print_board(connect_four)
        print(f"Player {player} won!!")
        break
else:
    print("It's a draw!!")
