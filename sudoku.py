#prints the board
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

#This function checks whether to place a number in a given board[row][column] or not

def is_valid(board, row, col, num):

    # This seaches the row and sees if any dupe number is present in the row, if it is, returns false
    if num in board[row]:
        return False

    # As you might have guessed, this checks the columns similar to the above approach.
    for r in range(9):
        if board[r][col] == num:
            return False

    # This one is to seach within the 3x3 sub-grid whether there is any duplicate value or not
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False


    # If none of those are false then it indeed must be valid so we return valid
    return True


# Just some bunch of for loops, and validation check, ez
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


sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(sudoku_board):
    print("Sudoku solved:")
    print_board(sudoku_board)
else:
    print("No solution exists")
