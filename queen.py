def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    
    for i in range(row):
        if board[i][col]:
            return False

    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row):
    if row >= len(board):
        print_solution(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True  
            if solve_n_queens(board, row + 1):
                board[row][col] = False  
            else:
                board[row][col] = False  

    return False

def solve_8_queens():
    board = [[False for _ in range(8)] for _ in range(8)]
    solve_n_queens(board, 0)

if __name__ == "__main__":
    solve_8_queens()
