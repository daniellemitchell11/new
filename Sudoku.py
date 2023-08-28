import random

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve(board)

    # Remove numbers to create a puzzle
    num_to_remove = random.randint(30, 40)
    cells = [(row, col) for row in range(9) for col in range(9)]
    random.shuffle(cells)

    for _ in range(num_to_remove):
        row, col = cells.pop()
        removed_value = board[row][col]
        board[row][col] = 0

        # Check if the puzzle still has a unique solution
        temp_board = [row[:] for row in board]
        if not solve(temp_board):
            board[row][col] = removed_value

    return board

if __name__ == "__main__":
    sudoku_board = generate_sudoku()
    print("Generated Sudoku Puzzle:")
    print_board(sudoku_board)
    
    while True:
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))
        
        if is_valid(sudoku_board, row, col, num):
            sudoku_board[row][col] = num
            print_board(sudoku_board)
        else:
            print("Invalid move! Try again.")
        
        if all(all(cell != 0 for cell in row) for row in sudoku_board):
            print("Congratulations! You solved the Sudoku puzzle!")
            break
