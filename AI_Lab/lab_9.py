n = 4
board = [[0 for r in range(n)] for c in range(n)]

def print_board(board):
    for row in board:
        print(row)


def is_safe(board, row, col, n):
    for i in range(n):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, col, n):
    if col == n:
        print_board(board)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            if solve(board, col + 1, n):
                return True
            else:
                board[i][col] = 0
    return False

solve(board, 0, n)
