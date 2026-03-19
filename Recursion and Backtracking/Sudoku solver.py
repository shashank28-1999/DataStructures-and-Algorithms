#solve sudoku
def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def is_valid(board, r, c, num):
    if any(board[r][i] == num for i in range(9)): return False
    if any(board[i][c] == num for i in range(9)): return False
    br, bc = 3 * (r // 3), 3 * (c // 3) # rounds to nearest integer
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    for num in range(1, 10):
        if is_valid(board, r, c, num):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0
    return False

board = [[0]*9 for _ in range(9)]
solve(board)
for row in board:
    print(row)