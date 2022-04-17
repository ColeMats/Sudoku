sudoku_game = [[0, 3, 1, 6, 0, 7, 0, 0, 0],
                [6, 0, 0, 8, 0, 0, 2, 5, 7],
                [8, 0, 0, 0, 9, 0, 6, 0, 3], 
                [4, 0, 0, 0, 0, 0, 8, 3, 2], 
                [0, 1, 0, 0, 6, 9, 0, 0, 0], 
                [7, 0, 3, 2, 4, 0, 0, 0, 6], 
                [9, 0, 2, 4, 0, 1, 0, 7, 8], 
                [0, 8, 5, 0, 0, 0, 0, 0, 9], 
                [3, 0, 4, 0, 0, 0, 0, 6, 1]]

# Process:
# 1. Find an Empty Cell
# 2. Try all values until one works
# 3. Move on the next empty cell
# 4. Try all values until one works
# 4a. If one works, move on to next empty cell.
# 4b. If one does not work, go back to previous cell and 
#     try another value that works
# Repeat step four

# prints board to terminal in a readable format
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

# Searches through all rows to find first empty cell and return the empty cell's position
def find_empty_cell(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return (row, column)
    return None

# Checks to see if the cell fits within the row, column, and 3x3 square
def check(board, value, position):
    
    # Checks the row to see if any values match
    for i in range(len(board[0])):
        if board[position[0]][i] == value and position[1] != i:
            return False

    # Checks the columns to see if any values match
    for i in range(len(board[0])):
        if board[i][position[1]] == value and position[0] != i:
            return False

    # Checks the 3x3 square to see if any values match
    start_x = position[1] 
    start_y = position[0]
    
    start_x -= position[1] % 3
    start_y -= position[0] % 3

    for i in range(0, 3):
        for j in range(0, 3):
            if board[start_y + i][start_x + j] == value and position[1] != start_x + j and position[0] != start_y + i:
                return False

    # Returns true if value passes all checks
    return True

def solve_sudoku(board):
    position = find_empty_cell(board)
    if not position:
        return True
    else:
        row, col = position
    
    for value in range(1, 10):
        if check(board, value, (row, col)):
            board[row][col] = value
            if solve_sudoku(board):
                return True

            board[row][col] = 0
    return False

print_board(sudoku_game)
print('\n')
solve_sudoku(sudoku_game)
print_board(sudoku_game)