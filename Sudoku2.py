M = 9

def puzzle(a):
    print("\nSolved Sudoku:\n")
    for i in range(M):
        for j in range(M):
            print(a[i][j], end=" ")
        print()

def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[startRow + i][startCol + j] == num:
                return False
    return True

def Sudoku(grid, row, col):
    if row == M - 1 and col == M:
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Sudoku(grid, row, col + 1)
    
    for num in range(1, M + 1):
        if solve(grid, row, col, num):
            grid[row][col] = num
            if Sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False

# --- Input from user ---
print("Enter the Sudoku puzzle row by row (9 space-separated integers per row, use 0 for empty cells):\n")

grid = []
for i in range(9):
    while True:
        try:
            row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
            if len(row) != 9 or any(not (0 <= n <= 9) for n in row):
                raise ValueError
            grid.append(row)
            break
        except ValueError:
            print("Invalid input! Please enter exactly 9 numbers between 0 and 9.")

# --- Solve the Sudoku ---
if Sudoku(grid, 0, 0):
    puzzle(grid)
else:
    print("\nSolution does not exist :(")
