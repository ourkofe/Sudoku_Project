import random

def generate_sudoku(): # 스도쿠 퍼즐 생성
    board = initialize_board()
    solve_sudoku(board)
    remove_numbers(board)
    return board

def remove_numbers(board):
    empty_cells = random.sample(range(81), 40)  # 랜덤하게 40개의 숫자를 제거
    for idx in empty_cells:
        row = idx // 9
        col = idx % 9
        board[row][col] = 0