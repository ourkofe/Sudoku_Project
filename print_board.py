def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '-' for num in row))

board = initialize_board()
print_board(board)