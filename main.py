
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if any(board[i][col] == num for i in range(9)):
        return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    if any(board[start_row + i][start_col + j] == num for i in range(3) for j in range(3)):
        return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False  
    return True

board = [
    [0, 0, 5, 9, 1, 0, 0, 2, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 1, 0, 0, 2, 0, 0, 0],
    [0, 0, 2, 6, 0, 7, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 5, 0, 0, 4, 9, 0],
    [6, 0, 0, 2, 0, 0, 0, 5, 0],
    [0, 8, 0, 0, 0, 4, 0, 0, 0],
    [3, 0, 7, 0, 0, 0, 2, 0, 0]
]

if solve_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))
else:
    print("No solution exists.")