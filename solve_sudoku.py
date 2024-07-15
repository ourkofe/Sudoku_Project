def solve_sudoku(board):
    empty_cell = find_empty_cell(board) # 비어있는 칸 찾기
    if not empty_cell:
        return board # 보드가 다 채워짐

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return board
            board[row][col] = 0  # Backtrack
    return None

def find_empty_cell(board): # 보드에서 0이 들어있는 칸을 찾는 함수
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0: # 0을 찾으면 해당 좌표 반환
                return (i, j)
    return None

def is_valid_move(board, row, col, num): # 숫자가 스도쿠 규칙에 맞는지 확인
    return (
        is_valid_row(board, row, num) and # 행의 숫자 확인
        is_valid_col(board, col, num) and # 열의 숫자 확인
        is_valid_box(board, row - row % 3, col - col % 3, num) # 해당 숫자가 3x3 박스에 있는지 확인
    )

def is_valid_row(board, row, num): # 숫자가 행에 이미 있는지 확인
    return num not in board[row]

def is_valid_col(board, col, num): # 숫자가 열에 이미 있는지 확인
    return num not in [board[i][col] for i in range(9)]

def is_valid_box(board, start_row, start_col, num): # 해당 숫자가 3x3 박스에 있는지 확인
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True